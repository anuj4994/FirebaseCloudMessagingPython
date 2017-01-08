# FirebaseCloudMessagingPython
This script will send notifications to applications in which firebase cloud messaging is enabled.

Run this script on any server. And make request to ip:port/sendMessage path. Pass post parameter of apiKey of application registrationId of device and title and body of message.
And notification will be sent.
Code is running on following path.
http://54.70.113.238:7001/sendMessage/

parameters:
RequestParams params  = new RequestParams();

params.put("regId","device registration id ");

params.put("title","Response Added");

params.put("apiKey"," your api key");

params.put("body","Response to your request has been added by admin. Please check as soon as possible.");

