import { Environment } from 'aws-cdk-lib';
import { CHANNEL_IDS } from './channels';
import { API_KEY, OAUTH_KEY } from './keys';

export interface StageProps {
  name: string;
  env: Environment;
  channels: string[];
  apiKey: string;
  oauthKey: string;
  frequencyInMinutes: number;
}

export const TEST: StageProps = {
  name: 'Test',
  env: {
    account: '476114139282',
    region: 'us-west-2'
  },
  channels: CHANNEL_IDS,
  apiKey: API_KEY,
  oauthKey: OAUTH_KEY,
  frequencyInMinutes: 720,
};

export const STAGES = [TEST];
