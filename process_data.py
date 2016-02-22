from receiver import Receiver


class ProcessData:

    def get_ambulance_data(self):
        """Return the two last data sets from Receiver

        Returns
        -------
        Array containing first and last
        first : dict containing GPS data, timestamp, speed
        last : dict containing GPS data, timestamp, speed
        """
        # TODO: Implement listener

        # When history stack has two elements
        # Pop elements
        first = Receive.history.get()  # Remove from history stack
        last = Receive.history.get()
        Receive.history.put(last)  # Put last element back to the history stack

        return [first, last]
