from receiver import Receive


class ProcessData:

    def getAmbulanceData(self):
        # TODO: Implement listener

        # When history stack has two elements
        # Pop elements
        first = Receive.history.get()  # Remove from history stack
        last = Receive.history.get()
        Receive.history.put(last)  # Put last element back to the history stack

        long = Receive.history[long]
        lat =
