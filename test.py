import re

text = """
        <div class="et_pb_module et_pb_toggle et_pb_toggle_open  et_pb_accordion_item_0">


        				<h5 class="et_pb_toggle_title">CHAPTER 1: REAL NUMBERS &amp; ALGEBRA</h5>
        				<div class="et_pb_toggle_content clearfix">

        <h5>Unit 1: Positives and Negatives</h5>
        <p><a href="/how_to/positives_and_negatives/addition_and_subtraction/">Addition and Subtraction</a> <a href="/how_to/positives_and_negatives/multiplication_and_division/">Multiplication and Division</a></p>
        <h5>Unit 2: Order of Operations / Evaluation / Absolute Value</h5>
        <p><a href="/how_to/order_of_operations_-_evaluation/order_of_operations/">Order of Operations</a> <a href="/how_to/order_of_operations_-_evaluation/evaluation/">Evaluation</a> <a href="/how_to/absolute_value/integers/">Absolute Value</a></p>
        <h5>Unit 3: Fractions</h5>
        <p><a href="/how_to/fractions/addition_and_subtraction/">Addition and Subtraction</a> <a href="/how_to/fractions/multiplication_and_division/">Multiplication and Division</a></p>
        <h5>Unit 4: Simplifying with Variables</h5>
        <p><a href="/how_to/algebraic_concepts/field_properties/">Field Properties</a> <a href="/how_to/simplifying_with_variables/combining_like_terms/">Combining Like Terms</a> <a href="/how_to/simplifying_with_variables/distributive_property/">Distributive Property</a> <a href="/how_to/simplifying_with_variables/distributive_-_like_terms/">Distributive / Like Terms</a>
        				</div> <!-- .et_pb_toggle_content -->
        			</div> <!-- .et_pb_toggle -->
        			<div class="et_pb_module et_pb_toggle et_pb_toggle_close  et_pb_accordion_item_1">


        				<h5 class="et_pb_toggle_title">CHAPTER 2: LINEAR EQUATIONS &amp; INEQUALITIES</h5>
        				<div class="et_pb_toggle_content clearfix">

        <h5>Unit 1: Beginning Equations</h5>
        <p><a href="/how_to/beginning_equations/two-step_equations/">Two-Step Equations</a> <a href="/how_to/intermediate_equations/equations_with_fractions/">Equations with Fractions</a> <a href="/how_to/intermediate_equations/equations_involving_distributive/">Equations Involving Distributive</a></p>
        <h5>Unit 2: Advanced Equations</h5>
        <p><a href="/how_to/advanced_equations/variable_on_both_sides/">Variable on Both Sides</a> <a href="/how_to/advanced_equations/variable_on_both_sides_-_fractions/">Variable on Both Sides / Fractions</a> <a href="/how_to/advanced_equations/variable_on_both_sides_-_distributive/">Variable on Both Sides / Distributive</a> <a href="/how_to/equations_with_decimals/integer_solutions/">Equations with Decimals</a></p>
        <h5>Unit 3: Formulas</h5>
        <p><a href="/how_to/fractions_and_formulas/beginning_formulas/">Beginning Formulas</a> <a href="/how_to/formulas/advanced_formulas/">Advanced Formulas</a></p>
        <h5>Unit 4: Beginning Word Problems</h5>
        <p><a href="/how_to/one-step_equations/writing_and_solving_equations/">Writing and Solving Equations</a> <a href="/how_to/multi-step_equations/modeling_two-step_equations/">Modeling Two-Step Equations</a> <a href="/how_to/introductory_word_problems/consecutive_integer_problems/">Consecutive Integer Problems</a> <a href="/how_to/introductory_word_problems/geometry_problems/">Geometry Problems</a></p>
        <h5>Unit 5: Advanced Word Problems</h5>
        <p><a href="/how_to/age_-_value_-_interest_problems/age_problems/">Age Problems</a> <a href="/how_to/age_-_value_-_interest_problems/value_problems/">Value Problems</a> <a href="/how_to/age_-_value_-_interest_problems/interest_problems/">Interest Problems</a> <a href="/how_to/mixture_-_motion_problems/mixture_problems/">Mixture Problems</a> <a href="/how_to/motion_problems/introductory_motion_problems/">Introductory Motion Problems</a> <a href="/how_to/mixture_-_motion_problems/advanced_motion_problems/">Advanced Motion Problems</a></p>
        <h5>Unit 6: Inequalities</h5>
        <p><a href="/how_to/inequalities/solving_and_graphing_inequalities/">Solving and Graphing Inequalities</a> <a href="/how_to/inequalities/combined_inequalities/">Combined Inequalities</a> <a href="/how_to/inequalities/advanced_inequality_problems/">Advanced Inequality Problems</a></p>
        <h5>Unit 7: Absolute Value</h5>
        <p><a href="/how_to/absolute_value/absolute_value_equations/">Absolute Value Equations</a> <a href="/how_to/absolute_value/absolute_value_inequalities/">Absolute Value Inequalities</a>
        				</div> <!-- .et_pb_toggle_content -->
        			</div> <!-- .et_pb_toggle --><div class="et_pb_module et_pb_toggle et_pb_toggle_close  et_pb_accordion_item_2">


        				<h5 class="et_pb_toggle_title">CHAPTER 3: GRAPHS, LINEAR EQUATIONS, &amp; FUNCTIONS</h5>
        				<div class="et_pb_toggle_content clearfix">

        <h5>Unit 1: Graphs</h5>
        <p><a href="/how_to/functions/the_coordinate_system/">The Coordinate System</a> <a href="/how_to/graphing/graphing_lines/">Graphing Lines</a> <a href="/how_to/graphing/the_intercept_method/">The Intercept Method</a> <a href="/how_to/graphing/graphing_inequalities_in_two_variables/">Graphing Inequalities in Two Variables</a></p>
        <h5>Unit 2: Slope</h5>
        <p><a href="/how_to/lines_and_slope/using_the_graph_of_a_line_to_find_slope/">Using the Graph of a Line to Find Slope</a> <a href="/how_to/lines_and_slope/using_slope_to_graph_a_line/">Using Slope to Graph a Line</a> <a href="/how_to/coordinates_and_slope/using_coordinates_to_find_slope/">Using Coordinates to Find Slope</a> <a href="/how_to/introduction_to_linear_equations_and_functions/slope_as_a_rate_of_change/">Slope as a Rate of Change</a></p>
        <h5>Unit 3: Slope-Intercept Form</h5>
        <p><a href="/how_to/slope-intercept_form/using_slope-intercept_form_to_graph_a_line/">Using Slope-Intercept Form to Graph a Line</a> <a href="/how_to/slope-intercept_form/converting_to_slope-intercept_form_and_graphing/">Converting to Slope-Intercept Form and Graphing</a> <a href="/how_to/writing_equations_of_lines/using_graphs_and_slope-intercept_form/">Using Graphs and Slope-Intercept Form</a> <a href="/how_to/writing_equations_of_lines/using_tables_and_slope-intercept_form/">Using Tables and Slope-Intercept Form</a></p>
        <h5>Unit 4: Writing Equations of Lines</h5>
        <p><a href="/how_to/writing_equations_of_lines/standard_form/">Standard Form</a> <a href="/how_to/writing_equations_of_lines/the_point-slope_formula/">The Point-Slope Formula</a> <a href="/how_to/writing_equations_of_lines/given_two_points/">Given Two Points</a> <a href="/how_to/writing_equations_of_lines/parallel_and_perpendicular/">Parallel and Perpendicular</a></p>
        <h5>Unit 5: Functions</h5>
        <p><a href="/how_to/functions/definition_of_a_function/">Definition of a Function</a> <a href="/how_to/functions/function_and_arrow_notation/">Function and Arrow Notation</a> <a href="/how_to/writing_equations_of_lines/direct_variation/">Direct Variation</a> <a href="/how_to/writing_equations_of_lines/applications_of_direct_variation_and_linear_functions/">Applications of Direct Variation and Linear Functions</a>
        				</div> <!-- .et_pb_toggle_content -->
        			</div> <!-- .et_pb_toggle -->
"""

result = re.findall(r'<div class="et_pb_module et_pb_toggle et_pb_toggle_[a-z]*  et_pb_accordion_item_[0-9]">(.*?)</div> <!-- .et_pb_toggle -->', text, re.DOTALL)
# result = re.findall(r'<div class="et_pb_module et_pb_toggle et_pb_toggle_close  et_pb_accordion_item_1">(.*?)</div> <!-- .et_pb_toggle -->', text)

print(result)
