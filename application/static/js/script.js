$(document).ready(function () {
  let sel_group = $("#select_group");
  let sel_test = $("#select_test");
  let set_questions = new Map();
  let set_answers = new Map();
  let set_ans = new Map();
  let number_ques = 0;
  let number_suq = 0;

  let sort_set_questions = new Map();
  let ques_numbers = [];

  $("#input_number_questions").val("");
  $("#input_success_questions").val("");
  $("#input_persent").val("");

  $("#LoginButton").on("click", function () {
    get_groups();
    $("#input_number_questions").val("");
    $("#input_success_questions").val("");
    $("#input_persent").val("");
  });

  $("#SignUpButton").on("click", function () {
    get_groups();
    $("#input_number_questions").val("");
    $("#input_success_questions").val("");
    $("#input_persent").val("");
  });

  get_groups();

  function get_groups() {
    sel_group.empty();
    $.ajax({
      type: "GET",
      url: "api/groups/",
      success: function (response) {
        for (i = 0; i < response.length; i++) {
          sel_group.append(
            `<option value="${response[i].id}">${response[i].name}</option>`
          );
        }
        get_tests();
      },
    });
  }

  sel_group.change(function () {
    get_tests();
  });

  function get_tests() {
    sel_test.empty();
    $.ajax({
      type: "GET",
      url: "api/tests/?group=" + sel_group.val(),
      success: function (response) {
        for (i = 0; i < response.length; i++) {
          sel_test.append(
            `<option value="${response[i].id}">${response[i].name}</option>`
          );
        }
      },
    });
  }

  $("#StartTestButton").on("click", function () {
    $("#test-title").html($("#select_test option:selected").text());
    $("#TestModal").fadeIn();
    get_questions();
    $("#input_number_questions").val("");
    $("#input_success_questions").val("");
    $("#input_persent").val("");
  });

  function get_questions() {
    number_ques = 0;
    number_suq = 0;
    ques_numbers = [];
    set_questions.clear();
    $("#input_text").val("");
    $.ajax({
      type: "GET",
      url: "api/questions/?test=" + sel_test.val(),
      success: function (response) {
        for (i = 0; i < response.length; i++) {
          set_questions.set(response[i].number, {
            id: response[i].id,
            question: response[i].question,
          });
        }
        Array.from(set_questions.keys())
          .sort((a, b) => a - b)
          .forEach(function (key) {
            sort_set_questions.set(key, set_questions.get(key));
          });
        console.log(sort_set_questions);
        ques_numbers = Array.from(sort_set_questions.keys());
        number_ques = ques_numbers.length;
        next_question();
      },
    });
  }

  function next_question() {
    if (ques_numbers.length != 0) {
      const first_number = ques_numbers.shift();
      $("#label-question").html(`Вопрос ${first_number}:`);
      $("#input_super").val(sort_set_questions.get(first_number).question);
      get_answers(sort_set_questions.get(first_number).id);
      sort_set_questions.delete(first_number);
    } else {
      alert("Тест окончен. Смотрите результаты в таблице.");
      $("#TestModal").fadeOut();
      // console.log("РЕЗУЛЬТАТЫ");
      // console.log(number_ques);
      // console.log(number_suq);
      // console.log(Math.round((number_suq / number_ques) * 100));
      $("#input_number_questions").val(number_ques);
      $("#input_success_questions").val(number_suq);
      $("#input_persent").val(
        String(Math.round((number_suq / number_ques) * 100)) + "%"
      );
    }
  }

  function get_answers(question_id) {
    $("#answer_container").empty();
    $("#input_text").val("");
    set_answers.clear();
    set_ans.clear();
    $.ajax({
      type: "GET",
      url: "api/answers/?question=" + question_id,
      success: function (response) {
        for (i = 0; i < response.length; i++) {
          set_answers.set(response[i].id, response[i].correct);
          set_ans.set(response[i].id, [response[i].name, response[i].correct]);
          $("#answer_container").append(
            `<label id="lbl${response[i].id}"><input type="checkbox" id="ch${response[i].id}" />&#160&#160${response[i].name}</label><p></p>`
          );
        }
      },
    });
  }

  function check_answer() {
    for (let entry of set_answers) {
      console.log($(`#ch${entry}`).is(":checked"), entry[1]);
      if ($(`#ch${entry[0]}`).is(":checked") != entry[1]) {
        return false;
      }
    }
    number_suq++;
  }

  $("#TestOkButton").on("click", function () {
    console.log("NEXT");
    check_answer();
    next_question();
  });

  $("#RightAnswerButton").on("click", function () {
    console.log(set_ans);
    for (let entry of set_ans) {
      const ch = document.querySelector(`#lbl${entry[0]}`);
      const parent = ch.parentNode;
      parent.removeChild(ch);
    }
    for (let entry of set_ans) {
      if (entry[1][1] == true) {
        $("#answer_container").append(
          `<label id="lbl${entry[0]}"><input type="checkbox" checked="true" id="ch${entry[0]}" />&#160&#160${entry[1][0]}</label><p></p>`
        );
      } else {
        $("#answer_container").append(
          `<label id="lbl${entry[0]}"><input type="checkbox" id="ch${entry[0]}" />&#160&#160${entry[1][0]}</label><p></p>`
        );
      }
    }
  });

  $("#NewTestButton").on("click", function () {
    $.ajax({
      type: "GET",
      url: "api/questions/new_test/",
      success: function (response) {
        console.log(response);
      },
    });
  });
});
