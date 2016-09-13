class ListTable(list):
    """
    Overridden list class which takes a 2-dimensional list of
    the form [[1,2,3],[4,5,6]], and renders an HTML Table in
    IPython Notebook.
    """

    def _repr_html_(self):
        html = ["<table>"]
        for row in self:
            html.append("<tr>")

            for col in row:
                html.append("<td>{0}</td>".format(col))

            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)


def print_knapsack_table(d, rows, m, v):
    from IPython.core.display import display, HTML
    n = len(d) - 1
    M = len(d[0]) - 1
    table = ListTable()
    table.append(["", "", "", "0 <= j <= M kg"])
    table.append(["i", "mass", "value", [x for x in range(M+1)]])
    for i in range(rows+1):
        if i == 0:
            table.append([i, '-', '-', d[i]])
        else:
            table.append([i, str(m[i-1]) + "kg", "$" + str(v[i-1]), d[i]])
    display(HTML("<h3>i=%s</h3>" % rows))
    display(table)
    display(HTML('<hr>'))
