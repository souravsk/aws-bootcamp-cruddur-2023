import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class ThumbingServerlessCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const bucketname: string = process.env.THUMBING_BUCKET_NAME as string;
    const bucket = this.createBucket(bucketname);
  }
  createBucket(bucketName: string): s3.IBucket{
    const bucket = new s3.Bucket(this, 'Thumbingbucket', {
      bucketName: bucketName,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });
    return bucket;
  }
}
