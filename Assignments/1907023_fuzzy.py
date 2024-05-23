#Fuzzy Light Controll
# Roll : 1907023

def fuzzy_light_duration_controller(time, occupancy):
    def membership_time(time):
        if time < 0 or time > 24:
            return {"Early": 0, "Midday": 0, "Evening": 0}
        elif 0 <= time < 4:
            return {"Early": 1, "Midday": 0, "Evening": 0}
        elif 4 <= time <= 6:
            return {"Early": (6 - time) / 2, "Midday": (time - 4) / 2, "Evening": 0}
        elif 6 < time <= 10:
            return {"Early": 0, "Midday": 1, "Evening": 0}
        elif 10 < time <= 12:
            return {"Early": 0, "Midday": (12 - time) / 2, "Evening": (time - 10) / 2}
        elif 12 < time <= 24:
            return {"Early": 0, "Midday": 0, "Evening": 1}

    def membership_occupancy(occupancy):
        if occupancy < 0 or occupancy > 1:
            return {"Low": 0, "Medium": 0, "High": 0}
        elif 0 <= occupancy <= 0.2:
            return {"Low": 1, "Medium": 0, "High": 0}
        elif 0.2 < occupancy <= 0.4:
            return {"Low": (0.4 - occupancy) / 0.2, "Medium": (occupancy - 0.2) / 0.2, "High": 0}
        elif 0.4 < occupancy <= 0.6:
            return {"Low": 0, "Medium": 1, "High": 0}
        elif 0.6 < occupancy < 0.8:
            return {"Low": 0, "Medium": (0.8 - occupancy) / 0.2, "High": (occupancy - 0.6) / 0.2}
        elif 0.8 <= occupancy < 1:
            return {"Low": 0, "Medium": 0, "High": 1}

    def rule_evaluation(time_mf, occupancy_mf):
        r1 = max(time_mf["Early"], occupancy_mf["Low"])
        r2 = min(time_mf["Midday"], occupancy_mf["Low"])
        res1 = max(r1, r2)
        r3 = min(time_mf["Midday"], occupancy_mf["Medium"])
        r4 = max(time_mf["Evening"], occupancy_mf["Medium"])
        res2 = max(r3, r4)
        res3 = time_mf["Evening"]
        return res1, res2, res3

    def defuzzification(short, medium, long):
        numerator = (0 + 10) * short + (20) * medium + (30 + 40 + 50 + 60) * long
        denominator = 2 * short + medium + 4 * long
        return numerator / denominator

    fuzzy_time = membership_time(time)
    fuzzy_occupancy = membership_occupancy(occupancy)

    short, medium, long = rule_evaluation(fuzzy_time, fuzzy_occupancy)

    fuzzified_assessment = defuzzification(short, medium, long)
    return fuzzified_assessment

sample_input1 = 5
sample_input2 = 0.3

output = fuzzy_light_duration_controller(sample_input1, sample_input2)
print("Fuzzified Assessment is:", output)
