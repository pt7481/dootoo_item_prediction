# 🔍 Exploratory Analysis: Task Completion Prediction

## Project Summary

Explores the predictive value of task text semantic similarities to topic names (e.g. "Chore", "Work", "Excercise").  

**This exercise is mainly academic as the available dataset is too small to be able to draw credible inferences (332 samples post filtering).**

### What I Did

* Downloaded latest encrypted task completion data from Thoughtswork [dootoo productivity app](https://dootoo.app) as input source.
* Engineered features describing the following:
    * Creation time components (`hour_of_day`, `day_of_week`)
    * Task hierarchy (`has_parent`)
    * Task Publicity (`is_public`)
    * Topic Similarities (`similarity_Eating`, `similarity_Exercise`, etc).
* Obtained task text similarities to topics using Hugging Face [Sentence Transformers all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model Inference Provider API.
* Protected user privacy by decrypting task text and never displaying task text in clear-text.
* Trained hyperparameter-tuned XGBoost Classifier with engineered feature set to predict task completion.
* Evaluated model on Precision and Recall with closer focus on recall of minority completion task `is_done==1`.

### What I Learned

* Initial precision and recall scores (both scored >50% predicting training data) indicate creation time, hierarchy, and publicity *may* have some predictive value towards task completion (not drawing any inferences due to low sample size).
* Ablation testing of topic similarity features showed may not be predictive of task completion given their inclusion reduced recall to below 20%.
* SHAP analysis revealed the following tentative insights:
  * The day of the week the task was created had the most predictive power relative to all other features
    * Creating a task earlier in the week (starting from Monday) increased its probability of completion.
  * Making a task public increased its probability of completion.
  * Making a task a subtask increased its probability of completion.

### Next Steps

* Consider evaluating predictive value of task creation time, hierarchy, publicity, and topic similarity once able to obtain 100+ tasks from 100+ users.
* Explore viability of training model per user (or user group) to account for different user behaviors or goals.
