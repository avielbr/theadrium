# classes acting as containers for various HTML locator "tags"


class Name:
    CALC2_H          = 'B00006'  # name
    CALC2_T          = 'B00007'  # name
    DIFEQ_H          = 'B00008'  # name
    DIFEQ_T          = 'B00009'  # name
    PHYS2_H          = 'B00011'  # name
    PHYS2_T          = 'B00012'  # name


class ID:
    USERFIELD        = 'R1C1'
    PASSFIELD        = 'password-field'
    LOGIN            = 'loginbtn'
    SEMESTERS        = 'select2-R1C2-container'
    LINES            = 'select2-myTable0_length-80-container'


class CSS:
    COURSESITES      = "div.wrapper:nth-child(6) div.header nav.navbar.navbar-default.mega-menu div.container:nth-child(2) div.col-md-11 div.collapse.navbar-collapse.navbar-responsive-collapse.Menu90 ul.nav.navbar-nav li.dropdown:nth-child(2) > a.dropdown-toggle.menu-item-has-children.DDLocal"
    ENTERCOURSESITES = "div.wrapper:nth-child(6) div.header nav.navbar.navbar-default.mega-menu div.container:nth-child(2) div.col-md-11 div.collapse.navbar-collapse.navbar-responsive-collapse.Menu90 ul.nav.navbar-nav li.dropdown:nth-child(2) ul.dropdown-menu li:nth-child(1) > a:nth-child(1)"
    NEXTPAGE         = "div.wrapper:nth-child(6) div.container.content div.row div.col-md-12 div.panel.panel-grey.margin-bottom-40.table-responsive:nth-child(5) div.dataTables_wrapper.form-inline.dt-bootstrap.no-footer div.row:nth-child(3) div.col-sm-7 div.dataTables_paginate.paging_simple_numbers ul.pagination li.paginate_button.next:nth-child(4) > a:nth-child(1)"
    GOTOZOOMS_CSS    = "div.wrapper:nth-child(5) div.container.content div.row div.col-md-12 div.col-md-2.dir-rtl:nth-child(11) ul.list-group.sidebar-nav-v2.panel-grey.margin-bottom-40.dir-rtl:nth-child(1) li.list-group-item.menu_item:nth-child(8) a:nth-child(2) > span:nth-child(1)"
    LINESFIELD_CSS   = "body:nth-child(2) span.select2-container.select2-container--default.select2-container--open:nth-child(8) span.select2-dropdown.select2-dropdown--below span.select2-search.select2-search--dropdown > input.select2-search__field"

class XPath:
    GOTOZOOMS        = "//li[@id='btitle_course_blockonlineteacher']//a"
    NEXTPAGE         = "//a[contains(text(),'2')]"