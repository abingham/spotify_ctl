#! /usr/bin/env python

import subprocess

import baker

def cmd(c):
    subprocess.call('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.{0}'.format(c).split())

@baker.command
def play_pause():
    cmd('PlayPause')

@baker.command
def next():
    cmd('Next')

@baker.command
def previous():
    cmd('Previous')

if __name__ == '__main__':
    baker.run()

#def volume_up():
#    subprocess.call('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Volume 10'.split())

'''
$ mdbus2 org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2
[METHOD]    org.mpris.MediaPlayer2.Raise() -> ()
[METHOD]    org.mpris.MediaPlayer2.Quit() -> ()
[PROPERTY]  org.mpris.MediaPlayer2.read( b:CanQuit )
[PROPERTY]  org.mpris.MediaPlayer2.read( b:CanRaise )
[PROPERTY]  org.mpris.MediaPlayer2.read( b:HasTrackList )
[PROPERTY]  org.mpris.MediaPlayer2.read( s:Identity )
[PROPERTY]  org.mpris.MediaPlayer2.read( s:DesktopEntry )
[PROPERTY]  org.mpris.MediaPlayer2.read( as:SupportedUriSchemes )
[PROPERTY]  org.mpris.MediaPlayer2.read( as:SupportedMimeTypes )
[METHOD]    org.mpris.MediaPlayer2.Player.Next() -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.Previous() -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.Pause() -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.PlayPause() -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.Stop() -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.Play() -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.Seek( x:Offset ) -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.SetPosition( o:TrackId, x:Position ) -> ()
[METHOD]    org.mpris.MediaPlayer2.Player.OpenUri( s:none ) -> ()
[SIGNAL]    org.mpris.MediaPlayer2.Player.Seeked( x:Position )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( s:PlaybackStatus )
[PROPERTY]  org.mpris.MediaPlayer2.Player.readwrite( s:LoopStatus )
[PROPERTY]  org.mpris.MediaPlayer2.Player.readwrite( d:Rate )
[PROPERTY]  org.mpris.MediaPlayer2.Player.readwrite( b:Shuffle )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( a{sv}:Metadata )
[PROPERTY]  org.mpris.MediaPlayer2.Player.readwrite( d:Volume )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( x:Position )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( d:MinimumRate )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( d:MaximumRate )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( b:CanGoNext )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( b:CanGoPrevious )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( b:CanPlay )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( b:CanPause )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( b:CanSeek )
[PROPERTY]  org.mpris.MediaPlayer2.Player.read( b:CanControl )
[METHOD]    org.freedesktop.DBus.Properties.Get( s:interface_name, s:property_name ) -> ( v:value )
[METHOD]    org.freedesktop.DBus.Properties.Set( s:interface_name, s:property_name, v:value ) -> ()
[METHOD]    org.freedesktop.DBus.Properties.GetAll( s:interface_name ) -> ( a{sv}:values )
[METHOD]    org.freedesktop.DBus.Introspectable.Introspect() -> ( s:xml_data )

http://www.mabishu.com/blog/2010/11/15/playing-with-d-bus-interface-of-spotify-for-linux/
'''
