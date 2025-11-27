import pygame
from config import *

class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.sound_volumes = {}

        self.muted = False

        self.sound_volumes["Button"] = VOL_SELECT
        self.sound_volumes["Jump"] = VOL_JUMP
        self.sound_volumes["Bounce"] = VOL_BOUNCE
        self.sound_volumes["Music"] = VOL_SOUND

    def load_sound(self, name, path, volume=1.0):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        self.sounds[name] = sound
        self.sound_volumes[name] = volume

    def play_sound(self, name):
        if not self.muted and name in self.sounds:
            self.sounds[name].play()

    def play_music(self, name):
        if not self.muted and name in self.sounds:
            self.sounds[name].play(-1)

    def stop_music(self, name):
        self.sounds[name].stop()
    
    def mute(self):
        self.muted = True
        pygame.mixer.music.set_volume(0)
        for sound in self.sounds.values():
            sound.set_volume(0)
    
    def unmute(self):
        self.muted = False
        pygame.mixer.music.set_volume(self.sound_volumes["Music"])
        for sound_name in self.sounds:
            self.sounds[sound_name].set_volume(self.sound_volumes[sound_name])

    def toggle_mute(self):
        if self.muted:
            self.unmute()
        else:
            self.mute()
