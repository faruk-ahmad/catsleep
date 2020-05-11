# catsleep
A lightweight tool that reminds user to take break after a certain time period.



## 1. Configuration Examples
--------------------------------------------------

Configuration file can be found in users Home directory, named ".catsleep_config.json"

### 1.1 Interval configuration
You can configure the interval in between two alarms or notifications by modifying the configuration file.

* The alarm will be played after 30 minutes

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

If you want to set the interval as 1 hour instead of default 30 minutes, then change the value in the interval field as bellow-

* The alarm will be played after 1 hour or 60 minutes

```json
{
	"interval_minutes": 60,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

N.B. Interval needs to be input in minutes.


### 1.2 Frequency configuration
The frequency of notifications means, how many times you want the alarm to be played at a time. You can configure the frequency by modifying the configuration file.

* The alarm will be played only once at a slot

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

If you want to set the frequency 2 instead of default 1 , then change the value in the frequency field as bellow-

* The alarm will be played twice at a slot.

```json
{
	"interval_minutes": 30,
	"frequency_number": 2,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

N.B. The frequency should be integer number.



### 1.3 Frequency interval configuration
The frequency interval of notifications means, how much gap time you want in between consecutive alarms at a slot. You can configure the frequency interval by modifying the configuration file.

* The alarm will be played twice after 30 minutes with a gap of 2 minutes in between

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

If you want to set the frequency interval 5 instead of default 1 , then change the value in the frequency interval field as bellow-

* The alarm will be played twice by a gap of 5 minutes at a slot.

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 5,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

N.B. The frequency interval should be in minutes and less than the interval value.


### 1.4 Audio configuration
You can either turn the audio message on or off by modifying configuration file. The possible values are "yes" and "no". Any value except "yes" are considered to be as "no"


* Audio message will be played.

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

If you want to turn the audio message off, then put "no" in the play_audio field.

* Audio message is turned off-

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "no",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

N.B. Any value except "yes" is considered to be as "no"



### 1.5 Text Notification configuration
You can either turn the text message on or off by modifying configuration file. The possible values are "yes" and "no". Any value except "yes" are considered to be as "no"


* Text message will be displayed.

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

If you want to turn the text message off, then put "no" in the show_text field.

* Text message is turned off-

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "no",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

N.B. Any value except "yes" is considered to be as "no"



### 1.6 Beep Notification configuration
You can either turn the Beep sound on or off by modifying configuration file. The possible values are "yes" and "no". Any value except "yes" are considered to be as "no"


* Beep sound will be played.

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

If you want to turn the Beep sound off, then put "no" in the play_beep field.

* Beep sound is turned off-

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "no",
	"voice_mode": "random"
}
```

N.B. Any value except "yes" is considered to be as "no"



### 1.7 Voice mode configuration
You can choose the mode of voice message to be played. You can choose "male", "female" or "random" selected voice messasge. 


* Male voice will be played.

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "male"
}
```


* Female voice will be played.

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "female"
}
```

* Randomly selected voice will be played.

```json
{
	"interval_minutes": 30,
	"frequency_number": 1,
	"frequency_interval_minutes": 1,
	"play_audio_on": "yes",
	"show_text_on": "yes",
	"play_beep_on": "yes",
	"voice_mode": "random"
}
```

N.B. Any value except "male", "female" and "random" is considered to be random.

--------------------------------------------------
