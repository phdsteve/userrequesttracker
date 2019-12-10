#!/usr/bin/python3
import os
import request
import tkinter
import tkinter.filedialog as filedialog
import user


class Application:
    def __init__(self):
        # Build a list that will hold request objects, an int to used when
        # we want to select a particular request, and a variable that will
        # point to our selected Member once chosen.
        self.__requests = []
        self.__users = []
        self.__admins = []
        self.__selected_index = -1
        self.__selected_request = None

        self.__window = tkinter.Tk()
        self.__window.title('User Request Management System')

        # Create four StringVar objects to be bound to the Entry widgets
        self.__name = tkinter.StringVar()

        frame = tkinter.Frame(self.__window)
        self.__load_button = tkinter.Button(frame, text='Load Data File', anchor=tkinter.W, command=self.load_data)
        self.__load_button.pack(side='left')
        self.__save_button = tkinter.Button(frame, text='Save Data File', anchor=tkinter.W, command=self.save_data)
        self.__save_button.pack(side='left')
        frame.pack()

        # Build a Frame consisting of a Label and Entry widget for each field
        self.build_input_frame('Name: ', self.__name)

        # Build a new Frame and add button for new request
        frame = tkinter.Frame(self.__window)
        self.__add_button = tkinter.Button(frame, text='Add Request', anchor=tkinter.W, command=self.add_request)
        self.__add_button.pack(side='left')
        frame.pack()

        # Now, we will use a Listbox widget to display the requests
        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text='User Requests')
        self.__request_list = tkinter.Listbox(frame, width=120, selectmode=tkinter.SINGLE)
        # .bind is a special method that lets us connect a method in our
        # Application class definition with the user's action of clicking on
        # a row in our Listbox
        self.__request_list.bind('<<ListboxSelect>>', self.select_request)
        label.pack()
        self.__request_list.pack()
        frame.pack()

    def build_input_frame(self, label, text_variable):
        """Build the top frames of the window for being able to enter data."""
        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text=label, width=15, anchor=tkinter.W)
        entry = tkinter.Entry(frame, textvariable=text_variable, width=30)
        label.pack(side='left')
        entry.pack(side='right')
        frame.pack()

    def load_data(self):
        members_file = filedialog.askopenfile(initialdir=os.getcwd(), title="Open file",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        try:
            for person in members_file:
                c = user.User(person[:-1])
                self.__requests.append(c)
                self.__request_list.insert(tkinter.END, str(c))
        except TypeError:
            pass

        try:
            members_file.close()
        except AttributeError:
            pass

        self.after_selected_operation()

    def save_data(self):
        members_file = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save file",
                                                    filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        output_file = open(members_file, 'w')
        for person in self.__requests:
            output_file.write('{}\n'.format(person.get_name()))

        try:
            output_file.close()
        except AttributeError and FileNotFoundError:
            pass

        self.after_selected_operation()

    def add_request(self):
        """Get the values from the bound variables and create a new Member."""
        if self.__name.get() != '':
            c = user.User(self.__name.get())
            self.__requests.append(c)

            # Add this Member's __str__ output to the listbox
            self.__request_list.insert(tkinter.END, str(c))

        self.after_selected_operation()

    def select_request(self, event):
        """Get the Member at the index selected, and set the Entry fields
           with its values."""
        # Get the current selection from the Listbox. curselection() returns
        # a tuple and we want the first item
        # Get the current selection from the Listbox. curselection() returns
        # a tuple and we want the first item
        current_selection = self.__request_list.curselection()
        if current_selection:
            self.__selected_index = current_selection[0]

            # Grab the Member object from self.__members at that index
            self.__selected_request = self.__requests[self.__selected_index]

            # Use it's values to set the StringVars
            self.__name.set(self.__selected_request.get_name())

            # Make sure the Save button is enabled
            self.__match_button.config(state=tkinter.NORMAL)
            self.__delete_button.config(state=tkinter.NORMAL)

    def delete_member(self):
        """Remove the Member at the index selected then set the Entry fields
           to empty values."""
        if 0 <= self.__selected_index < len(self.__requests):
            del self.__requests[self.__selected_index]
            self.__request_list.delete(self.__selected_index)

            # Call the method to deselect the item, clear Entry fields, and
            # disable buttons.
            self.after_selected_operation()

    def after_selected_operation(self):
        """Clear the selected index, member, and disable buttons."""
        self.__selected_index = -1
        self.__selected_request = None

        self.__name.set('')

        # Make sure the Save and Delete buttons are disabled
        self.__delete_button.config(state=tkinter.DISABLED)

    @staticmethod
    def start():
        """This method starts our GUI application."""
        tkinter.mainloop()


def main():
    app = Application()
    app.start()


main()
