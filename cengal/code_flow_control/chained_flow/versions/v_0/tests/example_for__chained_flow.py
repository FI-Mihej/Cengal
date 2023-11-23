#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cengal.code_flow_control.chained_flow.versions.v_1.chained_flow import *
from random import randint

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


def random_int(a, b):
    if a < -20:
        raise ChainLinkFailed('Too small!')
    result = randint(a, b)
    return result


def int_div(a, b):
    result = a / b
    return result


def int_square(value):
    result = value * value
    return result


def user_input(is_ok__context_holder=None):
    if is_ok__context_holder:
        uinput = input('Enter something:')
        str_len = len(uinput)
        if str_len < 10:
            raise ChainLinkFailed('Too short!')
        result = uinput
        is_ok__context_holder.push_result(True, uinput)
        return result


def print_result(result_block_id, is_ok__context_holder=None):
    if is_ok__context_holder:
        print('RESULT FOR "{}":'.format(is_ok__context_holder._context_holder_id),
              is_ok__context_holder.read_block_result_link(result_block_id).result)
    else:
        print('ERROR IN "{}": Can\'t compute!'.format(is_ok__context_holder._context_holder_id))
        print(str(is_ok__context_holder))


@link__function__simple
def random_int_d(a, b):
    if a < -20:
        raise ChainLinkFailed('Too small!')
    result = randint(a, b)
    return result


@link__function__simple
def int_div_d(a, b):
    result = a / b
    return result


@link__function__simple
def int_square_d(value):
    result = value * value
    return result


@link__function
def user_input_d(is_ok__context_holder=None):
    if is_ok__context_holder:
        uinput = input('Enter something:')
        str_len = len(uinput)
        if str_len < 10:
            raise ChainLinkFailed('Too short!')
        result = uinput
        is_ok__context_holder.push_result(True, uinput)
        return result


@chain_reader__function
def print_result_d(result_block_id, is_ok__context_holder=None):
    if is_ok__context_holder:
        print('RESULT:', is_ok__context_holder.read_block_result_link(result_block_id).result)
    else:
        print('Error: Can\'t compute!')
        print(str(is_ok__context_holder))


def with_chain_example(raise_exceptions=False):
    """
    Console output:

========================
=== WITH-CHAIN-RAISE-EXCEPTIONS: ===


WITH raise_exceptions:


>> loop iteration #0 START

Ops: ZeroDivisionError

Oh! There are errors in Main Loop! Interesting!

{{CONTEXT_HOLDER_ID(Test Holder): CONTEXT_HOLDER_INFO(Some holder)}:[
(index(0), depth(1), ID(1 str), INFO(None), RESULT((False, ISOK INTERNAL RESULT. EXTERNAL EXCEPTION: <class 'ZeroDivisionError'> division by zero ))),
(index(1), depth(0), ID(main loop), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: BAD HISTORY IMPORT EXCEPTION)))
]}



========================
========================
========================



========================
=== WITH-CHAIN: ===


WITHOUT raise_exceptions:


>> loop iteration #0 START

Ops: ZeroDivisionError
Sum was not computed because of "Did not fit criteria because of "14" in 2 block" in "Sum" block.
Mul: 120.0
GlobalSum of (Mul, Sum, 0): 126.0
GlobalSum2 of (Mul, Sum, 0): 126.0

>> loop iteration #0 END
{{CONTEXT_HOLDER_ID(Test Holder): CONTEXT_HOLDER_INFO(Some holder)}:[
(index(0), depth(0), ID(0), INFO(None), RESULT((True, 6))),
(index(1), depth(0), ID(1 str), INFO(None), RESULT((False, ISOK INTERNAL RESULT. EXTERNAL EXCEPTION: <class 'ZeroDivisionError'> division by zero ))),
(index(2), depth(0), ID(2), INFO(None), RESULT((True, 14))),
(index(3), depth(0), ID(2 str), INFO(None), RESULT((False, ISOK INTERNAL RESULT. EXTERNAL EXCEPTION: <class 'ZeroDivisionError'> division by zero ))),
(index(4), depth(0), ID(Hello), INFO(None), RESULT((True, 20.0))),
(index(5), depth(0), ID(Sum), INFO(None), RESULT((False, Did not fit criteria because of "14" in 2 block))),
(index(6), depth(0), ID(Mul), INFO(None), RESULT((True, 120.0))),
(index(7), depth(0), ID(print1), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(8), depth(0), ID(print2), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(9), depth(0), ID(GlobalSum), INFO(None), RESULT((True, 126.0))),
(index(10), depth(0), ID(GlobalSum2), INFO(None), RESULT((True, 126.0)))
]}


Everything is fine: result fit criteria of current reader block: "ResultType(CriteriaType.forbidden, {'1'})"!


Everything is fine: result fit criteria of current reader block: "ResultType(CriteriaType.forbidden, {'2'})"!


>> loop iteration #1 START

Ops: ZeroDivisionError
Sum was not computed because of "Did not fit criteria because of "14" in 2 block" in "Sum" block.
Mul: 120.0
GlobalSum of (Mul, Sum, 0): 126.0
GlobalSum2 of (Mul, Sum, 0): 126.0

>> loop iteration #1 END
{{CONTEXT_HOLDER_ID(Test Holder): CONTEXT_HOLDER_INFO(Some holder)}:[
(index(0), depth(0), ID(0), INFO(None), RESULT((True, 6))),
(index(1), depth(0), ID(1 str), INFO(None), RESULT((False, ISOK INTERNAL RESULT. EXTERNAL EXCEPTION: <class 'ZeroDivisionError'> division by zero ))),
(index(2), depth(0), ID(2), INFO(None), RESULT((True, 14))),
(index(3), depth(0), ID(2 str), INFO(None), RESULT((True, 54.0))),
(index(4), depth(0), ID(Hello), INFO(None), RESULT((True, 20.0))),
(index(5), depth(0), ID(Sum), INFO(None), RESULT((False, Did not fit criteria because of "14" in 2 block))),
(index(6), depth(0), ID(Mul), INFO(None), RESULT((True, 120.0))),
(index(7), depth(0), ID(print1), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(8), depth(0), ID(print2), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(9), depth(0), ID(GlobalSum), INFO(None), RESULT((True, 126.0))),
(index(10), depth(0), ID(GlobalSum2), INFO(None), RESULT((True, 126.0)))
]}


Everything is fine: result fit criteria of current reader block: "ResultType(CriteriaType.forbidden, {'1'})"!


Everything is NOT fine: did not fit default criteria set in context constructor: "ResultType(CriteriaType.forbidden, {'2'})"!


Oh! There are errors in Main Loop! Interesting!

{{CONTEXT_HOLDER_ID(Test Holder): CONTEXT_HOLDER_INFO(Some holder)}:[
(index(0), depth(1), ID(1 str), INFO(None), RESULT((False, ISOK INTERNAL RESULT. EXTERNAL EXCEPTION: <class 'ZeroDivisionError'> division by zero ))),
(index(1), depth(1), ID(Sum), INFO(None), RESULT((False, Did not fit criteria because of "14" in 2 block))),
(index(2), depth(1), ID(print1), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(3), depth(1), ID(print2), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(4), depth(0), ID(main loop), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: BAD HISTORY IMPORT EXCEPTION)))
]}


========================

    :param raise_exceptions:
    :return:
    """
    if raise_exceptions:
        print()
        print('WITH raise_exceptions:')
        print()
    else:
        print()
        print('WITHOUT raise_exceptions:')
        print()

    function_context = Chain('Test Holder', 'Some holder', ResultType(CriteriaType.optional, set()))

    with link(function_context, 'main loop'):
        if function_context:
            for index in range(10):
                print()
                print('>> loop iteration #{} START'.format(index))
                print()

                context = Chain('Test Holder', 'Some holder', ResultType(CriteriaType.forbidden, {'1 str'}),
                                raise_exceptions=raise_exceptions)

                with link(context, 0, None, ResultType(CriteriaType.any, None)):
                    if context:
                        result = 2 * 3
                        context.push_result(True, result)

                try:
                    with link(context, '1 str', None, ResultType(CriteriaType.any, None)):
                        if context:
                            try:
                                result = 54 / 0  # if raise_exceptions - it will break Main Loop
                                context.push_result(True, result)
                            except ZeroDivisionError:
                                print('Ops: ZeroDivisionError')
                                raise
                except ZeroDivisionError:
                    print('THIS LINE WILL NOT BE EXECUTED!')

                with link(context, 2):
                    if context:
                        result = 14
                        context.push_result(True, result)
                    else:
                        raise ChainLinkFailed('Something went wrong.')

                try:
                    with link(context, '2 str'):
                        if context:
                            result = 54 / index
                            context.push_result(True, result)
                except ZeroDivisionError:
                    print('THIS LINE WILL NOT BE EXECUTED!')

                with link(context, 'Hello', None, ResultType(CriteriaType.needed, set())):
                    if context:
                        result = 100 / 5
                        context.push_result(True, result)

                with link(context, 'Sum', None, ResultType(CriteriaType.forbidden, {0, 2})):
                    if context:
                        result = context.read_block_result_link(0).result + context.read_block_result_link(2).result
                        context.push_result(True, result)
                    else:
                        context.push_result(False, 'Did not fit criteria because of "{}" in 2 block'.format(
                            context.read_block_result_link(2).result))

                with link(context, 'Mul', None, ResultType(CriteriaType.needed, {0, 'Hello'})):
                    if context:
                        result = context.read_block_result_link(0).result * context.read_block_result_link('Hello').result
                        context.push_result(True, result)

                with link(context, 'print1', None, ResultType(CriteriaType.needed, {'Sum'})):
                    if context:
                        print('Sum: {}'.format(context.read_block_result_link('Sum').result))
                    else:
                        print('Sum was not computed because of "{}" in "Sum" block.'.format(
                            context.read_block_result_link('Sum').result
                        ))

                with link(context, 'print2', None, ResultType(CriteriaType.needed, {'Mul'})):
                    if context:
                        print('Mul: {}'.format(context.read_block_result_link('Mul').result))

                with link(context, 'GlobalSum', None, ResultType(CriteriaType.needed, set())):
                    if context:
                        interesting_results = {0, 'Sum', 'Mul'}
                        global_sum = 0
                        for interesting_result in interesting_results:
                            if context.read_block_result_link(interesting_result):
                                global_sum += context.read_block_result_link(interesting_result).result

                        print('GlobalSum of ({}): {}'.format(', '.join(str(x) for x in interesting_results), global_sum))
                        context.push_result(True, global_sum)

                with link(context, 'GlobalSum2'):
                    interesting_results = {0, 'Sum', 'Mul'}
                    global_sum = 0
                    for interesting_result in interesting_results:
                        if context.read_block_result_link(interesting_result):
                            global_sum += context.read_block_result_link(interesting_result).result

                    print('GlobalSum2 of ({}): {}'.format(', '.join(str(x) for x in interesting_results), global_sum))
                    context.push_result(True, global_sum)

                print()
                print('>> loop iteration #{} END'.format(index))
                print(str(context))
                print()

                with chain_reader(context):
                    if context:
                        print()
                        print('Everything is fine: result fit criteria of current reader block: '
                              '"ResultType(CriteriaType.forbidden, {\'1\'})"!')
                        print()
                    else:
                        context.raise_bad_blocks()

                with chain_reader(context, ResultType(CriteriaType.forbidden, {'2 str'})):
                    if context:
                        print()
                        print('Everything is fine: result fit criteria of current reader block: '
                              '"ResultType(CriteriaType.forbidden, {\'2\'})"!')
                        print()
                    else:
                        print()
                        print('Everything is NOT fine: did not fit default criteria set in context constructor: '
                              '"ResultType(CriteriaType.forbidden, {\'2\'})"!')
                        print()
                        context.raise_bad_blocks()

    with chain_reader(function_context):
        if function_context:
            print()
            print('Everything is fine!')
            print()
        else:
            print()
            print('Oh! There are errors in Main Loop! Interesting!')
            print()
            print(str(function_context))
            print()


def func_decorator_chain_example():
    """
    Console output:

========================
=== FUNC-DECORATOR-COMPLICATED-CHAIN: ===

Enter something:Hello
RESULT: 625.0
RESULT: ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: ChainLinkFailed (Too short!)


========================

    :return:
    """
    cont = Chain('Test Holder', 'Some holder', ResultType(CriteriaType.any, None))

    user_input_d(is_ok__context_holder=cont, is_ok__block_id='User Input')

    result_block_id = 'Result'

    # Will fail: -40 < -20.
    int_square_d(
        int_div_d(
            random_int_d(-40, 0, is_ok__context_holder=cont),  # -40 < -20
            random_int_d(3, 4, is_ok__context_holder=cont),
            is_ok__context_holder=cont),
        is_ok__context_holder=cont, is_ok__block_id=result_block_id,
        is_ok__block_results_criteria=ResultType(CriteriaType.not_successful, {result_block_id}),
        is_ok__ignore_block_result_criteria=IgnoreBlockResultCriteriaType.ignore_if_failed)

    # Will be successful.
    int_square_d(
        int_div_d(
            random_int_d(100, 100, is_ok__context_holder=cont),  # 100
            random_int_d(4, 4, is_ok__context_holder=cont), is_ok__context_holder=cont  # 4
        ),  # 25
        is_ok__context_holder=cont,
        is_ok__block_id=result_block_id,
        is_ok__block_results_criteria=ResultType(CriteriaType.not_successful, {result_block_id}),
        is_ok__ignore_block_result_criteria=IgnoreBlockResultCriteriaType.ignore_if_failed
    )  # 625

    # Will fail: 'Result' already successfully computed
    # Also will fail in stand alone mode: division by zero.
    int_1 = random_int_d(-10, 0, is_ok__context_holder=cont)
    int_2 = random_int_d(0, 0, is_ok__context_holder=cont)  # 0 (zero)
    div_res = int_div_d(int_1, int_2, is_ok__context_holder=cont)  # value / 0
    int_square_d(div_res, is_ok__context_holder=cont, is_ok__block_id=result_block_id
                 , is_ok__block_results_criteria=ResultType(CriteriaType.not_successful, {result_block_id})
                 , is_ok__ignore_block_result_criteria=IgnoreBlockResultCriteriaType.ignore_if_failed)

    # Will print "625"
    print_result_d(result_block_id, is_ok__context_holder=cont)

    # Will print user input or error (exception info) with text "Too short!"
    print_result_d('User Input', is_ok__context_holder=cont)


def func_runner_chain_complicated_example():
    """
    Console output:

========================
=== FUNC-RUNNER-COMPLICATED-CHAIN: ===

Enter something:World
RESULT FOR "Test Holder": 625.0
RESULT FOR "Test Holder": ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: ChainLinkFailed (Too short!)


========================

    :return:
    """
    cont = Chain('Test Holder', 'Some holder', ResultType(CriteriaType.any, None))

    cr = ChainUniRunner(globals(), cont, True)  # Simple-Mode - for any functions

    ChainUniRunner(globals(), cont)('User Input').user_input()  # Normal-Mode - for specially prepared functions

    result_block_id = 'Result'

    # Will fail: -40 < -20.
    # Will return None if you'll try to assign final result to the variable
    cr(result_block_id, None, ResultType(CriteriaType.not_successful, {result_block_id}),
       IgnoreBlockResultCriteriaType.ignore_if_failed
       ).int_square(
        cr().int_div(
            cr().random_int(-40, 0),  # -40 < -20
            cr().random_int(3, 4)))

    # Will be successful.
    # Will return 625 if you'll try to assign final result to the variable
    cr(result_block_id,
       block_results_criteria=ResultType(CriteriaType.not_successful, {result_block_id}),
       ignore_block_result_criteria=IgnoreBlockResultCriteriaType.ignore_if_failed
       ).int_square(
        cr().int_div(
            cr().random_int(100, 100),  # 100
            cr().random_int(4, 4)  # 4
        )  # 25
    )  # 625

    # Will fail: 'Result' already successfully computed
    # Also will fail in stand alone mode: division by zero.
    # Will return None if you'll try to assign final result to the variable
    int_1 = cr().random_int(-10, 0)
    int_2 = cr().random_int(0, 0)  # 0 (zero)
    div_res = cr().int_div(int_1, int_2)  # value / 0
    cr(result_block_id,
       block_results_criteria=ResultType(CriteriaType.not_successful, {result_block_id}),
       ignore_block_result_criteria=IgnoreBlockResultCriteriaType.ignore_if_failed
       ).int_square(div_res)

    # Will print "625"
    ChainReaderRunner(globals(), cont)().print_result(result_block_id)

    # Will print user input or error (exception info) with text "Too short!"
    crr = ChainReaderRunner(globals(), cont)
    crr().print_result('User Input')


def func_runner_chain_simple_example():
    """
    Console output:

========================
=== FUNC-RUNNER-SIMPLE-CHAIN: ===

RESULT FOR "Test Holder Number 1": 625.0

ERROR IN "Test Holder Number 2": Can't compute!
{{CONTEXT_HOLDER_ID(Test Holder Number 2): CONTEXT_HOLDER_INFO(Will fail)}:[
(index(0), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: ChainLinkFailed (Too small!)))),
(index(1), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(2), depth(0), ID(<function int_div at 0x000001D1D8A4EEA0>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(3), depth(0), ID(Result), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT)))
]}

ERROR IN "Test Holder Number 3": Can't compute!
{{CONTEXT_HOLDER_ID(Test Holder Number 3): CONTEXT_HOLDER_INFO(Every function should return number >= 0. Will fail.)}:[
(index(0), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((True, 100))),
(index(1), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((False, -3))),
(index(2), depth(0), ID(<function int_div at 0x000001D1D8A4EEA0>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(3), depth(0), ID(Result), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT)))
]}

ERROR IN "Test Holder Number 4": Can't compute!
{{CONTEXT_HOLDER_ID(Test Holder Number 4): CONTEXT_HOLDER_INFO(Every function should return even number. Will fail.)}:[
(index(0), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((True, 100))),
(index(1), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((True, 4))),
(index(2), depth(0), ID(<function int_div at 0x000001D1D8A4EEA0>), INFO(None), RESULT((False, 25.0))),
(index(3), depth(0), ID(Result), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT)))
]}


========================

    :return:
    """
    # ============================
    # TEST 1:
    cont = Chain('Test Holder Number 1', 'Will be successful', ResultType(CriteriaType.optional, set()))
    cr = ChainUniRunner(globals(), cont, True)  # Simple-Mode - for any functions

    # Will be successful.
    # Will return 625 if you'll try to assign final result to the variable
    cr('Result').int_square(
        cr().int_div(
            cr().random_int(100, 100),  # 100
            cr().random_int(4, 4)  # 4
        )  # 25
    )  # 625

    # Will print "625"
    ChainReaderRunner(globals(), cont)().print_result('Result')

    # ============================
    print()

    # ============================
    # TEST 2:
    cont = Chain('Test Holder Number 2', 'Will fail', ResultType(CriteriaType.optional, set()))
    cr = ChainUniRunner(globals(), cont, True)  # Simple-Mode - for any functions

    # Will fail: -40 < -20.
    # Will return None if you'll try to assign final result to the variable
    cr('Result').int_square(  # Will not be computed
        cr().int_div(  # Will not be computed
            cr().random_int(-40, 0),  # -40 < -20. EXCEPTION ChainLinkFailed ("Too small!")
            cr().random_int(3, 4)))  # Will not be computed

    # Will print an error
    ChainReaderRunner(globals(), cont)().print_result('Result')

    # ============================
    print()

    # ============================
    # TEST 3:
    cont = Chain('Test Holder Number 3', 'Every function should return number >= 0. Will fail.',
                 ResultType(CriteriaType.optional, set()))
    cr = ChainUniRunner(globals(), cont, True, lambda result: result >= 0)  # Simple-Mode - for any functions

    # Will fail: random_int(-5, -1) < 0.
    # Will return None if you'll try to assign final result to the variable
    cr('Result').int_square(
        cr().int_div(
            cr().random_int(100, 100),  # 100
            cr().random_int(-5, -1)  # result < 0. Result state is FAIL (push_result(False, ...))
        )  # Will not be computed
    )  # Will not be computed

    # Will print an error
    ChainReaderRunner(globals(), cont)().print_result('Result')

    # ============================
    print()

    # ============================
    # TEST 4:
    cont = Chain('Test Holder Number 4', 'Every function should return even number. Will fail.',
                 ResultType(CriteriaType.optional, set()))
    cr = ChainUniRunner(globals(), cont, True, lambda result: result % 2 == 0)  # Simple-Mode - for any functions

    # Will fail: 25 is odd.
    # Will return None if you'll try to assign final result to the variable
    int_1 = cr().random_int(100, 100)  # 100
    int_2 = cr().random_int(4, 4)  # 4
    div_res = cr().int_div(int_1, int_2)  # 25. Result is odd. Result state is FAIL (push_result(False, 25))
    cr('Result').int_square(div_res)  # Will not be computed

    # Will print an error
    ChainReaderRunner(globals(), cont)().print_result('Result')


def func_call_runner_chain_complicated_example():
    """
    Console output:

========================
=== FUNC-CALL-RUNNER-COMPLICATED-CHAIN: ===

Enter something:Hello World
RESULT FOR "Test Holder": 625.0
RESULT FOR "Test Holder": Hello World


========================

    :return:
    """
    cont = Chain('Test Holder', 'Some holder', ResultType(CriteriaType.any, None))

    cr = ChainUniCallRunner(cont, True)  # Simple-Mode - for any functions

    ChainUniCallRunner(cont)('User Input')(user_input)  # Normal-Mode - for specially prepared functions

    result_block_id = 'Result'

    # Will fail: -40 < -20.
    # Will return None if you'll try to assign final result to the variable
    cr(result_block_id, None, ResultType(CriteriaType.not_successful, {result_block_id}),
       IgnoreBlockResultCriteriaType.ignore_if_failed)(
        int_square,
        cr()(
            int_div,
            cr()(random_int, -40, 0),  # -40 < -20
            cr()(random_int, 3, 4)))

    # Will be successful.
    # Will return 625 if you'll try to assign final result to the variable
    cr(result_block_id,
       block_results_criteria=ResultType(CriteriaType.not_successful, {result_block_id}),
       ignore_block_result_criteria=IgnoreBlockResultCriteriaType.ignore_if_failed)(
        int_square,
        cr()(
            int_div,
            cr()(random_int, 100, 100),  # 100
            cr()(random_int, 4, 4)  # 4
        )  # 25
    )  # 625

    # Will fail: 'Result' already successfully computed
    # Also will fail in stand alone mode: division by zero.
    # Will return None if you'll try to assign final result to the variable
    int_1 = cr()(random_int, -10, 0)
    int_2 = cr()(random_int, 0, 0)  # 0 (zero)
    div_res = cr()(int_div, int_1, int_2)  # value / 0
    cr(result_block_id,
       block_results_criteria=ResultType(CriteriaType.not_successful, {result_block_id}),
       ignore_block_result_criteria=IgnoreBlockResultCriteriaType.ignore_if_failed
       )(int_square, div_res)

    # Will print "625"
    ChainReaderCallRunner(cont)()(print_result, result_block_id)

    # Will print user input or error (exception info) with text "Too short!"
    crr = ChainReaderCallRunner(cont)
    crr()(print_result, 'User Input')


def func_call_runner_chain_simple_example():
    """
    Console output:

========================
=== FUNC-CALL-RUNNER-SIMPLE-CHAIN: ===

RESULT FOR "Test Holder Number 1": 625.0

ERROR IN "Test Holder Number 2": Can't compute!
{{CONTEXT_HOLDER_ID(Test Holder Number 2): CONTEXT_HOLDER_INFO(Will fail)}:[
(index(0), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: ChainLinkFailed (Too small!)))),
(index(1), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(2), depth(0), ID(<function int_div at 0x000001D1D8A4EEA0>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(3), depth(0), ID(Result), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT)))
]}

ERROR IN "Test Holder Number 3": Can't compute!
{{CONTEXT_HOLDER_ID(Test Holder Number 3): CONTEXT_HOLDER_INFO(Every function should return number >= 0. Will fail.)}:[
(index(0), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((True, 100))),
(index(1), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((False, -5))),
(index(2), depth(0), ID(<function int_div at 0x000001D1D8A4EEA0>), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT))),
(index(3), depth(0), ID(Result), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT)))
]}

ERROR IN "Test Holder Number 4": Can't compute!
{{CONTEXT_HOLDER_ID(Test Holder Number 4): CONTEXT_HOLDER_INFO(Every function should return even number. Will fail.)}:[
(index(0), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((True, 100))),
(index(1), depth(0), ID(<function random_int at 0x000001D1D8A4EE18>), INFO(None), RESULT((True, 4))),
(index(2), depth(0), ID(<function int_div at 0x000001D1D8A4EEA0>), INFO(None), RESULT((False, 25.0))),
(index(3), depth(0), ID(Result), INFO(None), RESULT((False, ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT)))
]}


========================

    :return:
    """
    # ============================
    # TEST 1:
    cont = Chain('Test Holder Number 1', 'Will be successful', ResultType(CriteriaType.optional, set()))
    cr = ChainUniCallRunner(cont, True)  # Simple-Mode - for any functions

    # Will be successful.
    # Will return 625 if you'll try to assign final result to the variable
    cr('Result')(
        int_square,
        cr()(
            int_div,
            cr()(random_int, 100, 100),  # 100
            cr()(random_int, 4, 4)  # 4
        )  # 25
    )  # 625

    # Will print "625"
    ChainReaderCallRunner(cont)()(print_result, 'Result')

    # ============================
    print()

    # ============================
    # TEST 2:
    cont = Chain('Test Holder Number 2', 'Will fail', ResultType(CriteriaType.optional, set()))
    cr = ChainUniCallRunner(cont, True)  # Simple-Mode - for any functions

    # Will fail: -40 < -20.
    # Will return None if you'll try to assign final result to the variable
    cr('Result')(
        int_square,  # Will not be computed
        cr()(
            int_div,  # Will not be computed
            cr()(random_int, -40, 0),  # -40 < -20. EXCEPTION ChainLinkFailed ("Too small!")
            cr()(random_int, 3, 4)))  # Will not be computed

    # Will print an error
    ChainReaderCallRunner(cont)()(print_result, 'Result')

    # ============================
    print()

    # ============================
    # TEST 3:
    cont = Chain('Test Holder Number 3', 'Every function should return number >= 0. Will fail.',
                 ResultType(CriteriaType.optional, set()))
    cr = ChainUniCallRunner(cont, True, lambda result: result >= 0)  # Simple-Mode - for any functions

    # Will fail: random_int(-5, -1) < 0.
    # Will return None if you'll try to assign final result to the variable
    cr('Result')(
        int_square,
        cr()(
            int_div,
            cr()(random_int, 100, 100),  # 100
            cr()(random_int, -5, -1)  # result < 0. Result state is FAIL (push_result(False, ...))
        )  # Will not be computed
    )  # Will not be computed

    # Will print an error
    ChainReaderCallRunner(cont)()(print_result, 'Result')

    # ============================
    print()

    # ============================
    # TEST 4:
    cont = Chain('Test Holder Number 4', 'Every function should return even number. Will fail.',
                 ResultType(CriteriaType.optional, set()))
    cr = ChainUniCallRunner(cont, True, lambda result: result % 2 == 0)  # Simple-Mode - for any functions

    # Will fail: 25 is odd.
    # Will return None if you'll try to assign final result to the variable
    int_1 = cr()(random_int, 100, 100)  # 100
    int_2 = cr()(random_int, 4, 4)  # 4
    div_res = cr()(int_div, int_1, int_2)  # 25. Result is odd. Result state is FAIL (push_result(False, 25))
    cr('Result')(int_square, div_res)  # Will not be computed

    # Will print an error
    ChainReaderCallRunner(cont)()(print_result, 'Result')


def main():
    separator = '========================\n'
    title_template = separator + '=== {} ===' + '\n'
    block_separator = ('\n' * 2) + (separator * 3) + ('\n' * 2)

    print(title_template.format('WITH-CHAIN-RAISE-EXCEPTIONS:'))
    with_chain_example(True)

    print(block_separator)
    print(title_template.format('WITH-CHAIN:'))
    with_chain_example(False)

    print(block_separator)
    print(title_template.format('FUNC-DECORATOR-COMPLICATED-CHAIN:'))
    func_decorator_chain_example()

    print(block_separator)
    print(title_template.format('FUNC-RUNNER-COMPLICATED-CHAIN:'))
    func_runner_chain_complicated_example()

    print(block_separator)
    print(title_template.format('FUNC-RUNNER-SIMPLE-CHAIN:'))
    func_runner_chain_simple_example()

    print(block_separator)
    print(title_template.format('FUNC-CALL-RUNNER-COMPLICATED-CHAIN:'))
    func_call_runner_chain_complicated_example()

    print(block_separator)
    print(title_template.format('FUNC-CALL-RUNNER-SIMPLE-CHAIN:'))
    func_call_runner_chain_simple_example()


if __name__ == "__main__":
    main()
