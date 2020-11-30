# Pi Sound Machine

Using the [pHAT BEAT](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-phat-beat) from [Pimoroni](https://learn.pimoroni.com/) I was able to make a very rudimentary sound machine to play white noise at night while I sleep.

The configuration scripts from Pimoroni should install the essential libraries and configuration files needed for the pHAT BEAT to function.

The script uses `mpg123` to play the audio file. Make sure that is installed.

Add this to `/etc/rc.local` to get the script to run at boot.

```
sudo -u pi python3 /home/pi/pi-sound-machine/audio.py &
```

This line in `/etc/asound.conf` disables the lights on the pHAT BEAT.

```
pcm_scope.pivumeter {
    ...
    brightness 0
    ...
}
```

The `play/pause` button works as expected as should the `+` and `-` for changing volume. Modify the code as expected and copy over an `mp3` audio file for the white noise as needed.
