function createTable(data, el) {
    $("#" + el).html("<table class='table table-striped table-condensed table-bordered' id='" + el + "-table'></table>");
    var tbl = $('#' + el + '-table');

    $.when($.get(data)).then(function(data){
        var csv_data = $.csv.toArrays(data, {});
        var custom_formatting = [];
        var table_head = "<thead><tr>";

        for (head_id = 0; head_id < csv_data[0].length; head_id++) {
            table_head += "<th>" + csv_data[0][head_id] + "</th>";
        }

        table_head += "</tr></thead>";

        tbl.append(table_head);
        tbl.append("<tbody></tbody>");

        for (row_id = 1; row_id < csv_data.length; row_id++) {
            var row_html = "<tr>";

            for (col_id = 0; col_id < csv_data[row_id].length; col_id++) {
                row_html += "<td>" + csv_data[row_id][col_id] + "</td>";
            }

            row_html += "</tr>";

            $('#' + el + '-table tbody').append(row_html);
        }

        tbl.DataTable({ "paging": false });

        $('#search').keyup(function() {
            tbl.DataTable().search(this.value).draw();
        });

        $('button[type=reset]').click(function() {
            tbl.DataTable().search('').draw();
        });
    });
}