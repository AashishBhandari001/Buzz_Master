document.addEventListener("DOMContentLoaded", () => {
  // Fetch quiz data from the backend
  fetch("admin/student/question/")
    .then((response) => response.json())
    .then((data) => {
      const { questions, options } = data;
      displayQuiz(questions, options);
    })
    .catch((error) => console.error("Error fetching quiz data:", error));
});
