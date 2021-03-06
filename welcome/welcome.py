"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

@XBlock.needs("i18n")
class WelcomeXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    course_objectives = String(display_name="Course Objectives", name="Course Objectives", multiline_editor='html', help="List of course objectives to be done", resettable_editor=False, default="Course Objectives",
                scope=Scope.content)
                
    teacher_comments = String(display_name="Extra Comments", name="Extra Comments", multiline_editor='html', help="Extra description from the course runner", resettable_editor=False, default="Extra Comments",
                score=Scope.content)
    
    
    editable_fields = ('course_objectives', 'teacher_comments')
    
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the WelcomeXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/welcome.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/welcome.css"))
        frag.add_javascript(self.resource_string("static/js/src/welcome.js"))
        frag.initialize_js('WelcomeXBlock')
        return frag

    
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("WelcomeXBlock",
             """<vertical_demo>
                <welcome/>
                </vertical_demo>
             """),
        ]
