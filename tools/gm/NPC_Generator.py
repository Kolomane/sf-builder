import random, json, re

job_pos = ["Janitorial Engineer (inside)","Janitorial Engineer (outside)","Bread Engineer","Maintenance Technical Engineer","Executive Assistant","Assistant to the Executive Assistant","Financial Advisor","Ambassador","Security Architecture Guard","Lube Technician","Human Resources","Alien Resources","Lead Data Engineer","Client Services Manager","Stratosphere Engineer","Mesosphere Manager","Apoapsis & Periapsis Security","CONFIDENTIAL","Picker Packer Personnel","Drone Delivery Driver","Intelligence Analyst - Advanced Investigation Labs","Physical Security Guard","Advanced Maintenance Technician"]
job_prepend = ["Senior","Junior","Vice President","Principal","Lead"]
races = ["Shobhad","Ikeshti","Dromada","Contemplative","Screedreep","Pahtra","Orc","Halfling","Gnome","Dwarf","Ysoki","Vesk","Shirren","Human","Android","Kasatha","Elf","Lashunta","Raxilite","Draelik","Formian"]

def main():
    with open("tools\gm\Castrovel_NPCs.json", "r") as file:
        json_data = json.load(file)
    json_result = {}

    # for job in job_pos:
    #     json_result[job] = {}

    for single_race in races:
        json_result[single_race] = {}

    for entry in range(len(json_data)):
        # temp_job_pos = json_data[entry]['Job Position']
        # for job in job_pos:
            # temp_reg = re.compile(f".*?{re.escape(job)}.*")
            # the_match = re.match(temp_reg,temp_job_pos)
            # if the_match:
            #     json_result[job].update({f"{json_data[entry]['Name']}": json_data[entry]})
        temp_race = json_data[entry]['Race']
        for single_race in races:
            if temp_race == single_race:
                json_result[single_race].update({f"{json_data[entry]['Name']}": json_data[entry]})
    
    with open('tools/gm/NPCs_by_race.json', 'w', encoding='utf-8') as f:
        json.dump(json_result, f, ensure_ascii=False, indent=4)
    # print(json.dumps(json_result))
main()