import edge_tts
import asyncio

class TTS:
    def __init__(self):
        self.out_audiofile = "media/outaudios/out_audio.wav"  # Fixed variable name
    
    async def text_to_audio(self, text: str):  # Renamed to reflect it saves WAV
        communicate = edge_tts.Communicate(text, "en-US-RogerNeural")
        await communicate.save(self.out_audiofile)  # Fixed filename reference
        return self.out_audiofile  # Return the correct file path

# Run the TTS function properly
if __name__ == "__main__":
    tts = TTS()
    asyncio.run(tts.text_to_audio(" Hi, I'm Mahendra from Andhra Pradesh. I have a Diploma and B.Tech in Computer Science and Engineering, focusing on AI Agents, automation, and generative AI. I've developed projects like AI interview systems and job matching platforms. I love coding and solving AI problems, and I enjoy movies, cricket, and gaming in my free time."))  # Use asyncio.run() to call async function
