import streamlit as st
import pandas as pd
import altair as alt

st.markdown(
     """
     <style>
     body {
         font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
                      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
         background-color: #121212;
         color: #F5F5F5;
         margin: 0;
         padding: 0;
     }
     .container {
         max-width: 900px;
         margin: auto;
         padding: 20px;
     }
     h1, h2, h3, h4 {
         text-align: center;
         font-weight: 600;
         color: #FFFFFF;
         margin-bottom: 0.5em;
     }
     h1 {
         font-size: 2.4rem;
         margin-top: 0.5em;
     }
     h2 {
         font-size: 2rem;
         margin-top: 1.5em;
     }
     h3 {
         font-size: 1.5rem;
         margin-top: 1em;
     }
     table {
         width: 100%;
         border-collapse: collapse;
         margin: 20px 0;
         font-size: 1rem;
         background-color: #1E1E1E;
         color: #F5F5F5;
     }
     table, th, td {
         border: 1px solid #333333;
     }
     th, td {
         padding: 12px;
         text-align: left;
     }
     tr:nth-child(even) {
         background-color: #2A2A2A;
     }
     tr:hover {
         background-color: #333333;
     }
     .scrollable-table {
         overflow-x: auto;
     }
     .stButton button {
         background-color: #FF9800;
         color: #FFFFFF;
         border: none;
         padding: 0.6em 1em;
         font-weight: 600;
         border-radius: 5px;
         cursor: pointer;
     }
     .stButton button:hover {
         background-color: #e68900;
         color: #000000;
     }
     .stSelectbox, .stNumberInput, .stRadio, .stTextInput {
         color: #000000;
     }
     </style>
     """,
     unsafe_allow_html=True
 )

def calculate_macros(weight, height, age, gender, activity_level, goal):
     if gender == 'Male':
         bmr = 10 * weight + 6.25 * height - 5 * age + 5
     else:
         bmr = 10 * weight + 6.25 * height - 5 * age - 161
 
     activity_multipliers = {
         "Sedentary (little or no exercise)": 1.2,
         "Lightly active (1-3 days/week)": 1.375,
         "Moderately active (3-5 days/week)": 1.55,
         "Very active (6-7 days/week)": 1.725,
         "Super active (twice/day intense training)": 1.9
     }
     tdee = bmr * activity_multipliers[activity_level]
 
     if goal == "Lose Weight":
         tdee -= 500
     elif goal == "Gain Muscle":
         tdee += 500
 
     protein = (tdee * 0.3) / 4
     fats = (tdee * 0.25) / 9
     carbs = (tdee * 0.45) / 4
     return tdee, protein, fats, carbs
 
def df_to_html_table(df):
     return df.to_html(index=False, escape=False)
 

nico_routine = pd.DataFrame({
     "Day": [
         "Day 1: Chest + Triceps + Abs",
         "Day 2: Back + Biceps + Abs",
         "Day 3: Legs + Calves + Abs",
         "Day 4: Shoulders + Abs",
         "Day 5: Chest + Biceps + Abs"
     ],
     "Warm-Up": [
         "5 min of light cardio + dynamic stretching + perform each exercise movement without weight (ascending pyramid approach)",
         "5 min of light cardio + dynamic stretching + no-weight rehearsal of the day’s exercises",
         "5 min of light cardio + dynamic stretching + no-weight rehearsal (bodyweight squats, calf raises, etc.)",
         "5 min of light cardio + dynamic stretching + no-weight rehearsal (light overhead press, etc.)",
         "5 min of light cardio + dynamic stretching + no-weight rehearsal (light bench press, light curls, etc.)"
     ],
     "Exercises": [
         "<b>Chest (Big):</b><br>• Barbell Bench Press – 4 sets (pyramid)<br>• Incline Dumbbell Press – 3 sets (8–12 reps)"
         "<br><br><b>Triceps (Small):</b><br>• Skullcrushers (EZ-Bar or Dumbbells) – 3 sets (8–12 reps)<br>• Cable Triceps Pushdown – 3 sets (8–12 reps)"
         "<br><br><b>Abs:</b><br>• Plank – 3 sets (30–45 s)<br>• Crunches – 3 sets (15 reps)",
 
         "<b>Back (Big):</b><br>• Deadlifts or Barbell Row – 4 sets (pyramid)<br>• Lat Pulldown or Pull-Ups – 3 sets (8–12 reps)"
         "<br><br><b>Biceps (Small):</b><br>• Barbell Curls – 3 sets (8–12 reps)<br>• Hammer Curls – 3 sets (8–12 reps)"
         "<br><br><b>Abs:</b><br>• Hanging Leg Raises – 3 sets (10–12 reps)<br>• Bicycle Crunches – 3 sets (20 total)",
 
         "<b>Legs (Big):</b><br>• Squats – 4 sets (pyramid)<br>• Leg Press – 3 sets (8–12 reps)<br>• Walking Lunges (or Split Squats) – 3 sets (~8–12 each leg)"
         "<br><br><b>Calves (Small):</b><br>• Standing Calf Raises – 3 sets (12–15 reps)<br>• Seated Calf Raises – 3 sets (12–15 reps)"
         "<br><br><b>Abs:</b><br>• Reverse Crunches – 3 sets (12 reps)<br>• Russian Twists – 3 sets (20 total)",
 
         "<b>Shoulders (Big):</b><br>• Overhead Press (Barbell or Dumbbells) – 4 sets (pyramid)<br>• Lateral Raises – 3 sets (10–12 reps)<br>• Rear Delt Flyes or Face Pulls – 3 sets (10–12 reps)"
         "<br><br><b>Abs (Small):</b><br>• Ab Wheel Rollouts – 3 sets (10–12 reps)<br>• Side Plank – 3 sets (30–45 s each side)",
 
         "<b>Chest (Big):</b><br>• Dumbbell Bench Press – 4 sets (pyramid)<br>• Cable Flyes or Dips – 3 sets (8–12 reps)"
         "<br><br><b>Biceps (Small):</b><br>• EZ-Bar Curls – 3 sets (8–12 reps)<br>• Concentration Curls – 3 sets (8–12 reps)"
         "<br><br><b>Abs:</b><br>• Leg Raises (on bench or hanging) – 3 sets (10–12 reps)<br>• Side Plank – 3 sets (30–45 s each side)"
     ],
     "Cool Down": [
         "5–10 min of static stretching focusing on chest, triceps, shoulders, and lower back",
         "5–10 min of static stretching focusing on the entire back, biceps, forearms, and lower back",
         "5–10 min of static stretching focusing on quads, hamstrings, glutes, calves, and lower back",
         "5–10 min of static stretching focusing on shoulders, traps/neck, core muscles, and lower back",
         "5–10 min of static stretching focusing on chest, biceps, shoulders, and lower back"
     ]
 })

nico_tips = """
 <ul>
 <li><strong>Time Management:</strong> Aim for ~1 hour per session (5–10 min Warm-Up, ~40–45 min Exercises, 5–10 min Cool Down).</li>
 <li><strong>Progressive Overload:</strong> Increase weight gradually while maintaining proper form.</li>
 <li><strong>Abs Frequency:</strong> Abs every day; keep each session short. Swap in other core moves if desired.</li>
 <li><strong>Rest Days:</strong> Incorporate rest or active recovery (light cardio, mobility) as needed.</li>
 </ul>
 """

kiara_routine = pd.DataFrame({
     "Day": [
         "Day 1",
         "Day 2",
         "Day 3"
     ],
     "Warm-Up": [
         "<ul><li>5–10 min of light dynamic stretching</li><li>Practice each exercise with zero weight before adding load (pyramidal)</li></ul>",
         "<ul><li>5–10 min of light dynamic stretching</li><li>Practice each exercise with zero weight before adding load (pyramidal)</li></ul>",
         "<ul><li>5–10 min of light dynamic stretching</li><li>Practice each exercise with zero weight before adding load (pyramidal)</li></ul>"
     ],
     "Exercises": [
         "<b>HIIT Treadmill (15 min):</b><br>• 1 min walking<br>• 4 min jogging<br>• 10 min high intensity<br><br>"
         "<b>Smith Machine Squats</b> (4 sets: 12,10,8,6)<br>"
         "<b>Hip Thrust</b> (4 sets: 12,10,8,6)<br>"
         "<b>Lying Leg Curls</b> (3 sets: 12,10,8)<br>"
         "<b>Standing Calf Raises</b> (3 sets: 12,10,8)<br>"
         "<b>Abs:</b> Leg Raises (3×15), Plank (3×30 sec)",
 
         "<b>HIIT Treadmill (15 min):</b><br>• 1 min walking<br>• 4 min jogging<br>• 10 min high intensity<br><br>"
         "<b>Dumbbell Romanian Deadlift</b> (4 sets: 12,10,8,6)<br>"
         "<b>Glute Machine</b> (3 sets: 12,10,8)<br>"
         "<b>Seated Leg Curls</b> (3 sets: 12,10,8)<br>"
         "<b>Seated Calf Raises</b> (3 sets: 12,10,8)<br>"
         "<b>Abs:</b> Crunches (3×15), Side Plank (3×30 sec/side)",
 
         "<b>HIIT Treadmill (15 min):</b><br>• 1 min walking<br>• 4 min jogging<br>• 10 min high intensity<br><br>"
         "<b>Smith Machine Sumo Squats</b> (4 sets: 12,10,8,6)<br>"
         "<b>Hip Thrust</b> (4 sets: 12,10,8,6)<br>"
         "<b>Dumbbell Leg Curls</b> (3 sets: 12,10,8)<br>"
         "<b>Dumbbell Calf Raises</b> (3 sets: 12,10,8)<br>"
         "<b>Abs:</b> Bicycle Crunches (3×15/side), Plank w/Knee Tucks (3×10/side)"
     ],
     "Cool Down": [
         "5–10 min static stretching: quads, hamstrings, glutes, calves, lower back",
         "5–10 min static stretching: quads, hamstrings, glutes, calves, lower back",
         "5–10 min static stretching: quads, hamstrings, glutes, calves, lower back"
     ]
 })

kiara_tips = """
 <ul>
 <li><strong>Zero-Weight Warm-Up:</strong> Empty bar or light dumbbells to refine technique.</li>
 <li><strong>Pyramidal Progression:</strong> Increase weight each set while lowering reps (12,10,8,6).</li>
 <li><strong>Core & Stability:</strong> Engage abs during squats, hip thrusts, deadlifts.</li>
 <li><strong>Recovery:</strong> At least 1 rest/low-impact day weekly (e.g., walk, yoga).</li>
 </ul>
 """

if "progress_data" not in st.session_state:
     st.session_state.progress_data = {
         "Nico": [],
         "Kiara": []
     }
 

st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<h1>🏋️ Personalized Workout & Nutrition App</h1>", unsafe_allow_html=True)
 
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Choose a section", ["Workout Routines", "Calorie & Macro Calculator", "Gym Progress"])
 

if app_mode == "Workout Routines":
     name = st.selectbox("Select Your Name:", ["Select", "Nico", "Kiara"])
     if name == "Nico":
         st.markdown("<h2>💪 Nico's 5-Day Routine</h2>", unsafe_allow_html=True)
         st.markdown("<h3>Warm-Up</h3>", unsafe_allow_html=True)
         st.markdown(
             f"<div class='scrollable-table'>{df_to_html_table(nico_routine[['Day','Warm-Up']] )}</div>",
             unsafe_allow_html=True
         )
         st.markdown("<h3>Exercises</h3>", unsafe_allow_html=True)
         st.markdown(
             f"<div class='scrollable-table'>{df_to_html_table(nico_routine[['Day','Exercises']] )}</div>",
             unsafe_allow_html=True
         )
         st.markdown("<h3>Cool Down</h3>", unsafe_allow_html=True)
         st.markdown(
             f"<div class='scrollable-table'>{df_to_html_table(nico_routine[['Day','Cool Down']] )}</div>",
             unsafe_allow_html=True
         )
         st.markdown("<h3>Additional Tips</h3>", unsafe_allow_html=True)
         st.markdown(nico_tips, unsafe_allow_html=True)
 
     elif name == "Kiara":
         st.markdown("<h2>🏋️‍♀️ Kiara's 3-Day Routine</h2>", unsafe_allow_html=True)
         st.markdown("<h3>Warm-Up</h3>", unsafe_allow_html=True)
         st.markdown(
             f"<div class='scrollable-table'>{df_to_html_table(kiara_routine[['Day','Warm-Up']] )}</div>",
             unsafe_allow_html=True
         )
         st.markdown("<h3>Exercises</h3>", unsafe_allow_html=True)
         st.markdown(
             f"<div class='scrollable-table'>{df_to_html_table(kiara_routine[['Day','Exercises']] )}</div>",
             unsafe_allow_html=True
         )
         st.markdown("<h3>Cool Down</h3>", unsafe_allow_html=True)
         st.markdown(
             f"<div class='scrollable-table'>{df_to_html_table(kiara_routine[['Day','Cool Down']] )}</div>",
             unsafe_allow_html=True
         )
         st.markdown("<h3>Tips</h3>", unsafe_allow_html=True)
         st.markdown(kiara_tips, unsafe_allow_html=True)
 

elif app_mode == "Calorie & Macro Calculator":
     st.markdown("<h2>🍽️ Calculate Your Daily Caloric & Macro Needs</h2>", unsafe_allow_html=True)
     st.markdown(
         """
         <p>
         This calculator uses the <strong>Mifflin–St. Jeor Equation</strong> to estimate
         Basal Metabolic Rate (BMR). We then factor in your <strong>Activity Level</strong>
         for Total Daily Energy Expenditure (TDEE), and adjust based on your goal:
         <strong>Lose Weight</strong>, <strong>Gain Muscle</strong>, or <strong>Maintain</strong>.
         </p>
         <p>
         We divide daily calories into <strong>Protein</strong> (30%), <strong>Fats</strong> (25%),
         <strong>Carbs</strong> (45%). Actual macro ratios can vary by individual preference.
         </p>
         <p>
         For detailed food tracking, consider apps like <strong>MyFitnessPal</strong> or
         <strong>Fitia</strong> to log daily intake.
         </p>
         """,
         unsafe_allow_html=True
     )
 
     weight = st.number_input("Enter your weight (kg):", min_value=30.0, max_value=200.0, step=0.1)
     height = st.number_input("Enter your height (cm):", min_value=120.0, max_value=250.0, step=0.1)
     age = st.number_input("Enter your age:", min_value=10, max_value=100, step=1)
     gender = st.selectbox("Select your gender:", ["Male", "Female"])
     activity_level = st.selectbox(
         "Select your activity level:",
         [
             "Sedentary (little or no exercise)",
             "Lightly active (1-3 days/week)",
             "Moderately active (3-5 days/week)",
             "Very active (6-7 days/week)",
             "Super active (twice/day intense training)"
         ]
     )
     goal = st.selectbox("What is your goal?", ["Maintain Weight", "Lose Weight", "Gain Muscle"])
 
     if st.button("Calculate Macros"):
         tdee, protein, fats, carbs = calculate_macros(weight, height, age, gender, activity_level, goal)
         st.markdown("<h3>🔥 Your Daily Caloric & Macro Breakdown:</h3>", unsafe_allow_html=True)
         st.markdown(f"<p><strong>Total Daily Calories:</strong> {tdee:.0f} kcal</p>", unsafe_allow_html=True)
         st.markdown(f"<p><strong>Protein:</strong> {protein:.0f} g/day</p>", unsafe_allow_html=True)
         st.markdown(f"<p><strong>Fats:</strong> {fats:.0f} g/day</p>", unsafe_allow_html=True)
         st.markdown(f"<p><strong>Carbs:</strong> {carbs:.0f} g/day</p>", unsafe_allow_html=True)
 

elif app_mode == "Gym Progress":
     st.markdown("<h2>📈 Gym Progress</h2>", unsafe_allow_html=True)
     st.markdown(
         """
         <p>
         Track <strong>Weight</strong> & <strong>Body Fat %</strong> to monitor body composition changes.
         If you can’t measure some weeks, use visual references (below) to estimate body fat:
         </p>
         """,
         unsafe_allow_html=True
     )
     st.image(
         "https://tptspersonaltraining.co.uk/wp-content/uploads/2017/04/body-fat-percentage-men-women.jpg",
         caption="Body Fat Percentage Reference",
         width=600
     )
 
     selected_user = st.selectbox("Select Your Name:", ["Select", "Nico", "Kiara"])
     if selected_user != "Select":
         st.markdown("<h3>Record Your Current Stats</h3>", unsafe_allow_html=True)
         new_weight = st.number_input("Weight (kg):", min_value=30.0, max_value=200.0, step=0.1)
         new_fat = st.number_input("Body Fat (%):", min_value=0.0, max_value=100.0, step=0.1)
 
         if st.button("Add Progress Entry"):
             st.session_state.progress_data[selected_user].append({
                 "Weight (kg)": new_weight,
                 "Fat (%)": new_fat
             })
             st.success("Progress entry added!")
 
         user_data = st.session_state.progress_data[selected_user]
         if len(user_data) > 0:
             st.markdown(f"<h3>{selected_user}'s Progress History</h3>", unsafe_allow_html=True)
             df_progress = pd.DataFrame(user_data)
 
            
             df_progress["Estimated Muscle Mass (kg)"] = (
                 df_progress["Weight (kg)"] * (1 - df_progress["Fat (%)"] / 100.0)
             ) * 0.45
 
             st.dataframe(df_progress)
             df_progress["Measurement #"] = df_progress.index + 1
 
             # Weight Chart
             st.markdown(f"<h4>{selected_user}'s Weight Over Time (kg)</h4>", unsafe_allow_html=True)
             chart_weight = (
                 alt.Chart(df_progress)
                 .mark_line(point=True)
                 .encode(
                     x="Measurement #:O",
                     y="Weight (kg):Q",
                     tooltip=["Measurement #", "Weight (kg)"]
                 )
                 .interactive()
                 .properties(width="container", height=300)
             )
             st.altair_chart(chart_weight, use_container_width=True)
 
             # Body Fat Chart
             st.markdown(f"<h4>{selected_user}'s Body Fat Over Time (%)</h4>", unsafe_allow_html=True)
             chart_fat = (
                 alt.Chart(df_progress)
                 .mark_line(point=True)
                 .encode(
                     x="Measurement #:O",
                     y="Fat (%):Q",
                     tooltip=["Measurement #", "Fat (%)"]
                 )
                 .interactive()
                 .properties(width="container", height=300)
             )
             st.altair_chart(chart_fat, use_container_width=True)
 
             st.markdown(f"<h4>Estimated Muscle Mass Over Time (kg)</h4>", unsafe_allow_html=True)
             chart_muscle = (
                 alt.Chart(df_progress)
                 .mark_line(point=True)
                 .encode(
                     x="Measurement #:O",
                     y="Estimated Muscle Mass (kg):Q",
                     tooltip=["Measurement #", "Estimated Muscle Mass (kg)"]
                 )
                 .interactive()
                 .properties(width="container", height=300)
             )
             st.altair_chart(chart_muscle, use_container_width=True)
 
             st.markdown(
                 "<p><em>Note:</em> This muscle mass calculation is a rough estimate; "
                 "actual muscle mass varies by genetics, training, etc.</p>",
                 unsafe_allow_html=True
             )
         else:
             st.info("No progress data yet. Add your first entry above!")
 
st.markdown("</div>", unsafe_allow_html=True)
 

st.markdown("<h3 style='text-align: center;'>Stay Consistent & Enjoy Your Workouts! 💪🔥</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Developed by Mateo M. with ☕</h4>", unsafe_allow_html=True)
 



