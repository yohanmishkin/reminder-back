# remindr [![Build Status](https://travis-ci.org/yohanmishkin/remindr.svg?branch=master)](https://travis-ci.org/yohanmishkin/remindr)


Ember app 
	> phone #, cron, message
	> Stripe checkout 
		> returns Stripe token
	> Lambda (handler.schedule_remindr())
		> creates mp3 (put number in filename?)
		> uploads to S3
		> schedules remindr (with parameters?)
			> Lambda (handler.process_remindr())
				> uses Twilio to call number with mp3