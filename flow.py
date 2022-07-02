from metaflow import FlowSpec, conda, step


class Flow(FlowSpec):
    @conda(libraries={"pytorch::pytorch": "1.12.0"}, python="3.10.5")
    @step
    def start(self):
        import torch
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    Flow()
