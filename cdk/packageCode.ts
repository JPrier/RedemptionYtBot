import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import archiver from 'archiver';

// Directories
const distDir = '../dist';
const srcDir = '../service';
const zipFile = 'lambda_function.zip';

// Helper function to run commands synchronously
function runCommand(command: string) {
  try {
    execSync(command, { stdio: 'inherit' });
  } catch (error) {
    console.error(`Error running command: ${command}`);
    process.exit(1);
  }
}

// Function to recursively copy files and directories
function copyDirectory(srcDir: string, distDir: string) {
  // Ensure the destination directory exists
  if (!fs.existsSync(distDir)) {
    fs.mkdirSync(distDir, { recursive: true });
  }

  // Read the contents of the source directory
  fs.readdirSync(srcDir).forEach((file) => {
    const srcPath = path.join(srcDir, file);
    const distPath = path.join(distDir, file);

    // Check if the current item is a file or a directory
    const stat = fs.statSync(srcPath);

    if (stat.isDirectory()) {
      // If it's a directory, recursively copy its contents
      copyDirectory(srcPath, distPath);
    } else {
      // If it's a file, copy it
      fs.copyFileSync(srcPath, distPath);
    }
  });
}

// Function to package Lambda function
function packageLambda() {
  // Clean up old files
  console.log('Cleaning up old files...');
  if (fs.existsSync(distDir)) {
    fs.rmdirSync(distDir, { recursive: true });
  }
  fs.mkdirSync(distDir);

  // Copy Lambda function code
  console.log('Copying Lambda function code...');
  copyDirectory(srcDir, distDir);

  // Install dependencies
  console.log('Installing dependencies...');
  runCommand('pipenv requirements > requirements.txt');
  runCommand(`pipenv run pip install -r ./requirements.txt --target ${distDir}`);

  // Zip the Lambda package
  console.log('Zipping Lambda package...');
  const output = fs.createWriteStream(zipFile);
  const archive = archiver('zip', { zlib: { level: 9 } });

  archive.pipe(output);
  archive.directory(distDir, false);
  archive.finalize();

  output.on('close', () => {
    console.log(`Package created: ${zipFile}`);
  });
}

packageLambda();
