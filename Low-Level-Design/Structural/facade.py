# Complex subsystem classes
class AudioSystem:
    def __init__(self):
        self.volume = 50
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Audio system powered on")

    def turn_off(self):
        self.is_on = False
        print("Audio system powered off")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Audio volume set to {volume}")

    def set_surround_sound(self):
        print("Surround sound activated")


class VideoProjector:
    def __init__(self):
        self.is_on = False
        self.input_source = None

    def turn_on(self):
        self.is_on = True
        print("Projector warming up...")
        print("Projector ready")

    def turn_off(self):
        print("Projector cooling down...")
        self.is_on = False
        print("Projector powered off")

    def set_input(self, source):
        self.input_source = source
        print(f"Projector input set to {source}")


class StreamingDevice:
    def __init__(self):
        self.is_connected = False
        self.current_app = None

    def connect(self):
        self.is_connected = True
        print("Streaming device connected to network")

    def disconnect(self):
        self.is_connected = False
        print("Streaming device disconnected")

    def launch_app(self, app_name):
        if self.is_connected:
            self.current_app = app_name
            print(f"Launching {app_name}")
        else:
            print("Cannot launch app - not connected")


class LightingSystem:
    def __init__(self):
        self.brightness = 100

    def dim_lights(self, level):
        self.brightness = level
        print(f"Lights dimmed to {level}%")

    def turn_off_lights(self):
        self.brightness = 0
        print("All lights turned off")

    def turn_on_lights(self):
        self.brightness = 100
        print("All lights turned on")


class ClimateControl:
    def __init__(self):
        self.temperature = 72

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"Temperature set to {temp}°F")


# Facade class
class HomeTheaterFacade:
    def __init__(self):
        self.audio = AudioSystem()
        self.projector = VideoProjector()
        self.streaming = StreamingDevice()
        self.lights = LightingSystem()
        self.climate = ClimateControl()

    def watch_movie(self, movie_service="Netflix"):
        """Simplified interface for watching a movie"""
        print("=== Starting Movie Night ===")

        # Turn on and configure audio
        self.audio.turn_on()
        self.audio.set_volume(75)
        self.audio.set_surround_sound()

        # Set up projector
        self.projector.turn_on()
        self.projector.set_input("HDMI1")

        # Configure streaming
        self.streaming.connect()
        self.streaming.launch_app(movie_service)

        # Set ambiance
        self.lights.dim_lights(20)
        self.climate.set_temperature(68)

        print("=== Ready to enjoy your movie! ===")

    def end_movie(self):
        """Simplified interface for ending movie session"""
        print("=== Ending Movie Night ===")

        # Shutdown streaming
        self.streaming.disconnect()

        # Turn off projector
        self.projector.turn_off()

        # Reset audio
        self.audio.set_volume(50)
        self.audio.turn_off()

        # Restore lighting and climate
        self.lights.turn_on_lights()
        self.climate.set_temperature(72)

        print("=== Movie night ended ===")

    def listen_to_music(self):
        """Simplified interface for music listening"""
        print("=== Starting Music Session ===")

        self.audio.turn_on()
        self.audio.set_volume(60)
        self.streaming.connect()
        self.streaming.launch_app("Spotify")
        self.lights.dim_lights(50)

        print("=== Enjoy your music! ===")

    def gaming_mode(self):
        """Simplified interface for gaming"""
        print("=== Starting Gaming Session ===")

        self.projector.turn_on()
        self.projector.set_input("HDMI2")  # Gaming console
        self.audio.turn_on()
        self.audio.set_volume(80)
        self.lights.dim_lights(30)
        self.climate.set_temperature(70)  # Cooler for intense gaming

        print("=== Game on! ===")


# Usage
theater = HomeTheaterFacade()

# Simple movie watching - no need to know about all the subsystems
theater.watch_movie("Disney+")
print("\n" + "=" * 50 + "\n")
theater.end_movie()

print("\n" + "=" * 50 + "\n")

# Easy gaming setup
theater.gaming_mode()
