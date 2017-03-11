$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();
});

function createTable(data, el, cols_filter) {
    $("#" + el).html("<table class='table table-striped table-condensed table-bordered' id='" + el + "-table'></table>");
    var tbl = $('#' + el + '-table');

    $.when($.get(data)).then(function(data){
        var csv_data = $.csv.toArrays(data, {});
        var col_names = "";

        for (head_id = 0; head_id < csv_data[0].length; head_id++) {
            col_names += "<th>" + csv_data[0][head_id] + "</th>";
        }

        tbl.append("<thead><tr>" + col_names + "</tr></thead>");
        tbl.append("<tfoot><tr>" + col_names + "</tr></tfoot>");
        tbl.append("<tbody></tbody>");

        for (row_id = 1; row_id < csv_data.length; row_id++) {
            var row_html = "<tr>";

            for (col_id = 0; col_id < csv_data[row_id].length; col_id++) {
                row_html += "<td>" + csv_data[row_id][col_id] + "</td>";
            }

            row_html += "</tr>";

            $('#' + el + '-table tbody').append(row_html);
        }

        tbl.DataTable({
            paging: false,
            initComplete: function() {
                this.api().columns().every(function() {
                    var column = this;
                    var columnIdx = this.index();
                    if (cols_filter.indexOf(columnIdx) != -1) {
                        var select = $('<br /><select><option value=""></option></select>')
                            .appendTo($(column.footer()).empty())
                            .on('change', function () {
                                if (this.value.length) {
                                    var val = $.fn.dataTable.util.escapeRegex($(this).val());

                                    column
                                        .search(val ? '^' + val + '$' : '', true, false)
                                        .draw();
                                }
                            });

                        column.data().unique().sort().each(function (d, j) {
                            if (d.length && d != '-' && d != undefined) {
                                select.append('<option value="' + d + '">' + d + '</option>');
                            }
                        });
                    } else {
                        $(column.footer()).empty();
                    }
                });
            }
        });

        $('#search').keyup(function() {
            tbl.DataTable().search(this.value).draw();
        });

        $('button[type=reset]').click(function() {
            tbl.DataTable().search('').draw();
            $('#search').focus();
        });
    });
}

// Google Analytics
if (window.location.hostname == 'localhost') {
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
    ga('create', 'UA-93496143-1', 'auto');
    ga('send', 'pageview');
}