$(document).ready(function () {
  let sel_group = $("#select_group");
  let sel_test = $("#select_test");
  let set_questions = new Map();

  $("#LoginButton").on("click", function () {
    get_groups();
  });

  $("#SignUpButton").on("click", function () {
    get_groups();
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
    // const url = `api/tasks/?status=${sel_status.val()}`;
    // console.log(url);
    // table.ajax.url(url).load();
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
    console.log("вошла");
    get_question();
  });

  function get_question() {
    console.log("вошла1");
    $("#input_text").val("");
    $.ajax({
      type: "GET",
      url: "api/questions/?test=" + sel_test.val(),
      success: function (response) {
        for (i = 0; i < response.length; i++) {
          set_questions.set(response[i].id, response[i].question);
        }
        console.log("вошла2");
        console.log({ set_questions });
      },
    });
  }

  function get_question() {
    console.log("вошла1");
    $("#input_text").val("");
    $.ajax({
      type: "GET",
      url: "api/questions/?test=" + sel_test.val(),
      success: function (response) {
        for (i = 0; i < response.length; i++) {
          set_questions.set(response[i].number, response[i].question);
        }
        console.log({ set_questions });
        console.log(set_questions.get(1));

        let myarray = new Map();
        let new_myarray = new Map();

        array = [10, 20, 5, 200, 100];
        console.log(array.sort((a, b) => a - b));
        myarray.set(10, 1);
        myarray.set(5, 100);
        myarray.set(20, 50);
        console.log(myarray);
        console.log(Array.from(myarray.keys()).sort());
        Array.from(myarray.keys())
          .sort((a, b) => a - b)
          .forEach(function (key) {
            new_myarray.set(key, myarray.get(key));
          });
        // myarray.sort((a, b) => a - b);
        console.log(new_myarray);

        $("#label-question").html(`Вопрос 1:`);
        $("#input_super").val(set_questions.get(1));
        console.log("TEXT");
        console.log($("#input_super").val());
        get_answers(1);
      },
    });
  }

  function get_answers(question_id) {
    $("#answer_container").empty();
    $("#input_text").val("");
    $.ajax({
      type: "GET",
      url: "api/answers/?question=" + question_id,
      success: function (response) {
        console.log(response);
        for (i = 0; i < response.length; i++) {
          console.log(response[i]);
          console.log(response[i].id);
          console.log(response[i].name);
          $("#answer_container").append(
            `<label><input type="checkbox" id="${response[i].id}" />&#160&#160${response[i].name}</label><p></p>`
          );
        }
      },
    });
  }

  // console.log("***Table***");
  // const url = "api/tests/";
  // console.log(url);
  // let table = $("#SP_Table").DataTable({
  //   ajax: {
  //     url: url,
  //     dataSrc: "",
  //   },
  //   columns: [
  //     { data: "id", visible: false },
  //     { data: "status" },
  //     { data: "start_date" },
  //     { data: "stop_date" },
  //     { data: "message" },
  //     { data: "phones" },
  //     { data: "clients", visible: false },
  //   ],
  //   DisplayLength: 10,
  //   processing: true,
  //   lengthMenu: [
  //     [10, 15, 20, -1],
  //     [10, 15, 20, "Все"],
  //   ],
  //   createdRow: function (row, data) {
  //     if (data.status) {
  //       $("td", row).eq(0).html("Ожидание");
  //     } else {
  //       $("td", row).eq(0).html("Завершена");
  //     }
  //   },
  // });
});
