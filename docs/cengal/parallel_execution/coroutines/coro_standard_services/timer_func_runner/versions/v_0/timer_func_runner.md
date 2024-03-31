---
title: timer_func_runner
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.timer_func_runner<wbr>.versions<wbr>.v_0<wbr>.timer_func_runner    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-timer_func_runner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-timer_func_runner-view-source"><span>View Source</span></label>

                        <div class="pdoc-code codehilite"><pre><span></span><span id="L-1"><a href="#L-1"><span class="linenos">  1</span></a><span class="ch">#!/usr/bin/env python</span>
</span><span id="L-2"><a href="#L-2"><span class="linenos">  2</span></a><span class="c1"># coding=utf-8</span>
</span><span id="L-3"><a href="#L-3"><span class="linenos">  3</span></a>
</span><span id="L-4"><a href="#L-4"><span class="linenos">  4</span></a><span class="c1"># Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;</span>
</span><span id="L-5"><a href="#L-5"><span class="linenos">  5</span></a><span class="c1"># </span>
</span><span id="L-6"><a href="#L-6"><span class="linenos">  6</span></a><span class="c1"># Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span>
</span><span id="L-7"><a href="#L-7"><span class="linenos">  7</span></a><span class="c1"># you may not use this file except in compliance with the License.</span>
</span><span id="L-8"><a href="#L-8"><span class="linenos">  8</span></a><span class="c1"># You may obtain a copy of the License at</span>
</span><span id="L-9"><a href="#L-9"><span class="linenos">  9</span></a><span class="c1"># </span>
</span><span id="L-10"><a href="#L-10"><span class="linenos"> 10</span></a><span class="c1">#     http://www.apache.org/licenses/LICENSE-2.0</span>
</span><span id="L-11"><a href="#L-11"><span class="linenos"> 11</span></a><span class="c1"># </span>
</span><span id="L-12"><a href="#L-12"><span class="linenos"> 12</span></a><span class="c1"># Unless required by applicable law or agreed to in writing, software</span>
</span><span id="L-13"><a href="#L-13"><span class="linenos"> 13</span></a><span class="c1"># distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span>
</span><span id="L-14"><a href="#L-14"><span class="linenos"> 14</span></a><span class="c1"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span>
</span><span id="L-15"><a href="#L-15"><span class="linenos"> 15</span></a><span class="c1"># See the License for the specific language governing permissions and</span>
</span><span id="L-16"><a href="#L-16"><span class="linenos"> 16</span></a><span class="c1"># limitations under the License.</span>
</span><span id="L-17"><a href="#L-17"><span class="linenos"> 17</span></a>
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="sd">Module Docstring</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.2.0&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TimerFuncRunner&#39;</span><span class="p">,</span> <span class="s1">&#39;add_timer_func_run_from_other_service&#39;</span><span class="p">,</span> <span class="s1">&#39;discard_timer_func_run_from_other_service&#39;</span><span class="p">,</span> <span class="s1">&#39;timer_func_run_on&#39;</span><span class="p">,</span> <span class="s1">&#39;try_timer_func_run_on&#39;</span><span class="p">,</span> <span class="s1">&#39;atimer_func_run_on&#39;</span><span class="p">,</span> <span class="s1">&#39;atry_timer_func_run_on&#39;</span><span class="p">,</span> <span class="s1">&#39;timer_func_run&#39;</span><span class="p">,</span> <span class="s1">&#39;try_timer_func_run&#39;</span><span class="p">,</span> <span class="s1">&#39;atimer_func_run&#39;</span><span class="p">,</span> <span class="s1">&#39;atry_timer_func_run&#39;</span><span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values</span> <span class="kn">import</span> <span class="n">ValueExistence</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.timer</span> <span class="kn">import</span> <span class="n">Timer</span><span class="p">,</span> <span class="n">TimerRequest</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">overload</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="k">class</span> <span class="nc">TimerFuncRunnerRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="k">def</span> <span class="nf">discard</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">)</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="k">class</span> <span class="nc">TimerFuncRunner</span><span class="p">(</span><span class="n">DualImmediateProcessingServiceMixin</span><span class="p">,</span> <span class="n">ServiceWithADirectRequestMixin</span><span class="p">,</span> <span class="n">TypedService</span><span class="p">[</span><span class="n">TimerRequest</span><span class="p">]):</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span> <span class="o">=</span> <span class="n">Timer</span><span class="p">()</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_add</span><span class="p">,</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_discard</span><span class="p">,</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="p">}</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing_single</span><span class="p">(</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">TimerRequest</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">is_background_coro</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="nf">_add_request_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="k">def</span> <span class="nf">timer_handler_func</span><span class="p">(</span><span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">handler_</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args_</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs_</span><span class="p">):</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>                <span class="n">handler_</span><span class="p">(</span><span class="o">*</span><span class="n">args_</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs_</span><span class="p">)</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">exception</span><span class="p">(</span><span class="s1">&#39;TimerFuncRunner. Event handler error&#39;</span><span class="p">)</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>            <span class="k">finally</span><span class="p">:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="n">timer_handler</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">timer_handler_func</span><span class="p">,</span> <span class="n">foreground</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_added</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">timer_handler</span><span class="p">,</span> <span class="n">delay</span><span class="p">)</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="n">timer_request</span><span class="o">.</span><span class="n">foreground</span> <span class="o">=</span> <span class="n">foreground</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="k">return</span> <span class="n">timer_request</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="k">def</span> <span class="nf">_on_add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">TimerRequest</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>            <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">is_background_coro</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="nf">_on_discard</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">TimerRequest</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">timer_request</span><span class="p">)</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">timer_request</span><span class="o">.</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>        
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">add_timer_func_run_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="n">foreground</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="k">return</span> <span class="n">timer_request</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>    <span class="k">def</span> <span class="nf">discard_timer_func_run_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">timer_request</span><span class="p">)</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">timer_request</span><span class="o">.</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="n">direct_requests_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">direct_requests_buff</span><span class="p">)()</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="k">for</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="ow">in</span> <span class="n">direct_requests_buff</span><span class="p">:</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="p">()</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span><span class="p">:</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">_add_direct_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="k">return</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    <span class="k">def</span> <span class="nf">task_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    <span class="k">def</span> <span class="nf">task_triggered</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">in_forground_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">)</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">nearest_event</span><span class="p">()</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a><span class="n">TimerFuncRunnerRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">TimerFuncRunner</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a><span class="k">def</span> <span class="nf">add_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">current_service</span><span class="p">:</span> <span class="n">Service</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="n">timer_func_runner</span><span class="p">:</span> <span class="n">TimerFuncRunner</span> <span class="o">=</span> <span class="n">current_service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    <span class="k">return</span> <span class="n">timer_func_runner</span><span class="o">.</span><span class="n">add_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">foreground</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a><span class="k">def</span> <span class="nf">discard_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">current_service</span><span class="p">:</span> <span class="n">Service</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    <span class="n">timer_func_runner</span><span class="p">:</span> <span class="n">TimerFuncRunner</span> <span class="o">=</span> <span class="n">current_service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">)</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    <span class="k">return</span> <span class="n">timer_func_runner</span><span class="o">.</span><span class="n">discard_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">timer_request</span><span class="p">)</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a><span class="k">def</span> <span class="nf">timer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a><span class="sd">        </span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a><span class="sd">        An example:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroSchedulerType, ExplicitWorker, Worker, CoroID</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import timer_func_run_on</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a><span class="sd">        from typing import Optional, Union</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="sd">        def my_func(loop: CoroSchedulerType, coro_worker: AnyWorker, a, b) -&gt; Optional[CoroID]:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="sd">            try:</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="sd">                def print_hello_world(name: str):</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">                    print(f&#39;Hello Wrold from {name}!)</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">                </span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="sd">                timer_func_run_on(10, print_hello_world, &#39;John Doe&#39;)</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a><span class="sd">            except CoroSchedulerContextIsNotAvailable:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a><span class="sd">                print(&#39;We are outside of the loop AND no loop was selected as a Primary AND our given `loop` var is None)</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a><span class="sd">        </span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a><span class="sd">    Args:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a><span class="sd">        context (Tuple[Optional[CoroSchedulerType], Optional[Interface], bool]): _description_</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a><span class="sd">        delay (float): delay in seconds</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="sd">        handler (Callable): handler</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">    Returns:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">        ValueExistence[Optional[CoroID]]: _description_</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>    <span class="k">return</span> <span class="n">make_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="k">def</span> <span class="nf">try_timer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a><span class="sd">        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="sd">        </span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a><span class="sd">        An example:</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroSchedulerType, ExplicitWorker, Worker, CoroID</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import try_put_coro_to</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a><span class="sd">        from typing import Optional, Union</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="sd">        def my_func(loop: CoroSchedulerType, coro_worker: AnyWorker, a, b) -&gt; Optional[CoroID]:</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a><span class="sd">            def print_hello_world(name: str):</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a><span class="sd">                print(f&#39;Hello Wrold from {name}!)</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a><span class="sd">            </span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a><span class="sd">            try_timer_func_run_on(10, print_hello_world, &#39;John Doe&#39;)</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a><span class="sd">        </span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a><span class="sd">    Args:</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a><span class="sd">        context (Tuple[Optional[CoroSchedulerType], Optional[Interface], bool]): _description_</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a><span class="sd">        delay (float): delay in seconds</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="sd">        handler (Callable): handler</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a><span class="sd">    Returns:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a><span class="sd">        ValueExistence[Optional[CoroID]]: _description_</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>    <span class="k">return</span> <span class="n">try_make_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atimer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]:</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">amake_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atry_timer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">atry_make_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="k">def</span> <span class="nf">timer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="k">return</span> <span class="n">make_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a><span class="k">def</span> <span class="nf">try_timer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>    <span class="k">return</span> <span class="n">try_make_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atimer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]:</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">amake_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atry_timer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">atry_make_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="TimerFuncRunner">
                            <input id="TimerFuncRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TimerFuncRunner</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.DualImmediateProcessingServiceMixin</span>, <span class="base">cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request.versions.v_0.service_with_a_direct_request.ServiceWithADirectRequestMixin</span>, <span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.TypedService[cengal.time_management.timer.versions.v_0.timer.TimerRequest]</span>):

                <label class="view-source-button" for="TimerFuncRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner-55"><a href="#TimerFuncRunner-55"><span class="linenos"> 55</span></a><span class="k">class</span> <span class="nc">TimerFuncRunner</span><span class="p">(</span><span class="n">DualImmediateProcessingServiceMixin</span><span class="p">,</span> <span class="n">ServiceWithADirectRequestMixin</span><span class="p">,</span> <span class="n">TypedService</span><span class="p">[</span><span class="n">TimerRequest</span><span class="p">]):</span>
</span><span id="TimerFuncRunner-56"><a href="#TimerFuncRunner-56"><span class="linenos"> 56</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="TimerFuncRunner-57"><a href="#TimerFuncRunner-57"><span class="linenos"> 57</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TimerFuncRunner-58"><a href="#TimerFuncRunner-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span> <span class="o">=</span> <span class="n">Timer</span><span class="p">()</span>
</span><span id="TimerFuncRunner-59"><a href="#TimerFuncRunner-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TimerFuncRunner-60"><a href="#TimerFuncRunner-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TimerFuncRunner-61"><a href="#TimerFuncRunner-61"><span class="linenos"> 61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TimerFuncRunner-62"><a href="#TimerFuncRunner-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="TimerFuncRunner-63"><a href="#TimerFuncRunner-63"><span class="linenos"> 63</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_add</span><span class="p">,</span>
</span><span id="TimerFuncRunner-64"><a href="#TimerFuncRunner-64"><span class="linenos"> 64</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_discard</span><span class="p">,</span>
</span><span id="TimerFuncRunner-65"><a href="#TimerFuncRunner-65"><span class="linenos"> 65</span></a>        <span class="p">}</span>
</span><span id="TimerFuncRunner-66"><a href="#TimerFuncRunner-66"><span class="linenos"> 66</span></a>
</span><span id="TimerFuncRunner-67"><a href="#TimerFuncRunner-67"><span class="linenos"> 67</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing_single</span><span class="p">(</span>
</span><span id="TimerFuncRunner-68"><a href="#TimerFuncRunner-68"><span class="linenos"> 68</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">TimerRequest</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="TimerFuncRunner-69"><a href="#TimerFuncRunner-69"><span class="linenos"> 69</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">is_background_coro</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TimerFuncRunner-70"><a href="#TimerFuncRunner-70"><span class="linenos"> 70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TimerFuncRunner-71"><a href="#TimerFuncRunner-71"><span class="linenos"> 71</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TimerFuncRunner-72"><a href="#TimerFuncRunner-72"><span class="linenos"> 72</span></a>    
</span><span id="TimerFuncRunner-73"><a href="#TimerFuncRunner-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="nf">_add_request_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="TimerFuncRunner-74"><a href="#TimerFuncRunner-74"><span class="linenos"> 74</span></a>        <span class="k">def</span> <span class="nf">timer_handler_func</span><span class="p">(</span><span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">handler_</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args_</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs_</span><span class="p">):</span>
</span><span id="TimerFuncRunner-75"><a href="#TimerFuncRunner-75"><span class="linenos"> 75</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="TimerFuncRunner-76"><a href="#TimerFuncRunner-76"><span class="linenos"> 76</span></a>                <span class="n">handler_</span><span class="p">(</span><span class="o">*</span><span class="n">args_</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs_</span><span class="p">)</span>
</span><span id="TimerFuncRunner-77"><a href="#TimerFuncRunner-77"><span class="linenos"> 77</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="TimerFuncRunner-78"><a href="#TimerFuncRunner-78"><span class="linenos"> 78</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">exception</span><span class="p">(</span><span class="s1">&#39;TimerFuncRunner. Event handler error&#39;</span><span class="p">)</span>
</span><span id="TimerFuncRunner-79"><a href="#TimerFuncRunner-79"><span class="linenos"> 79</span></a>            <span class="k">finally</span><span class="p">:</span>
</span><span id="TimerFuncRunner-80"><a href="#TimerFuncRunner-80"><span class="linenos"> 80</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="TimerFuncRunner-81"><a href="#TimerFuncRunner-81"><span class="linenos"> 81</span></a>
</span><span id="TimerFuncRunner-82"><a href="#TimerFuncRunner-82"><span class="linenos"> 82</span></a>        <span class="n">timer_handler</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">timer_handler_func</span><span class="p">,</span> <span class="n">foreground</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TimerFuncRunner-83"><a href="#TimerFuncRunner-83"><span class="linenos"> 83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_added</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="TimerFuncRunner-84"><a href="#TimerFuncRunner-84"><span class="linenos"> 84</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">timer_handler</span><span class="p">,</span> <span class="n">delay</span><span class="p">)</span>
</span><span id="TimerFuncRunner-85"><a href="#TimerFuncRunner-85"><span class="linenos"> 85</span></a>        <span class="n">timer_request</span><span class="o">.</span><span class="n">foreground</span> <span class="o">=</span> <span class="n">foreground</span>
</span><span id="TimerFuncRunner-86"><a href="#TimerFuncRunner-86"><span class="linenos"> 86</span></a>        <span class="k">return</span> <span class="n">timer_request</span>
</span><span id="TimerFuncRunner-87"><a href="#TimerFuncRunner-87"><span class="linenos"> 87</span></a>    
</span><span id="TimerFuncRunner-88"><a href="#TimerFuncRunner-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="nf">_on_add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">TimerRequest</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="TimerFuncRunner-89"><a href="#TimerFuncRunner-89"><span class="linenos"> 89</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span>
</span><span id="TimerFuncRunner-90"><a href="#TimerFuncRunner-90"><span class="linenos"> 90</span></a>            <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">is_background_coro</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TimerFuncRunner-91"><a href="#TimerFuncRunner-91"><span class="linenos"> 91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TimerFuncRunner-92"><a href="#TimerFuncRunner-92"><span class="linenos"> 92</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TimerFuncRunner-93"><a href="#TimerFuncRunner-93"><span class="linenos"> 93</span></a>    
</span><span id="TimerFuncRunner-94"><a href="#TimerFuncRunner-94"><span class="linenos"> 94</span></a>    <span class="k">def</span> <span class="nf">_on_discard</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">TimerRequest</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="TimerFuncRunner-95"><a href="#TimerFuncRunner-95"><span class="linenos"> 95</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">timer_request</span><span class="p">)</span>
</span><span id="TimerFuncRunner-96"><a href="#TimerFuncRunner-96"><span class="linenos"> 96</span></a>        <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
</span><span id="TimerFuncRunner-97"><a href="#TimerFuncRunner-97"><span class="linenos"> 97</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">timer_request</span><span class="o">.</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="TimerFuncRunner-98"><a href="#TimerFuncRunner-98"><span class="linenos"> 98</span></a>        
</span><span id="TimerFuncRunner-99"><a href="#TimerFuncRunner-99"><span class="linenos"> 99</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TimerFuncRunner-100"><a href="#TimerFuncRunner-100"><span class="linenos">100</span></a>    
</span><span id="TimerFuncRunner-101"><a href="#TimerFuncRunner-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">add_timer_func_run_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="TimerFuncRunner-102"><a href="#TimerFuncRunner-102"><span class="linenos">102</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="n">foreground</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TimerFuncRunner-103"><a href="#TimerFuncRunner-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TimerFuncRunner-104"><a href="#TimerFuncRunner-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="n">timer_request</span>
</span><span id="TimerFuncRunner-105"><a href="#TimerFuncRunner-105"><span class="linenos">105</span></a>    
</span><span id="TimerFuncRunner-106"><a href="#TimerFuncRunner-106"><span class="linenos">106</span></a>    <span class="k">def</span> <span class="nf">discard_timer_func_run_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TimerFuncRunner-107"><a href="#TimerFuncRunner-107"><span class="linenos">107</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">timer_request</span><span class="p">)</span>
</span><span id="TimerFuncRunner-108"><a href="#TimerFuncRunner-108"><span class="linenos">108</span></a>        <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
</span><span id="TimerFuncRunner-109"><a href="#TimerFuncRunner-109"><span class="linenos">109</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">timer_request</span><span class="o">.</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="TimerFuncRunner-110"><a href="#TimerFuncRunner-110"><span class="linenos">110</span></a>        
</span><span id="TimerFuncRunner-111"><a href="#TimerFuncRunner-111"><span class="linenos">111</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="TimerFuncRunner-112"><a href="#TimerFuncRunner-112"><span class="linenos">112</span></a>
</span><span id="TimerFuncRunner-113"><a href="#TimerFuncRunner-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TimerFuncRunner-114"><a href="#TimerFuncRunner-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">:</span>
</span><span id="TimerFuncRunner-115"><a href="#TimerFuncRunner-115"><span class="linenos">115</span></a>            <span class="n">direct_requests_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span>
</span><span id="TimerFuncRunner-116"><a href="#TimerFuncRunner-116"><span class="linenos">116</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">direct_requests_buff</span><span class="p">)()</span>
</span><span id="TimerFuncRunner-117"><a href="#TimerFuncRunner-117"><span class="linenos">117</span></a>            <span class="k">for</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="ow">in</span> <span class="n">direct_requests_buff</span><span class="p">:</span>
</span><span id="TimerFuncRunner-118"><a href="#TimerFuncRunner-118"><span class="linenos">118</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TimerFuncRunner-119"><a href="#TimerFuncRunner-119"><span class="linenos">119</span></a>        
</span><span id="TimerFuncRunner-120"><a href="#TimerFuncRunner-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="p">()</span>
</span><span id="TimerFuncRunner-121"><a href="#TimerFuncRunner-121"><span class="linenos">121</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span><span class="p">:</span>
</span><span id="TimerFuncRunner-122"><a href="#TimerFuncRunner-122"><span class="linenos">122</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="TimerFuncRunner-123"><a href="#TimerFuncRunner-123"><span class="linenos">123</span></a>    
</span><span id="TimerFuncRunner-124"><a href="#TimerFuncRunner-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">_add_direct_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
</span><span id="TimerFuncRunner-125"><a href="#TimerFuncRunner-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">))</span>
</span><span id="TimerFuncRunner-126"><a href="#TimerFuncRunner-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TimerFuncRunner-127"><a href="#TimerFuncRunner-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TimerFuncRunner-128"><a href="#TimerFuncRunner-128"><span class="linenos">128</span></a>
</span><span id="TimerFuncRunner-129"><a href="#TimerFuncRunner-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">task_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="TimerFuncRunner-130"><a href="#TimerFuncRunner-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TimerFuncRunner-131"><a href="#TimerFuncRunner-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="TimerFuncRunner-132"><a href="#TimerFuncRunner-132"><span class="linenos">132</span></a>
</span><span id="TimerFuncRunner-133"><a href="#TimerFuncRunner-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">task_triggered</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="TimerFuncRunner-134"><a href="#TimerFuncRunner-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="TimerFuncRunner-135"><a href="#TimerFuncRunner-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="TimerFuncRunner-136"><a href="#TimerFuncRunner-136"><span class="linenos">136</span></a>
</span><span id="TimerFuncRunner-137"><a href="#TimerFuncRunner-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TimerFuncRunner-138"><a href="#TimerFuncRunner-138"><span class="linenos">138</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">)</span>
</span><span id="TimerFuncRunner-139"><a href="#TimerFuncRunner-139"><span class="linenos">139</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="TimerFuncRunner-140"><a href="#TimerFuncRunner-140"><span class="linenos">140</span></a>    
</span><span id="TimerFuncRunner-141"><a href="#TimerFuncRunner-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="nf">in_forground_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TimerFuncRunner-142"><a href="#TimerFuncRunner-142"><span class="linenos">142</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">)</span>
</span><span id="TimerFuncRunner-143"><a href="#TimerFuncRunner-143"><span class="linenos">143</span></a>    
</span><span id="TimerFuncRunner-144"><a href="#TimerFuncRunner-144"><span class="linenos">144</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="TimerFuncRunner-145"><a href="#TimerFuncRunner-145"><span class="linenos">145</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">nearest_event</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="TimerFuncRunner.__init__" class="classattr">
                                        <input id="TimerFuncRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TimerFuncRunner</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="TimerFuncRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.__init__-56"><a href="#TimerFuncRunner.__init__-56"><span class="linenos">56</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="TimerFuncRunner.__init__-57"><a href="#TimerFuncRunner.__init__-57"><span class="linenos">57</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TimerFuncRunner.__init__-58"><a href="#TimerFuncRunner.__init__-58"><span class="linenos">58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span> <span class="o">=</span> <span class="n">Timer</span><span class="p">()</span>
</span><span id="TimerFuncRunner.__init__-59"><a href="#TimerFuncRunner.__init__-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TimerFuncRunner.__init__-60"><a href="#TimerFuncRunner.__init__-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TimerFuncRunner.__init__-61"><a href="#TimerFuncRunner.__init__-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TimerFuncRunner.__init__-62"><a href="#TimerFuncRunner.__init__-62"><span class="linenos">62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="TimerFuncRunner.__init__-63"><a href="#TimerFuncRunner.__init__-63"><span class="linenos">63</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_add</span><span class="p">,</span>
</span><span id="TimerFuncRunner.__init__-64"><a href="#TimerFuncRunner.__init__-64"><span class="linenos">64</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_discard</span><span class="p">,</span>
</span><span id="TimerFuncRunner.__init__-65"><a href="#TimerFuncRunner.__init__-65"><span class="linenos">65</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="TimerFuncRunner.timer" class="classattr">
                                <div class="attr variable">
            <span class="name">timer</span>

        
    </div>
    <a class="headerlink" href="#TimerFuncRunner.timer"></a>
    
    

                            </div>
                            <div id="TimerFuncRunner.pending_tasks_number" class="classattr">
                                <div class="attr variable">
            <span class="name">pending_tasks_number</span>

        
    </div>
    <a class="headerlink" href="#TimerFuncRunner.pending_tasks_number"></a>
    
    

                            </div>
                            <div id="TimerFuncRunner.pending_foreground_tasks_number" class="classattr">
                                <div class="attr variable">
            <span class="name">pending_foreground_tasks_number</span>

        
    </div>
    <a class="headerlink" href="#TimerFuncRunner.pending_foreground_tasks_number"></a>
    
    

                            </div>
                            <div id="TimerFuncRunner.direct_requests" class="classattr">
                                <div class="attr variable">
            <span class="name">direct_requests</span>

        
    </div>
    <a class="headerlink" href="#TimerFuncRunner.direct_requests"></a>
    
    

                            </div>
                            <div id="TimerFuncRunner.add_timer_func_run_from_other_service" class="classattr">
                                        <input id="TimerFuncRunner.add_timer_func_run_from_other_service-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_timer_func_run_from_other_service</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span>,</span><span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">time_management</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">TimerRequest</span>:</span></span>

                <label class="view-source-button" for="TimerFuncRunner.add_timer_func_run_from_other_service-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.add_timer_func_run_from_other_service"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.add_timer_func_run_from_other_service-101"><a href="#TimerFuncRunner.add_timer_func_run_from_other_service-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">add_timer_func_run_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="TimerFuncRunner.add_timer_func_run_from_other_service-102"><a href="#TimerFuncRunner.add_timer_func_run_from_other_service-102"><span class="linenos">102</span></a>        <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="n">foreground</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TimerFuncRunner.add_timer_func_run_from_other_service-103"><a href="#TimerFuncRunner.add_timer_func_run_from_other_service-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TimerFuncRunner.add_timer_func_run_from_other_service-104"><a href="#TimerFuncRunner.add_timer_func_run_from_other_service-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="n">timer_request</span>
</span></pre></div>


    

                            </div>
                            <div id="TimerFuncRunner.discard_timer_func_run_from_other_service" class="classattr">
                                        <input id="TimerFuncRunner.discard_timer_func_run_from_other_service-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">discard_timer_func_run_from_other_service</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">timer_request</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">time_management</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">TimerRequest</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TimerFuncRunner.discard_timer_func_run_from_other_service-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.discard_timer_func_run_from_other_service"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.discard_timer_func_run_from_other_service-106"><a href="#TimerFuncRunner.discard_timer_func_run_from_other_service-106"><span class="linenos">106</span></a>    <span class="k">def</span> <span class="nf">discard_timer_func_run_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TimerFuncRunner.discard_timer_func_run_from_other_service-107"><a href="#TimerFuncRunner.discard_timer_func_run_from_other_service-107"><span class="linenos">107</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">timer_request</span><span class="p">)</span>
</span><span id="TimerFuncRunner.discard_timer_func_run_from_other_service-108"><a href="#TimerFuncRunner.discard_timer_func_run_from_other_service-108"><span class="linenos">108</span></a>        <span class="k">if</span> <span class="n">result</span><span class="p">:</span>
</span><span id="TimerFuncRunner.discard_timer_func_run_from_other_service-109"><a href="#TimerFuncRunner.discard_timer_func_run_from_other_service-109"><span class="linenos">109</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">timer_request</span><span class="o">.</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="TimerFuncRunner.discard_timer_func_run_from_other_service-110"><a href="#TimerFuncRunner.discard_timer_func_run_from_other_service-110"><span class="linenos">110</span></a>        
</span><span id="TimerFuncRunner.discard_timer_func_run_from_other_service-111"><a href="#TimerFuncRunner.discard_timer_func_run_from_other_service-111"><span class="linenos">111</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TimerFuncRunner.full_processing_iteration" class="classattr">
                                        <input id="TimerFuncRunner.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TimerFuncRunner.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.full_processing_iteration-113"><a href="#TimerFuncRunner.full_processing_iteration-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TimerFuncRunner.full_processing_iteration-114"><a href="#TimerFuncRunner.full_processing_iteration-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">:</span>
</span><span id="TimerFuncRunner.full_processing_iteration-115"><a href="#TimerFuncRunner.full_processing_iteration-115"><span class="linenos">115</span></a>            <span class="n">direct_requests_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span>
</span><span id="TimerFuncRunner.full_processing_iteration-116"><a href="#TimerFuncRunner.full_processing_iteration-116"><span class="linenos">116</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">direct_requests_buff</span><span class="p">)()</span>
</span><span id="TimerFuncRunner.full_processing_iteration-117"><a href="#TimerFuncRunner.full_processing_iteration-117"><span class="linenos">117</span></a>            <span class="k">for</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="ow">in</span> <span class="n">direct_requests_buff</span><span class="p">:</span>
</span><span id="TimerFuncRunner.full_processing_iteration-118"><a href="#TimerFuncRunner.full_processing_iteration-118"><span class="linenos">118</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_add_request_impl</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TimerFuncRunner.full_processing_iteration-119"><a href="#TimerFuncRunner.full_processing_iteration-119"><span class="linenos">119</span></a>        
</span><span id="TimerFuncRunner.full_processing_iteration-120"><a href="#TimerFuncRunner.full_processing_iteration-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="p">()</span>
</span><span id="TimerFuncRunner.full_processing_iteration-121"><a href="#TimerFuncRunner.full_processing_iteration-121"><span class="linenos">121</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span><span class="p">:</span>
</span><span id="TimerFuncRunner.full_processing_iteration-122"><a href="#TimerFuncRunner.full_processing_iteration-122"><span class="linenos">122</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TimerFuncRunner.task_added" class="classattr">
                                        <input id="TimerFuncRunner.task_added-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">task_added</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TimerFuncRunner.task_added-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.task_added"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.task_added-129"><a href="#TimerFuncRunner.task_added-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">task_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="TimerFuncRunner.task_added-130"><a href="#TimerFuncRunner.task_added-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TimerFuncRunner.task_added-131"><a href="#TimerFuncRunner.task_added-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="TimerFuncRunner.task_triggered" class="classattr">
                                        <input id="TimerFuncRunner.task_triggered-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">task_triggered</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TimerFuncRunner.task_triggered-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.task_triggered"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.task_triggered-133"><a href="#TimerFuncRunner.task_triggered-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">task_triggered</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="TimerFuncRunner.task_triggered-134"><a href="#TimerFuncRunner.task_triggered-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="TimerFuncRunner.task_triggered-135"><a href="#TimerFuncRunner.task_triggered-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="TimerFuncRunner.in_work" class="classattr">
                                        <input id="TimerFuncRunner.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TimerFuncRunner.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.in_work-137"><a href="#TimerFuncRunner.in_work-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TimerFuncRunner.in_work-138"><a href="#TimerFuncRunner.in_work-138"><span class="linenos">138</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">)</span>
</span><span id="TimerFuncRunner.in_work-139"><a href="#TimerFuncRunner.in_work-139"><span class="linenos">139</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="TimerFuncRunner.in_forground_work" class="classattr">
                                        <input id="TimerFuncRunner.in_forground_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_forground_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TimerFuncRunner.in_forground_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.in_forground_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.in_forground_work-141"><a href="#TimerFuncRunner.in_forground_work-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="nf">in_forground_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TimerFuncRunner.in_forground_work-142"><a href="#TimerFuncRunner.in_forground_work-142"><span class="linenos">142</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direct_requests</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TimerFuncRunner.time_left_before_next_event" class="classattr">
                                        <input id="TimerFuncRunner.time_left_before_next_event-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">time_left_before_next_event</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="TimerFuncRunner.time_left_before_next_event-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimerFuncRunner.time_left_before_next_event"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimerFuncRunner.time_left_before_next_event-144"><a href="#TimerFuncRunner.time_left_before_next_event-144"><span class="linenos">144</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="TimerFuncRunner.time_left_before_next_event-145"><a href="#TimerFuncRunner.time_left_before_next_event-145"><span class="linenos">145</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">nearest_event</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.DualImmediateProcessingServiceMixin</dt>
                                <dd id="TimerFuncRunner.single_task_registration_or_immediate_processing" class="function">single_task_registration_or_immediate_processing</dd>
                <dd id="TimerFuncRunner.single_task_registration_or_immediate_processing_multiple" class="function">single_task_registration_or_immediate_processing_multiple</dd>
                <dd id="TimerFuncRunner.single_task_registration_or_immediate_processing_single" class="function">single_task_registration_or_immediate_processing_single</dd>

            </div>
            <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="TimerFuncRunner.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="TimerFuncRunner.iteration" class="function">iteration</dd>
                <dd id="TimerFuncRunner.make_response" class="function">make_response</dd>
                <dd id="TimerFuncRunner.register_response" class="function">register_response</dd>
                <dd id="TimerFuncRunner.put_task" class="function">put_task</dd>
                <dd id="TimerFuncRunner.resolve_request" class="function">resolve_request</dd>
                <dd id="TimerFuncRunner.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="TimerFuncRunner.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="TimerFuncRunner.is_low_latency" class="function">is_low_latency</dd>
                <dd id="TimerFuncRunner.make_live" class="function">make_live</dd>
                <dd id="TimerFuncRunner.make_dead" class="function">make_dead</dd>
                <dd id="TimerFuncRunner.service_id_impl" class="function">service_id_impl</dd>
                <dd id="TimerFuncRunner.service_id" class="function">service_id</dd>
                <dd id="TimerFuncRunner.destroy" class="function">destroy</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="add_timer_func_run_from_other_service">
                            <input id="add_timer_func_run_from_other_service-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_timer_func_run_from_other_service</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">current_service</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span>,</span><span class="param">	<span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span>,</span><span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">time_management</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">TimerRequest</span>:</span></span>

                <label class="view-source-button" for="add_timer_func_run_from_other_service-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#add_timer_func_run_from_other_service"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="add_timer_func_run_from_other_service-151"><a href="#add_timer_func_run_from_other_service-151"><span class="linenos">151</span></a><span class="k">def</span> <span class="nf">add_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">current_service</span><span class="p">:</span> <span class="n">Service</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TimerRequest</span><span class="p">:</span>
</span><span id="add_timer_func_run_from_other_service-152"><a href="#add_timer_func_run_from_other_service-152"><span class="linenos">152</span></a>    <span class="n">timer_func_runner</span><span class="p">:</span> <span class="n">TimerFuncRunner</span> <span class="o">=</span> <span class="n">current_service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">)</span>
</span><span id="add_timer_func_run_from_other_service-153"><a href="#add_timer_func_run_from_other_service-153"><span class="linenos">153</span></a>    <span class="k">return</span> <span class="n">timer_func_runner</span><span class="o">.</span><span class="n">add_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">foreground</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="discard_timer_func_run_from_other_service">
                            <input id="discard_timer_func_run_from_other_service-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">discard_timer_func_run_from_other_service</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">current_service</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span>,</span><span class="param">	<span class="n">timer_request</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">time_management</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">TimerRequest</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="discard_timer_func_run_from_other_service-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#discard_timer_func_run_from_other_service"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="discard_timer_func_run_from_other_service-156"><a href="#discard_timer_func_run_from_other_service-156"><span class="linenos">156</span></a><span class="k">def</span> <span class="nf">discard_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">current_service</span><span class="p">:</span> <span class="n">Service</span><span class="p">,</span> <span class="n">timer_request</span><span class="p">:</span> <span class="n">TimerRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="discard_timer_func_run_from_other_service-157"><a href="#discard_timer_func_run_from_other_service-157"><span class="linenos">157</span></a>    <span class="n">timer_func_runner</span><span class="p">:</span> <span class="n">TimerFuncRunner</span> <span class="o">=</span> <span class="n">current_service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">)</span>
</span><span id="discard_timer_func_run_from_other_service-158"><a href="#discard_timer_func_run_from_other_service-158"><span class="linenos">158</span></a>    <span class="k">return</span> <span class="n">timer_func_runner</span><span class="o">.</span><span class="n">discard_timer_func_run_from_other_service</span><span class="p">(</span><span class="n">timer_request</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="timer_func_run_on">
                            <input id="timer_func_run_on-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">timer_func_run_on</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span>,</span><span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="timer_func_run_on-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#timer_func_run_on"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="timer_func_run_on-161"><a href="#timer_func_run_on-161"><span class="linenos">161</span></a><span class="k">def</span> <span class="nf">timer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="timer_func_run_on-162"><a href="#timer_func_run_on-162"><span class="linenos">162</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="timer_func_run_on-163"><a href="#timer_func_run_on-163"><span class="linenos">163</span></a><span class="sd">        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module</span>
</span><span id="timer_func_run_on-164"><a href="#timer_func_run_on-164"><span class="linenos">164</span></a><span class="sd">        </span>
</span><span id="timer_func_run_on-165"><a href="#timer_func_run_on-165"><span class="linenos">165</span></a><span class="sd">        An example:</span>
</span><span id="timer_func_run_on-166"><a href="#timer_func_run_on-166"><span class="linenos">166</span></a>
</span><span id="timer_func_run_on-167"><a href="#timer_func_run_on-167"><span class="linenos">167</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroSchedulerType, ExplicitWorker, Worker, CoroID</span>
</span><span id="timer_func_run_on-168"><a href="#timer_func_run_on-168"><span class="linenos">168</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import timer_func_run_on</span>
</span><span id="timer_func_run_on-169"><a href="#timer_func_run_on-169"><span class="linenos">169</span></a><span class="sd">        from typing import Optional, Union</span>
</span><span id="timer_func_run_on-170"><a href="#timer_func_run_on-170"><span class="linenos">170</span></a>
</span><span id="timer_func_run_on-171"><a href="#timer_func_run_on-171"><span class="linenos">171</span></a><span class="sd">        def my_func(loop: CoroSchedulerType, coro_worker: AnyWorker, a, b) -&gt; Optional[CoroID]:</span>
</span><span id="timer_func_run_on-172"><a href="#timer_func_run_on-172"><span class="linenos">172</span></a><span class="sd">            try:</span>
</span><span id="timer_func_run_on-173"><a href="#timer_func_run_on-173"><span class="linenos">173</span></a><span class="sd">                def print_hello_world(name: str):</span>
</span><span id="timer_func_run_on-174"><a href="#timer_func_run_on-174"><span class="linenos">174</span></a><span class="sd">                    print(f&#39;Hello Wrold from {name}!)</span>
</span><span id="timer_func_run_on-175"><a href="#timer_func_run_on-175"><span class="linenos">175</span></a><span class="sd">                </span>
</span><span id="timer_func_run_on-176"><a href="#timer_func_run_on-176"><span class="linenos">176</span></a><span class="sd">                timer_func_run_on(10, print_hello_world, &#39;John Doe&#39;)</span>
</span><span id="timer_func_run_on-177"><a href="#timer_func_run_on-177"><span class="linenos">177</span></a><span class="sd">            except CoroSchedulerContextIsNotAvailable:</span>
</span><span id="timer_func_run_on-178"><a href="#timer_func_run_on-178"><span class="linenos">178</span></a><span class="sd">                print(&#39;We are outside of the loop AND no loop was selected as a Primary AND our given `loop` var is None)</span>
</span><span id="timer_func_run_on-179"><a href="#timer_func_run_on-179"><span class="linenos">179</span></a><span class="sd">        </span>
</span><span id="timer_func_run_on-180"><a href="#timer_func_run_on-180"><span class="linenos">180</span></a><span class="sd">    Args:</span>
</span><span id="timer_func_run_on-181"><a href="#timer_func_run_on-181"><span class="linenos">181</span></a><span class="sd">        context (Tuple[Optional[CoroSchedulerType], Optional[Interface], bool]): _description_</span>
</span><span id="timer_func_run_on-182"><a href="#timer_func_run_on-182"><span class="linenos">182</span></a><span class="sd">        delay (float): delay in seconds</span>
</span><span id="timer_func_run_on-183"><a href="#timer_func_run_on-183"><span class="linenos">183</span></a><span class="sd">        handler (Callable): handler</span>
</span><span id="timer_func_run_on-184"><a href="#timer_func_run_on-184"><span class="linenos">184</span></a>
</span><span id="timer_func_run_on-185"><a href="#timer_func_run_on-185"><span class="linenos">185</span></a><span class="sd">    Returns:</span>
</span><span id="timer_func_run_on-186"><a href="#timer_func_run_on-186"><span class="linenos">186</span></a><span class="sd">        ValueExistence[Optional[CoroID]]: _description_</span>
</span><span id="timer_func_run_on-187"><a href="#timer_func_run_on-187"><span class="linenos">187</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="timer_func_run_on-188"><a href="#timer_func_run_on-188"><span class="linenos">188</span></a>    <span class="k">return</span> <span class="n">make_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>_summary_
    context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module</p>

<pre><code>An example:

from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroSchedulerType, ExplicitWorker, Worker, CoroID
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import timer_func_run_on
from typing import Optional, Union

def my_func(loop: CoroSchedulerType, coro_worker: AnyWorker, a, b) -&gt; Optional[CoroID]:
    try:
        def print_hello_world(name: str):
            print(f'Hello Wrold from {name}!)

        timer_func_run_on(10, print_hello_world, 'John Doe')
    except CoroSchedulerContextIsNotAvailable:
        print('We are outside of the loop AND no loop was selected as a Primary AND our given `loop` var is None)
</code></pre>

<p>Args:
    context (Tuple[Optional[CoroSchedulerType], Optional[Interface], bool]): _description_
    delay (float): delay in seconds
    handler (Callable): handler</p>

<p>Returns:
    ValueExistence[Optional[CoroID]]: _description_</p>
</div>


                </section>
                <section id="try_timer_func_run_on">
                            <input id="try_timer_func_run_on-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">try_timer_func_run_on</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span>,</span><span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="try_timer_func_run_on-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#try_timer_func_run_on"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="try_timer_func_run_on-191"><a href="#try_timer_func_run_on-191"><span class="linenos">191</span></a><span class="k">def</span> <span class="nf">try_timer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="try_timer_func_run_on-192"><a href="#try_timer_func_run_on-192"><span class="linenos">192</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="try_timer_func_run_on-193"><a href="#try_timer_func_run_on-193"><span class="linenos">193</span></a><span class="sd">        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module</span>
</span><span id="try_timer_func_run_on-194"><a href="#try_timer_func_run_on-194"><span class="linenos">194</span></a><span class="sd">        </span>
</span><span id="try_timer_func_run_on-195"><a href="#try_timer_func_run_on-195"><span class="linenos">195</span></a><span class="sd">        An example:</span>
</span><span id="try_timer_func_run_on-196"><a href="#try_timer_func_run_on-196"><span class="linenos">196</span></a>
</span><span id="try_timer_func_run_on-197"><a href="#try_timer_func_run_on-197"><span class="linenos">197</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroSchedulerType, ExplicitWorker, Worker, CoroID</span>
</span><span id="try_timer_func_run_on-198"><a href="#try_timer_func_run_on-198"><span class="linenos">198</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import try_put_coro_to</span>
</span><span id="try_timer_func_run_on-199"><a href="#try_timer_func_run_on-199"><span class="linenos">199</span></a><span class="sd">        from typing import Optional, Union</span>
</span><span id="try_timer_func_run_on-200"><a href="#try_timer_func_run_on-200"><span class="linenos">200</span></a>
</span><span id="try_timer_func_run_on-201"><a href="#try_timer_func_run_on-201"><span class="linenos">201</span></a><span class="sd">        def my_func(loop: CoroSchedulerType, coro_worker: AnyWorker, a, b) -&gt; Optional[CoroID]:</span>
</span><span id="try_timer_func_run_on-202"><a href="#try_timer_func_run_on-202"><span class="linenos">202</span></a><span class="sd">            def print_hello_world(name: str):</span>
</span><span id="try_timer_func_run_on-203"><a href="#try_timer_func_run_on-203"><span class="linenos">203</span></a><span class="sd">                print(f&#39;Hello Wrold from {name}!)</span>
</span><span id="try_timer_func_run_on-204"><a href="#try_timer_func_run_on-204"><span class="linenos">204</span></a><span class="sd">            </span>
</span><span id="try_timer_func_run_on-205"><a href="#try_timer_func_run_on-205"><span class="linenos">205</span></a><span class="sd">            try_timer_func_run_on(10, print_hello_world, &#39;John Doe&#39;)</span>
</span><span id="try_timer_func_run_on-206"><a href="#try_timer_func_run_on-206"><span class="linenos">206</span></a><span class="sd">        </span>
</span><span id="try_timer_func_run_on-207"><a href="#try_timer_func_run_on-207"><span class="linenos">207</span></a><span class="sd">    Args:</span>
</span><span id="try_timer_func_run_on-208"><a href="#try_timer_func_run_on-208"><span class="linenos">208</span></a><span class="sd">        context (Tuple[Optional[CoroSchedulerType], Optional[Interface], bool]): _description_</span>
</span><span id="try_timer_func_run_on-209"><a href="#try_timer_func_run_on-209"><span class="linenos">209</span></a><span class="sd">        delay (float): delay in seconds</span>
</span><span id="try_timer_func_run_on-210"><a href="#try_timer_func_run_on-210"><span class="linenos">210</span></a><span class="sd">        handler (Callable): handler</span>
</span><span id="try_timer_func_run_on-211"><a href="#try_timer_func_run_on-211"><span class="linenos">211</span></a>
</span><span id="try_timer_func_run_on-212"><a href="#try_timer_func_run_on-212"><span class="linenos">212</span></a><span class="sd">    Returns:</span>
</span><span id="try_timer_func_run_on-213"><a href="#try_timer_func_run_on-213"><span class="linenos">213</span></a><span class="sd">        ValueExistence[Optional[CoroID]]: _description_</span>
</span><span id="try_timer_func_run_on-214"><a href="#try_timer_func_run_on-214"><span class="linenos">214</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="try_timer_func_run_on-215"><a href="#try_timer_func_run_on-215"><span class="linenos">215</span></a>    <span class="k">return</span> <span class="n">try_make_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>_summary_
    context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module</p>

<pre><code>An example:

from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroSchedulerType, ExplicitWorker, Worker, CoroID
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import try_put_coro_to
from typing import Optional, Union

def my_func(loop: CoroSchedulerType, coro_worker: AnyWorker, a, b) -&gt; Optional[CoroID]:
    def print_hello_world(name: str):
        print(f'Hello Wrold from {name}!)

    try_timer_func_run_on(10, print_hello_world, 'John Doe')
</code></pre>

<p>Args:
    context (Tuple[Optional[CoroSchedulerType], Optional[Interface], bool]): _description_
    delay (float): delay in seconds
    handler (Callable): handler</p>

<p>Returns:
    ValueExistence[Optional[CoroID]]: _description_</p>
</div>


                </section>
                <section id="atimer_func_run_on">
                            <input id="atimer_func_run_on-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">atimer_func_run_on</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span>,</span><span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="atimer_func_run_on-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#atimer_func_run_on"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="atimer_func_run_on-218"><a href="#atimer_func_run_on-218"><span class="linenos">218</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atimer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]:</span>
</span><span id="atimer_func_run_on-219"><a href="#atimer_func_run_on-219"><span class="linenos">219</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">amake_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="atry_timer_func_run_on">
                            <input id="atry_timer_func_run_on-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">atry_timer_func_run_on</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span>,</span><span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="atry_timer_func_run_on-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#atry_timer_func_run_on"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="atry_timer_func_run_on-222"><a href="#atry_timer_func_run_on-222"><span class="linenos">222</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atry_timer_func_run_on</span><span class="p">(</span><span class="n">context</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">],</span> <span class="nb">bool</span><span class="p">],</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="atry_timer_func_run_on-223"><a href="#atry_timer_func_run_on-223"><span class="linenos">223</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">atry_make_request_to_service_with_context</span><span class="p">(</span><span class="n">context</span><span class="p">,</span> <span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="timer_func_run">
                            <input id="timer_func_run-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">timer_func_run</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="timer_func_run-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#timer_func_run"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="timer_func_run-226"><a href="#timer_func_run-226"><span class="linenos">226</span></a><span class="k">def</span> <span class="nf">timer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]:</span>
</span><span id="timer_func_run-227"><a href="#timer_func_run-227"><span class="linenos">227</span></a>    <span class="k">return</span> <span class="n">make_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="try_timer_func_run">
                            <input id="try_timer_func_run-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">try_timer_func_run</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="try_timer_func_run-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#try_timer_func_run"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="try_timer_func_run-230"><a href="#try_timer_func_run-230"><span class="linenos">230</span></a><span class="k">def</span> <span class="nf">try_timer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="try_timer_func_run-231"><a href="#try_timer_func_run-231"><span class="linenos">231</span></a>    <span class="k">return</span> <span class="n">try_make_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="atimer_func_run">
                            <input id="atimer_func_run-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">atimer_func_run</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="atimer_func_run-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#atimer_func_run"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="atimer_func_run-234"><a href="#atimer_func_run-234"><span class="linenos">234</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atimer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]:</span>
</span><span id="atimer_func_run-235"><a href="#atimer_func_run-235"><span class="linenos">235</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">amake_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="atry_timer_func_run">
                            <input id="atry_timer_func_run-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">atry_timer_func_run</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">delay</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="atry_timer_func_run-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#atry_timer_func_run"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="atry_timer_func_run-238"><a href="#atry_timer_func_run-238"><span class="linenos">238</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">atry_timer_func_run</span><span class="p">(</span><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistence</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]:</span>
</span><span id="atry_timer_func_run-239"><a href="#atry_timer_func_run-239"><span class="linenos">239</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">atry_make_request_to_service</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">handler</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>