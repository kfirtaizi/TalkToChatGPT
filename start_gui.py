import tkinter as tk
import configparser
from tkinter import font

from modules import gtpy


# Make it so that multiple calls dont crash it
def start_program():
    # Update the config file with the values selected on the Scale widgets and the value of the Checkbutton
    config["voice_input"]["wakeword"] = str(voice_input_wakeword_entry.get())
    config["voice_output"]["gender"] = str(voice_output_gender_var.get())
    config["voice_output"]["rate"] = str(voice_output_rate_scale.get())
    config["voice_output"]["volume"] = str(voice_output_volume_scale.get())
    config["chrome"]["profile_name"] = str(chrome_profile_name_entry.get())

    # Save the config file if the Save Configuration checkbox is selected
    if save_configuration_var.get() == 1:
        with open("configuration/gui_fields.ini", "w") as config_file:
            config.write(config_file)

    # Save to actual configuration file for the program
    with open("configuration/config.ini", "w") as config_file:
        config.write(config_file)

    gtpy.start()


def reset_configuration():
    # Reset the values in the config file to the default values
    config.read("configuration/gui_fields_default.ini")

    # Update the values in the GUI to the default values
    voice_input_wakeword_entry.delete(0, "end")
    voice_input_wakeword_entry.insert(0, config["voice_input"]["wakeword"])
    voice_output_gender_var.set(config["voice_output"]["gender"])
    voice_output_rate_scale.set(config["voice_output"]["rate"])
    voice_output_volume_scale.set(config["voice_output"]["volume"])
    chrome_profile_name_entry.delete(0, "end")
    chrome_profile_name_entry.insert(0, config["chrome"]["profile_name"])


if __name__ == '__main__':
    # Load the config file
    config = configparser.ConfigParser()
    config.read("configuration/gui_fields.ini")

    # Create the main window
    window = tk.Tk()
    window.title("TalkToChatGPT")

    start_button = tk.Button(text="Start", command=start_program, width=20, bg="#00ab72",
                             font=("Arial", 16, "bold"))
    start_button.pack(padx=10, pady=10)

    # Create the Save Configuration checkbox and Reset Configuration button
    save_configuration_var = tk.IntVar(value=1)
    save_configuration_checkbox = tk.Checkbutton(text="Save Configuration", variable=save_configuration_var)
    save_configuration_checkbox.pack(padx=10, pady=10)

    voice_input_section = tk.LabelFrame(master=window, text="Voice Input", font=("Arial", 12, "bold"))
    voice_input_section.pack(padx=10, pady=10)

    voice_input_wakeword_label = tk.Label(master=voice_input_section, text="Wakeword:")
    voice_input_wakeword_label.pack(side="left")
    voice_input_wakeword_label2 = tk.Label(master=voice_input_section, text="(OK)", state="disabled")
    voice_input_wakeword_label2.pack(side="left")

    voice_input_wakeword_entry = tk.Entry(master=voice_input_section)
    voice_input_wakeword_entry.pack(side="left")

    # Insert the value of config['voice_input']['wakeword'] into the text field
    voice_input_wakeword_entry.insert(0, config["voice_input"]["wakeword"])

    # Set the state of the text field to 'normal' to allow the user to type in and edit its content
    voice_input_wakeword_entry.config(state="normal")

    voice_output_section = tk.LabelFrame(master=window, text="Voice Output", font=("Arial", 12, "bold"))
    voice_output_section.pack(padx=10, pady=10)

    voice_output_gender_label = tk.Label(master=voice_output_section, text="Gender:")
    voice_output_gender_label.pack(side="left")

    voice_output_gender_var = tk.StringVar(master=voice_output_section)

    voice_output_gender_var.set(config["voice_output"]["gender"])

    voice_output_gender_optionmenu = tk.OptionMenu(voice_output_section, voice_output_gender_var, "male", "female")
    voice_output_gender_optionmenu.pack(side="left")

    voice_output_rate_label = tk.Label(master=voice_output_section, text="Rate:")
    voice_output_rate_label.pack(side="left")

    voice_output_rate_scale = tk.Scale(master=voice_output_section, from_=0, to=400, orient="horizontal")
    voice_output_rate_scale.pack(side="left")

    voice_output_rate_scale.set(config["voice_output"]["rate"])

    voice_output_volume_label = tk.Label(master=voice_output_section, text="Volume:")
    voice_output_volume_label.pack(side="left")

    voice_output_volume_scale = tk.Scale(master=voice_output_section, from_=0.0, to=1.0, orient="horizontal",
                                         resolution=0.1)
    voice_output_volume_scale.pack(side="left")

    voice_output_volume_scale.set(config["voice_output"]["volume"])

    chrome_section = tk.LabelFrame(master=window, text="Chrome", font=("Arial", 12, "bold"))
    chrome_section.pack(padx=10, pady=10)

    chrome_profile_name_label = tk.Label(master=chrome_section, text="Profile Name:")
    chrome_profile_name_label.pack(side="left")

    chrome_profile_name_entry = tk.Entry(master=chrome_section)
    chrome_profile_name_entry.pack(side="left")

    reset_configuration_button = tk.Button(text="Reset Configuration", command=reset_configuration, width=15)
    reset_configuration_button.pack(padx=10, pady=10)

    chrome_profile_name_entry.insert(0, config["chrome"]["profile_name"])

    window.mainloop()
