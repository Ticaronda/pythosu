from configparser import ConfigParser
from queue import Queue

class osu():
    def __init__(self, file: str) -> None:
        self.file = file
        self.general: dict = {}
        self.difficulty: dict = {}
        self.timing_points: Queue = Queue()
        self.hit_objects: Queue = Queue()
        self.combo: Queue = Queue()
        self.song: str = ''

        self.open_osu()

    def open_osu(self) -> None:
        config = ConfigParser(comment_prefixes=("//", "osu file format"), allow_no_value=True)
        config.read(self.file)

        # GENERAL
        self.general["song"] = config["General"]["AudioFilename"]
        self.general["lead_in"] = int(config["General"]["AudioLeadIn"])
        self.general["preview_time"] = int(config["General"]["PreviewTime"])
        self.general["count_down"] = int(config["General"]["Countdown"])
        self.general["sample_set"] = config["General"]["SampleSet"]
        self.general["stack_leniency"] = float(config["General"]["StackLeniency"])
        self.general["mode"] = int(config["General"]["Mode"])

        # DIFFICULTY
        self.difficulty["hp_drain"] = float(config["Difficulty"]["HPDrainRate"])
        self.difficulty["circle_size"] = float(config["Difficulty"]["CircleSize"])
        self.difficulty["overall_difficulty"] = float(config["Difficulty"]["OverallDifficulty"])
        self.difficulty["approach_rate"] = float(config["Difficulty"]["ApproachRate"])
        self.difficulty["slider_multiplier"] = float(config["Difficulty"]["SliderMultiplier"])
        self.difficulty["slider_tick_rate"] = float(config["Difficulty"]["SliderTickRate"])

        # COMBO COLOURS
        for combo in config["Colours"]:
            self.combo.put(tuple(int(x) for x in config["Colours"][combo].split(',')))

        # TIMING POINTS
        for timing_point in config["TimingPoints"]:
            self.timing_points.put(TimingPoint(timing_point))

        # HIT OBJECTS
        for hit_object in config["HitObjects"]:
            self.hit_objects.put(HitObject(hit_object))

class TimingPoint():
    def __init__(self, input: str) -> None:
        self.input = input
        self.unpack()

    def unpack(self) -> None:
        input_array: list = self.input.split(',')
        self.time: int = int(input_array[0])
        self.beat_length: float = float(input_array[1]) # If inherited, negative inverse slider velocity multiplier
        self.meter: int = int(input_array[2]) # If inherited, ignore, AKA time signature
        self.sample_set: int = int(input_array[3])
        self.sample_index: int = int(input_array[4])
        self.volume: int = int(input_array[5])
        self.uninherited: bool = bool(int(input_array[6]))

class HitObject():
    def __init__(self, input: str) -> None:
        self.input = input
        self.unpack()

    def unpack(self) -> None:
        input_array: list = self.input.split(',')
        self.x: int = int(input_array[0])
        self.y: int = int(input_array[1])
        self.time: int = int(input_array[2])
        self.type: int = int(input_array[3])
        self.hit_sound: int = int(input_array[4])
        self.extras: list = input_array[5:]

if __name__ == "__main__":
    # open_osz("Reol - No title.osz")
    no_title = osu("maps/Reol - No title/Reol - No title (VINXIS) [toybot's Insane].osu")
