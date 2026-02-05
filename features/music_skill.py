# features/music_skill.py
from features.skill_base import Skill
from core.memory import Memory
from utils.logger import log_info

memory = Memory()

class PlaySongSkill(Skill):
    name = "play_song"

    def run(self, entities=None):
        song = entities.get("song") if entities else None
        if not song:
            last_song = memory.get("last_song")
            if last_song:
                song = last_song
            else:
                return "Please tell me the song name."
        memory.update("last_song", song)
        log_info(f"Playing song: {song}")
        return f"Playing {song}..."
