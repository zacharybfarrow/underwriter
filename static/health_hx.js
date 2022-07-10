let heart_attack_q = document.getElementById("heart_attack")
let stroke_q = document.getElementById("stroke")
let tia_q = document.getElementById("tia")
let cardio_surgery_q = document.getElementById("cardio_surgery")
let diabetes_q = document.getElementById("diabetes")
let insulin_q = document.getElementById("insulin")

// Event handler function to toggle hidden status of each duratioin select field
function switch_hidden(event, label_id, field_id) {
    let label = document.getElementById(label_id)
    let field = document.getElementById(field_id)
    if ((label.hidden == true) && (field.hidden == true)) {
        label.hidden = false
        field.hidden = false
    }
    else {
        label.hidden = true
        field.hidden = true
    }
}

// Event listeners
heart_attack_q.addEventListener("click", (event) => switch_hidden(event, "heart_attack_dur_lbl", "heart_attack_dur"))
stroke_q.addEventListener("click", (event) => switch_hidden(event, "stroke_dur_lbl", "stroke_dur"))
tia_q.addEventListener("click", (event) => switch_hidden(event, "tia_dur_lbl", "tia_dur"))
cardio_surgery_q.addEventListener("click", (event) => switch_hidden(event, "cardio_surgery_dur_lbl", "cardio_surgery_dur"))
diabetes_q.addEventListener("click", (event) => switch_hidden(event, "insulin_lbl", "insulin"))
diabetes_q.addEventListener("click", (event) => switch_hidden(event, "complications_lbl", "complications"))
insulin_q.addEventListener("click", (event) => switch_hidden(event, "insulin_dur_lbl", "insulin_dur"))
