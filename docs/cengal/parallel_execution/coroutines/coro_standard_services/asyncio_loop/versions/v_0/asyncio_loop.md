---
title: asyncio_loop
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.asyncio_loop<wbr>.versions<wbr>.v_0<wbr>.asyncio_loop    </h1>

                
                        <input id="mod-asyncio_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-asyncio_loop-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;AsyncioLoop&#39;</span><span class="p">,</span> <span class="s1">&#39;AsyncioLoopRequest&#39;</span><span class="p">,</span> <span class="s1">&#39;AsyncioLoopWasNotSetError&#39;</span><span class="p">,</span> <span class="s1">&#39;run_in_thread_pool&#39;</span><span class="p">,</span> <span class="s1">&#39;run_in_thread_pool_fast&#39;</span><span class="p">]</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.await_coro</span> <span class="kn">import</span> <span class="n">create_task</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.await_coro</span> <span class="kn">import</span> <span class="n">task_in_thread_pool</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">gly</span><span class="p">,</span> <span class="n">agly</span><span class="p">,</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.simple_yield</span> <span class="kn">import</span> <span class="n">Yield</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.sleep</span> <span class="kn">import</span> <span class="n">Sleep</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro</span> <span class="kn">import</span> <span class="n">PutCoro</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.throw_coro</span> <span class="kn">import</span> <span class="n">ThrowCoro</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.kill_coro</span> <span class="kn">import</span> <span class="n">KillCoro</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.wait_coro</span> <span class="kn">import</span> <span class="n">WaitCoro</span><span class="p">,</span> <span class="n">WaitCoroRequest</span><span class="p">,</span> <span class="n">CoroutineNotFoundError</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.asyncio.run_loop</span> <span class="kn">import</span> <span class="n">run_forever</span><span class="p">,</span> <span class="n">cancel_all_tasks</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.asyncio.atasks</span> <span class="kn">import</span> <span class="n">create_task_awaitable</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.file_manager</span> <span class="kn">import</span> <span class="n">path_relative_to_current_dir</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.cpu_clock_cycles</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.sleep_tools</span> <span class="kn">import</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">,</span> <span class="n">get_min_sleep_interval</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.serialization</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">cengal.math.numbers</span> <span class="kn">import</span> <span class="n">RationalNumber</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">Type</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">import</span> <span class="nn">os</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">get_event_loop</span><span class="p">,</span> <span class="n">get_running_loop</span><span class="p">,</span> <span class="n">Task</span> <span class="k">as</span> <span class="n">asyncio_Task</span><span class="p">,</span> <span class="n">sleep</span> <span class="k">as</span> <span class="n">asyncio_sleep</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">asyncio.coroutines</span> <span class="kn">import</span> <span class="n">_is_coroutine</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.args_manager</span> <span class="kn">import</span> <span class="n">args_kwargs</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">types</span> <span class="kn">import</span> <span class="n">coroutine</span> <span class="k">as</span> <span class="n">types_coroutine</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">coroutines</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">events</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">tasks</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="kn">import</span> <span class="nn">threading</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="sd">Module Docstring</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.3&quot;</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="k">class</span> <span class="nc">AsyncioLoopWasNotSetError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="k">pass</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="k">class</span> <span class="nc">ExternalAsyncioLoopAlreadyExistsError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="k">pass</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="k">class</span> <span class="nc">WaitingCancelled</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="k">pass</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="n">WAITING_FOR_NEW_REQUESTS_EVENT</span> <span class="o">=</span> <span class="s1">&#39;AsyncioLoopRequest - WaitingForNewRequestsEvent&#39;</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="k">class</span> <span class="nc">AsyncioLoopRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    <span class="k">def</span> <span class="nf">inherit_surrounding_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="nf">start_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">,</span> <span class="n">debug</span><span class="p">)</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="nf">ensure_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">)</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">)</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">wait</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio_Task</span><span class="p">:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">def</span> <span class="nf">_internal_loop_yield</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="nf">turn_on_loops_intercommunication</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">)</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="k">def</span> <span class="nf">_wait_intercommunication</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="nf">wait_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="k">def</span> <span class="nf">use_higher_level_sleep_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">)</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="nf">turn_on_low_latency_io_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">13</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">asyncio_coro_sleep_0</span><span class="p">():</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">asyncio_sleep</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="k">def</span> <span class="nf">request_giver</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="k">yield</span> <span class="n">request</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a><span class="nd">@types_coroutine</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a><span class="k">def</span> <span class="nf">asyncio_coro_request</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    <span class="k">return</span> <span class="p">(</span><span class="k">yield from</span> <span class="n">request_giver</span><span class="p">(</span><span class="n">request</span><span class="p">))</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="n">asyncio_coro_request</span><span class="o">.</span><span class="n">_is_coroutine</span> <span class="o">=</span> <span class="n">_is_coroutine</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="k">class</span> <span class="nc">AsyncioLoop</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroWrapperBase</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_internal_loop</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_new_requests</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_inherit_surrounding_loop</span><span class="p">,</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_start_internal_loop</span><span class="p">,</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_ensure_loop</span><span class="p">,</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set</span><span class="p">,</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_create_task</span><span class="p">,</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__internal_loop_yield</span><span class="p">,</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_turn_on_loops_intercommunication</span><span class="p">,</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="mi">10</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>            <span class="mi">11</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__internal_wait_for_new_requests</span><span class="p">,</span> 
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>            <span class="mi">12</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__use_higher_level_sleep_manager</span><span class="p">,</span> 
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="mi">13</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__low_latency_io_mode</span><span class="p">,</span> 
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="p">}</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_original_loop_class</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_idle_for</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RationalNumber</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># in seconds</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="n">events</span><span class="o">.</span><span class="n">_set_running_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="nf">_on_system_loop_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">next_event_after</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RationalNumber</span><span class="p">]):</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="k">if</span> <span class="n">next_event_after</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_idle_for</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="mf">0.001</span><span class="p">,</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">())</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_idle_for</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="mf">0.001</span><span class="p">,</span> <span class="n">next_event_after</span><span class="p">)</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>            <span class="s1">&#39;pending requests num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="p">}</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncioLoopRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus</span> <span class="kn">import</span> <span class="n">AsyncEventBusRequest</span><span class="p">,</span> <span class="n">try_send_async_event</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="c1"># throw_coro_service: ThrowCoro = self._loop.get_service_instance(ThrowCoro)</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="c1"># throw_coro_service._add_direct_request(self._waiting_coro_id, WaitingCancelled)</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="n">kill_coro_service</span><span class="p">:</span> <span class="n">KillCoro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">KillCoro</span><span class="p">)</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="n">kill_coro_service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span><span class="p">)</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span> <span class="n">WAITING_FOR_NEW_REQUESTS_EVENT</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span><span class="p">:</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="n">loop_response</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="n">exception_response</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>                <span class="n">loop_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>                <span class="n">exception_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>            
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>            <span class="k">if</span> <span class="n">loop_response</span> <span class="ow">or</span> <span class="n">exception_response</span><span class="p">:</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>                <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">loop_response</span><span class="p">,</span> <span class="n">exception_response</span><span class="p">)</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">)()</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">response</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">response</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="p">:</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">DirectResponse</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">))</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)()</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>    
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="nf">is_low_latency</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">)</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">)</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>    
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>    <span class="k">def</span> <span class="nf">_on_inherit_surrounding_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="ne">Exception</span><span class="p">]:</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="n">get_running_loop</span><span class="p">()</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>    
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>    <span class="k">def</span> <span class="nf">_on_start_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="ne">Exception</span><span class="p">]:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span><span class="p">:</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_asyncio_loop_has_run_once_method</span><span class="p">():</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>                    <span class="n">internal_loop_holding_coro_worker</span> <span class="o">=</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">CoroType</span><span class="o">.</span><span class="n">awaitable</span><span class="p">,</span> <span class="n">_internal_loop_holding_coro_run_once_based</span><span class="p">)</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>                    <span class="n">internal_loop_holding_coro_worker</span> <span class="o">=</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">CoroType</span><span class="o">.</span><span class="n">greenlet</span><span class="p">,</span> <span class="n">_internal_loop_holding_coro</span><span class="p">)</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>            <span class="k">except</span> <span class="n">ExternalAsyncioLoopAlreadyExistsError</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ex</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>            
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">internal_loop_holding_coro_worker</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">,</span> <span class="n">debug</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>            <span class="k">if</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="o">.</span><span class="n">is_background_coro</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>    
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="nf">_is_asyncio_loop_has_run_once_method</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="k">if</span> <span class="n">events</span><span class="o">.</span><span class="n">_get_running_loop</span><span class="p">()</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>            <span class="k">raise</span> <span class="n">ExternalAsyncioLoopAlreadyExistsError</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>        <span class="n">loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">new_event_loop</span><span class="p">()</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="s1">&#39;_run_once&#39;</span><span class="p">):</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>            <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                <span class="n">loop</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>    
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>    <span class="k">def</span> <span class="nf">_on_ensure_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="ne">Exception</span><span class="p">]:</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">()</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exception</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>            <span class="k">return</span> <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>        <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_inherit_surrounding_loop</span><span class="p">()</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exception</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>            <span class="k">return</span> <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_start_internal_loop</span><span class="p">(</span><span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>    <span class="k">def</span> <span class="nf">_on_set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">):</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="n">async_loop</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">()</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>    
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>    <span class="k">def</span> <span class="nf">register_await_response</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]):</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">_on_await</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">intercommunication_request</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">prevent_idle</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">()</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>        
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>        <span class="k">if</span> <span class="n">intercommunication_request</span><span class="p">:</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">awaiting_worker</span><span class="p">(</span><span class="n">asyncio_loop_instance</span><span class="p">:</span> <span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">):</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">awaitable</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>            
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>            <span class="n">asyncio_loop_instance</span><span class="o">.</span><span class="n">register_await_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">awaiting_worker</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">)</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="k">if</span> <span class="n">prevent_idle</span><span class="p">:</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>        
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>    <span class="k">def</span> <span class="nf">_on_create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio_Task</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]:</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">()</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">awaiting_wrapper</span><span class="p">(</span><span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">):</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>            <span class="k">return</span> <span class="k">await</span> <span class="n">awaitable</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="n">task</span><span class="p">:</span> <span class="n">asyncio_Task</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">awaiting_wrapper</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">)</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">task</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>    
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>    <span class="k">def</span> <span class="nf">_on__internal_loop_yield</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>    
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="nf">_on__internal_wait_for_new_requests</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_new_requests</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>    
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>    <span class="k">def</span> <span class="nf">register_new_asyncio_request</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>    
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>    <span class="k">def</span> <span class="nf">add_on_idle_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">:</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span><span class="p">)</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>    
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>    <span class="k">def</span> <span class="nf">discard_on_idle_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span><span class="p">)</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>    
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>    <span class="k">def</span> <span class="nf">_on__use_higher_level_sleep_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="kc">None</span><span class="p">],</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span> <span class="o">=</span> <span class="n">use_higher_level_sleep_manager</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="k">if</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span><span class="p">)</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">discard_on_idle_handler</span><span class="p">()</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>        
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>    <span class="k">def</span> <span class="nf">_on__low_latency_io_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">],</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        <span class="n">buff_low_latency_io_mode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span> <span class="o">&gt;</span> <span class="mi">0</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="k">if</span> <span class="n">low_latency_io_mode</span><span class="p">:</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">buff_low_latency_io_mode</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>    
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>    <span class="k">def</span> <span class="nf">_on_turn_on_loops_intercommunication</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">],</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        <span class="k">if</span> <span class="n">turn_on</span><span class="p">:</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wrong_request</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span><span class="p">:</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>            
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>        
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>    
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>    <span class="k">def</span> <span class="nf">_on_wrong_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Request</span><span class="p">:</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">args_kwargs</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_wait_intercommunication</span><span class="p">(</span><span class="n">asyncio_coro_sleep_0</span><span class="p">()))</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>            <span class="n">result</span><span class="p">:</span> <span class="n">Request</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">args_kwargs</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_wait_intercommunication</span><span class="p">(</span><span class="n">asyncio_coro_request</span><span class="p">(</span><span class="n">request</span><span class="p">)))</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>    
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="nf">inline_get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>            <span class="k">raise</span> <span class="n">AsyncioLoopWasNotSetError</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>    
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>    <span class="k">def</span> <span class="nf">inline_set_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]):</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="o">=</span> <span class="n">loop</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="o">=</span> <span class="n">exception</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>    
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>    <span class="k">def</span> <span class="nf">is_need_to_yield_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a><span class="n">AsyncioLoopRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">AsyncioLoop</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a><span class="k">def</span> <span class="nf">_internal_loop_holding_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>    <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">main_wrapper</span><span class="p">(</span><span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>        <span class="n">loop</span><span class="p">:</span> <span class="n">AbstractEventLoop</span> <span class="o">=</span> <span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">inline_set_internal_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>        <span class="k">if</span> <span class="n">interrupt_when_no_requests</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>            <span class="n">interrupt_when_no_requests</span> <span class="o">=</span> <span class="n">main_awaitable</span> <span class="ow">is</span> <span class="kc">None</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>        
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>        <span class="k">def</span> <span class="nf">on_loop_simple_yield</span><span class="p">():</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>            <span class="k">if</span> <span class="n">interrupt_when_no_requests</span> <span class="ow">and</span> <span class="n">service</span><span class="o">.</span><span class="n">is_need_to_yield_internal_loop</span><span class="p">():</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>                <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_internal_loop_yield</span><span class="p">())</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>                <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>            
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">service</span><span class="o">.</span><span class="n">need_to_stop_internal_loop</span><span class="p">:</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>                <span class="k">if</span> <span class="n">service</span><span class="o">.</span><span class="n">_idle_for</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>                    <span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="n">on_loop_simple_yield</span><span class="p">)</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>                    <span class="n">idle_for</span> <span class="o">=</span> <span class="n">service</span><span class="o">.</span><span class="n">_idle_for</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>                    <span class="n">service</span><span class="o">.</span><span class="n">_idle_for</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>                    <span class="n">loop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="n">idle_for</span><span class="p">,</span> <span class="n">on_loop_simple_yield</span><span class="p">)</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>        
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>        <span class="k">def</span> <span class="nf">on_loop_loop_yield</span><span class="p">():</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>            <span class="k">if</span> <span class="n">interrupt_when_no_requests</span> <span class="ow">and</span> <span class="n">service</span><span class="o">.</span><span class="n">is_need_to_yield_internal_loop</span><span class="p">():</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>                <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_internal_loop_yield</span><span class="p">())</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>            
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">service</span><span class="o">.</span><span class="n">need_to_stop_internal_loop</span><span class="p">:</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>                <span class="k">if</span> <span class="n">service</span><span class="o">.</span><span class="n">_idle_for</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>                    <span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="n">on_loop_loop_yield</span><span class="p">)</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>                    <span class="n">idle_for</span> <span class="o">=</span> <span class="n">service</span><span class="o">.</span><span class="n">_idle_for</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>                    <span class="n">service</span><span class="o">.</span><span class="n">_idle_for</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>                    <span class="n">loop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="n">idle_for</span><span class="p">,</span> <span class="n">on_loop_loop_yield</span><span class="p">)</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>        
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>        <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="n">on_loop_simple_yield</span><span class="p">)</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="n">on_loop_loop_yield</span><span class="p">)</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>        <span class="k">if</span> <span class="n">main_awaitable</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>            <span class="n">create_task_awaitable</span><span class="p">(</span><span class="n">main_awaitable</span><span class="p">)</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>    
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>    <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">add_on_idle_handler</span><span class="p">()</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="n">run_forever</span><span class="p">(</span><span class="n">main_wrapper</span><span class="p">(</span><span class="n">service</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">),</span> <span class="n">debug</span><span class="o">=</span><span class="n">debug</span><span class="p">)</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>        <span class="c1"># TODO: do something with exception</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">service</span><span class="o">.</span><span class="n">_on_system_loop_idle</span><span class="p">)</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>            <span class="k">pass</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">inline_set_internal_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">_internal_loop_holding_coro_run_once_based</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus</span> <span class="kn">import</span> <span class="n">AsyncEventBusRequest</span><span class="p">,</span> <span class="n">try_send_async_event</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>    <span class="kn">from</span> <span class="nn">.known_asyncio_compatible_loops</span> <span class="kn">import</span> <span class="n">prepare_loop</span><span class="p">,</span> <span class="n">restore_loop</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>    <span class="n">lyps</span><span class="p">:</span> <span class="n">LoopYieldPriorityScheduler</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">)</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>    <span class="n">umsi</span><span class="p">:</span> <span class="n">RationalNumber</span> <span class="o">=</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">()</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>    <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">main_wrapper_for_run_once</span><span class="p">(</span><span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>        <span class="n">loop</span><span class="p">:</span> <span class="n">AbstractEventLoop</span> <span class="o">=</span> <span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">inline_set_internal_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>        <span class="k">if</span> <span class="n">main_awaitable</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>            <span class="n">create_task_awaitable</span><span class="p">(</span><span class="n">main_awaitable</span><span class="p">)</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>    
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>    <span class="k">if</span> <span class="n">interrupt_when_no_requests</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>        <span class="n">interrupt_when_no_requests</span> <span class="o">=</span> <span class="n">main_awaitable</span> <span class="ow">is</span> <span class="kc">None</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>    
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>    <span class="n">main_wrapper_for_run_once_coro</span> <span class="o">=</span> <span class="n">main_wrapper_for_run_once</span><span class="p">(</span><span class="n">service</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">)</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>    
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>    <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>        <span class="k">if</span> <span class="n">events</span><span class="o">.</span><span class="n">_get_running_loop</span><span class="p">()</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>                <span class="s1">&#39;run_forever() cannot be called from a running event loop&#39;</span><span class="p">)</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">coroutines</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">main_wrapper_for_run_once_coro</span><span class="p">):</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;a coroutine was expected, got </span><span class="si">{!r}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">main_wrapper_for_run_once</span><span class="p">))</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>        <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">new_event_loop</span><span class="p">()</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">_original_loop_class</span> <span class="o">=</span> <span class="n">prepare_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>            <span class="n">events</span><span class="o">.</span><span class="n">set_event_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">set_debug</span><span class="p">(</span><span class="n">debug</span><span class="p">)</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">main_wrapper_for_run_once_coro</span><span class="p">)</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">_check_closed</span><span class="p">()</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">_check_running</span><span class="p">()</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">_set_coroutine_origin_tracking</span><span class="p">(</span><span class="n">loop</span><span class="o">.</span><span class="n">_debug</span><span class="p">)</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>            <span class="n">loop</span><span class="o">.</span><span class="n">_thread_id</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">get_ident</span><span class="p">()</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>            <span class="n">old_agen_hooks</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">get_asyncgen_hooks</span><span class="p">()</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>            <span class="n">sys</span><span class="o">.</span><span class="n">set_asyncgen_hooks</span><span class="p">(</span><span class="n">firstiter</span><span class="o">=</span><span class="n">loop</span><span class="o">.</span><span class="n">_asyncgen_firstiter_hook</span><span class="p">,</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>                                <span class="n">finalizer</span><span class="o">=</span><span class="n">loop</span><span class="o">.</span><span class="n">_asyncgen_finalizer_hook</span><span class="p">)</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>                <span class="n">events</span><span class="o">.</span><span class="n">_set_running_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>                <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>                    <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>                        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>                        <span class="k">await</span> <span class="n">ly</span><span class="p">()</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>                    <span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>                    <span class="c1"># if (not loop._ready) and (not loop._stopping) and (not loop._scheduled):</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>                    <span class="c1">#     loop.call_soon(lambda: None)</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>                    
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>                    <span class="n">loop</span><span class="o">.</span><span class="n">_run_once</span><span class="p">()</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>                    <span class="k">if</span> <span class="n">loop</span><span class="o">.</span><span class="n">_stopping</span><span class="p">:</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>                        <span class="k">break</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>                    <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">loop</span><span class="o">.</span><span class="n">_ready</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">loop</span><span class="o">.</span><span class="n">_stopping</span><span class="p">):</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>                        <span class="k">if</span> <span class="ow">not</span> <span class="n">loop</span><span class="o">.</span><span class="n">_scheduled</span><span class="p">:</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>                            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_internal_loop_yield</span><span class="p">())</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>                            <span class="k">continue</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>                        <span class="k">else</span><span class="p">:</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>                            <span class="n">when</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">_scheduled</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">_when</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>                            <span class="kn">from</span> <span class="nn">asyncio.base_events</span> <span class="kn">import</span> <span class="n">MAXIMUM_SELECT_TIMEOUT</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>                            <span class="n">timeout</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">when</span> <span class="o">-</span> <span class="n">loop</span><span class="o">.</span><span class="n">time</span><span class="p">()),</span> <span class="n">MAXIMUM_SELECT_TIMEOUT</span><span class="p">)</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>                            <span class="c1"># if get_min_sleep_interval() &lt;= timeout:</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>                            <span class="c1">#     usable_min_sleep_interval = get_usable_min_sleep_interval()</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>                            <span class="c1">#     if usable_min_sleep_interval &gt; timeout:</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>                            <span class="c1">#         timeout = usable_min_sleep_interval</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>                            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">service</span><span class="o">.</span><span class="n">low_latency_io_mode</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="mf">0.001</span> <span class="o">&lt;=</span> <span class="n">timeout</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">service</span><span class="o">.</span><span class="n">results</span><span class="p">):</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>                                <span class="n">service</span><span class="o">.</span><span class="n">new_requests_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>                                <span class="n">service</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>                                <span class="k">async</span> <span class="k">def</span> <span class="nf">waiting_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>                                    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus</span> <span class="kn">import</span> <span class="n">AsyncEventBusRequest</span><span class="p">,</span> <span class="n">try_send_async_event</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>                                    <span class="k">try</span><span class="p">:</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>                                        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>                                        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">send_event</span><span class="p">(</span><span class="n">WAITING_FOR_NEW_REQUESTS_EVENT</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>                                    <span class="k">except</span> <span class="n">WaitingCancelled</span><span class="p">:</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>                                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;AsyncIoLoop </span><span class="si">{</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">&quot;%H:%M:%S.</span><span class="si">%f</span><span class="s2">&quot;</span><span class="p">)</span><span class="si">}</span><span class="s1"> &gt;&gt; WaitingCancelled&#39;</span><span class="p">)</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>                                
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>                                <span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>                                <span class="k">try</span><span class="p">:</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>                                    <span class="c1"># TODO: reimplement it in more efficient and elegant way. Btw: Sleep currently will not cancel an event upon coro destroyed</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>                                    <span class="n">lyps_max_delay</span> <span class="o">=</span> <span class="n">lyps</span><span class="o">.</span><span class="n">max_delay</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>                                    <span class="n">new_max_timeout</span> <span class="o">=</span> <span class="n">umsi</span> <span class="k">if</span> <span class="n">lyps_max_delay</span> <span class="o">&lt;</span> <span class="n">umsi</span> <span class="k">else</span> <span class="n">lyps_max_delay</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>                                    <span class="n">new_timeout</span> <span class="o">=</span> <span class="n">timeout</span> <span class="k">if</span> <span class="n">new_max_timeout</span> <span class="o">&gt;</span> <span class="n">timeout</span> <span class="k">else</span> <span class="n">new_max_timeout</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>                                    <span class="n">waiting_coro_id</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">,</span> <span class="n">waiting_coro</span><span class="p">,</span> <span class="n">new_timeout</span><span class="p">)</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>                                    <span class="n">service</span><span class="o">.</span><span class="n">_waiting_coro_id</span> <span class="o">=</span> <span class="n">waiting_coro_id</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>                                    <span class="c1"># await i(WaitCoro, WaitCoroRequest().single(waiting_coro_id))</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>                                    <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">WAITING_FOR_NEW_REQUESTS_EVENT</span><span class="p">))</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>                                    <span class="c1"># print(f&#39;AsyncIoLoop {datetime.now().strftime(&quot;%H:%M:%S.%f&quot;)} &gt;&gt; WAITING_FOR_NEW_REQUESTS_EVENT&#39;)</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>                                <span class="k">except</span> <span class="p">(</span><span class="n">WaitingCancelled</span><span class="p">,</span> <span class="n">CoroutineNotFoundError</span><span class="p">):</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>                                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;AsyncIoLoop </span><span class="si">{</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">&quot;%H:%M:%S.</span><span class="si">%f</span><span class="s2">&quot;</span><span class="p">)</span><span class="si">}</span><span class="s1"> &gt;&gt; WaitingCancelled or CoroutineNotFoundError&#39;</span><span class="p">)</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>                                    <span class="k">pass</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>                                <span class="k">except</span><span class="p">:</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>                                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;AsyncIoLoop </span><span class="si">{</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">&quot;%H:%M:%S.</span><span class="si">%f</span><span class="s2">&quot;</span><span class="p">)</span><span class="si">}</span><span class="s1"> &gt;&gt; </span><span class="si">{</span><span class="n">get_exception</span><span class="p">()</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>                                    <span class="k">raise</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>                    <span class="k">if</span> <span class="n">interrupt_when_no_requests</span> <span class="ow">and</span> <span class="n">service</span><span class="o">.</span><span class="n">is_need_to_yield_internal_loop</span><span class="p">():</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>                        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_internal_loop_yield</span><span class="p">())</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>                        <span class="k">continue</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>            <span class="k">finally</span><span class="p">:</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>                <span class="n">loop</span><span class="o">.</span><span class="n">_stopping</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>                <span class="n">loop</span><span class="o">.</span><span class="n">_thread_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>                <span class="n">events</span><span class="o">.</span><span class="n">_set_running_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>                <span class="n">loop</span><span class="o">.</span><span class="n">_set_coroutine_origin_tracking</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>                <span class="n">sys</span><span class="o">.</span><span class="n">set_asyncgen_hooks</span><span class="p">(</span><span class="o">*</span><span class="n">old_agen_hooks</span><span class="p">)</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>            <span class="n">restore_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">service</span><span class="o">.</span><span class="n">_original_loop_class</span><span class="p">)</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>                <span class="n">cancel_all_tasks</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>                <span class="n">loop</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="n">loop</span><span class="o">.</span><span class="n">shutdown_asyncgens</span><span class="p">())</span>
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>            <span class="k">finally</span><span class="p">:</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>                <span class="n">events</span><span class="o">.</span><span class="n">set_event_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>                <span class="n">loop</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">inline_set_internal_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a><span class="k">def</span> <span class="nf">run_in_thread_pool_fast</span><span class="p">(</span><span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">function</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">task_wrapper</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">function</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>    <span class="k">return</span> <span class="n">interface</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">task_wrapper</span><span class="p">(</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>        <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">(),</span> 
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>        <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)))</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a><span class="k">def</span> <span class="nf">run_in_thread_pool</span><span class="p">(</span><span class="n">function</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>    <span class="k">return</span> <span class="n">run_in_thread_pool_fast</span><span class="p">(</span><span class="n">current_interface</span><span class="p">(),</span> <span class="n">function</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="AsyncioLoop">
                            <input id="AsyncioLoop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">AsyncioLoop</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</span>, <span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="AsyncioLoop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop-140"><a href="#AsyncioLoop-140"><span class="linenos">140</span></a><span class="k">class</span> <span class="nc">AsyncioLoop</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="AsyncioLoop-141"><a href="#AsyncioLoop-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="AsyncioLoop-142"><a href="#AsyncioLoop-142"><span class="linenos">142</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="AsyncioLoop-143"><a href="#AsyncioLoop-143"><span class="linenos">143</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-144"><a href="#AsyncioLoop-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-145"><a href="#AsyncioLoop-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroWrapperBase</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-146"><a href="#AsyncioLoop-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="AsyncioLoop-147"><a href="#AsyncioLoop-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_internal_loop</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-148"><a href="#AsyncioLoop-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-149"><a href="#AsyncioLoop-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-150"><a href="#AsyncioLoop-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_new_requests</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-151"><a href="#AsyncioLoop-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-152"><a href="#AsyncioLoop-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-153"><a href="#AsyncioLoop-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="AsyncioLoop-154"><a href="#AsyncioLoop-154"><span class="linenos">154</span></a>
</span><span id="AsyncioLoop-155"><a href="#AsyncioLoop-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="AsyncioLoop-156"><a href="#AsyncioLoop-156"><span class="linenos">156</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_inherit_surrounding_loop</span><span class="p">,</span>
</span><span id="AsyncioLoop-157"><a href="#AsyncioLoop-157"><span class="linenos">157</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_start_internal_loop</span><span class="p">,</span>
</span><span id="AsyncioLoop-158"><a href="#AsyncioLoop-158"><span class="linenos">158</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_ensure_loop</span><span class="p">,</span>
</span><span id="AsyncioLoop-159"><a href="#AsyncioLoop-159"><span class="linenos">159</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set</span><span class="p">,</span>
</span><span id="AsyncioLoop-160"><a href="#AsyncioLoop-160"><span class="linenos">160</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="AsyncioLoop-161"><a href="#AsyncioLoop-161"><span class="linenos">161</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="AsyncioLoop-162"><a href="#AsyncioLoop-162"><span class="linenos">162</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_create_task</span><span class="p">,</span>
</span><span id="AsyncioLoop-163"><a href="#AsyncioLoop-163"><span class="linenos">163</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__internal_loop_yield</span><span class="p">,</span>
</span><span id="AsyncioLoop-164"><a href="#AsyncioLoop-164"><span class="linenos">164</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_turn_on_loops_intercommunication</span><span class="p">,</span>
</span><span id="AsyncioLoop-165"><a href="#AsyncioLoop-165"><span class="linenos">165</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="AsyncioLoop-166"><a href="#AsyncioLoop-166"><span class="linenos">166</span></a>            <span class="mi">10</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="AsyncioLoop-167"><a href="#AsyncioLoop-167"><span class="linenos">167</span></a>            <span class="mi">11</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__internal_wait_for_new_requests</span><span class="p">,</span> 
</span><span id="AsyncioLoop-168"><a href="#AsyncioLoop-168"><span class="linenos">168</span></a>            <span class="mi">12</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__use_higher_level_sleep_manager</span><span class="p">,</span> 
</span><span id="AsyncioLoop-169"><a href="#AsyncioLoop-169"><span class="linenos">169</span></a>            <span class="mi">13</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__low_latency_io_mode</span><span class="p">,</span> 
</span><span id="AsyncioLoop-170"><a href="#AsyncioLoop-170"><span class="linenos">170</span></a>        <span class="p">}</span>
</span><span id="AsyncioLoop-171"><a href="#AsyncioLoop-171"><span class="linenos">171</span></a>        
</span><span id="AsyncioLoop-172"><a href="#AsyncioLoop-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AsyncioLoop-173"><a href="#AsyncioLoop-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AsyncioLoop-174"><a href="#AsyncioLoop-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="AsyncioLoop-175"><a href="#AsyncioLoop-175"><span class="linenos">175</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="AsyncioLoop-176"><a href="#AsyncioLoop-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-177"><a href="#AsyncioLoop-177"><span class="linenos">177</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_original_loop_class</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-178"><a href="#AsyncioLoop-178"><span class="linenos">178</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_idle_for</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RationalNumber</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># in seconds</span>
</span><span id="AsyncioLoop-179"><a href="#AsyncioLoop-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-180"><a href="#AsyncioLoop-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-181"><a href="#AsyncioLoop-181"><span class="linenos">181</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AsyncioLoop-182"><a href="#AsyncioLoop-182"><span class="linenos">182</span></a>    
</span><span id="AsyncioLoop-183"><a href="#AsyncioLoop-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AsyncioLoop-184"><a href="#AsyncioLoop-184"><span class="linenos">184</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-185"><a href="#AsyncioLoop-185"><span class="linenos">185</span></a>            <span class="n">events</span><span class="o">.</span><span class="n">_set_running_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="AsyncioLoop-186"><a href="#AsyncioLoop-186"><span class="linenos">186</span></a>
</span><span id="AsyncioLoop-187"><a href="#AsyncioLoop-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">_on_system_loop_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">next_event_after</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RationalNumber</span><span class="p">]):</span>
</span><span id="AsyncioLoop-188"><a href="#AsyncioLoop-188"><span class="linenos">188</span></a>        <span class="k">if</span> <span class="n">next_event_after</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-189"><a href="#AsyncioLoop-189"><span class="linenos">189</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_idle_for</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="mf">0.001</span><span class="p">,</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">())</span>
</span><span id="AsyncioLoop-190"><a href="#AsyncioLoop-190"><span class="linenos">190</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-191"><a href="#AsyncioLoop-191"><span class="linenos">191</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_idle_for</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="mf">0.001</span><span class="p">,</span> <span class="n">next_event_after</span><span class="p">)</span>
</span><span id="AsyncioLoop-192"><a href="#AsyncioLoop-192"><span class="linenos">192</span></a>
</span><span id="AsyncioLoop-193"><a href="#AsyncioLoop-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="AsyncioLoop-194"><a href="#AsyncioLoop-194"><span class="linenos">194</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="AsyncioLoop-195"><a href="#AsyncioLoop-195"><span class="linenos">195</span></a>            <span class="s1">&#39;pending requests num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span>
</span><span id="AsyncioLoop-196"><a href="#AsyncioLoop-196"><span class="linenos">196</span></a>        <span class="p">}</span>
</span><span id="AsyncioLoop-197"><a href="#AsyncioLoop-197"><span class="linenos">197</span></a>
</span><span id="AsyncioLoop-198"><a href="#AsyncioLoop-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="AsyncioLoop-199"><a href="#AsyncioLoop-199"><span class="linenos">199</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncioLoopRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="AsyncioLoop-200"><a href="#AsyncioLoop-200"><span class="linenos">200</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-201"><a href="#AsyncioLoop-201"><span class="linenos">201</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="AsyncioLoop-202"><a href="#AsyncioLoop-202"><span class="linenos">202</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-203"><a href="#AsyncioLoop-203"><span class="linenos">203</span></a>
</span><span id="AsyncioLoop-204"><a href="#AsyncioLoop-204"><span class="linenos">204</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AsyncioLoop-205"><a href="#AsyncioLoop-205"><span class="linenos">205</span></a>        <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus</span> <span class="kn">import</span> <span class="n">AsyncEventBusRequest</span><span class="p">,</span> <span class="n">try_send_async_event</span>
</span><span id="AsyncioLoop-206"><a href="#AsyncioLoop-206"><span class="linenos">206</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span>
</span><span id="AsyncioLoop-207"><a href="#AsyncioLoop-207"><span class="linenos">207</span></a>            <span class="c1"># throw_coro_service: ThrowCoro = self._loop.get_service_instance(ThrowCoro)</span>
</span><span id="AsyncioLoop-208"><a href="#AsyncioLoop-208"><span class="linenos">208</span></a>            <span class="c1"># throw_coro_service._add_direct_request(self._waiting_coro_id, WaitingCancelled)</span>
</span><span id="AsyncioLoop-209"><a href="#AsyncioLoop-209"><span class="linenos">209</span></a>            <span class="n">kill_coro_service</span><span class="p">:</span> <span class="n">KillCoro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">KillCoro</span><span class="p">)</span>
</span><span id="AsyncioLoop-210"><a href="#AsyncioLoop-210"><span class="linenos">210</span></a>            <span class="n">kill_coro_service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop-211"><a href="#AsyncioLoop-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-212"><a href="#AsyncioLoop-212"><span class="linenos">212</span></a>            <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span> <span class="n">WAITING_FOR_NEW_REQUESTS_EVENT</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="AsyncioLoop-213"><a href="#AsyncioLoop-213"><span class="linenos">213</span></a>
</span><span id="AsyncioLoop-214"><a href="#AsyncioLoop-214"><span class="linenos">214</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span><span class="p">:</span>
</span><span id="AsyncioLoop-215"><a href="#AsyncioLoop-215"><span class="linenos">215</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span>
</span><span id="AsyncioLoop-216"><a href="#AsyncioLoop-216"><span class="linenos">216</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="AsyncioLoop-217"><a href="#AsyncioLoop-217"><span class="linenos">217</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-218"><a href="#AsyncioLoop-218"><span class="linenos">218</span></a>
</span><span id="AsyncioLoop-219"><a href="#AsyncioLoop-219"><span class="linenos">219</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span>
</span><span id="AsyncioLoop-220"><a href="#AsyncioLoop-220"><span class="linenos">220</span></a>            <span class="n">loop_response</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-221"><a href="#AsyncioLoop-221"><span class="linenos">221</span></a>            <span class="n">exception_response</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-222"><a href="#AsyncioLoop-222"><span class="linenos">222</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-223"><a href="#AsyncioLoop-223"><span class="linenos">223</span></a>                <span class="n">loop_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span>
</span><span id="AsyncioLoop-224"><a href="#AsyncioLoop-224"><span class="linenos">224</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-225"><a href="#AsyncioLoop-225"><span class="linenos">225</span></a>                <span class="n">exception_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span>
</span><span id="AsyncioLoop-226"><a href="#AsyncioLoop-226"><span class="linenos">226</span></a>            
</span><span id="AsyncioLoop-227"><a href="#AsyncioLoop-227"><span class="linenos">227</span></a>            <span class="k">if</span> <span class="n">loop_response</span> <span class="ow">or</span> <span class="n">exception_response</span><span class="p">:</span>
</span><span id="AsyncioLoop-228"><a href="#AsyncioLoop-228"><span class="linenos">228</span></a>                <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span>
</span><span id="AsyncioLoop-229"><a href="#AsyncioLoop-229"><span class="linenos">229</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">loop_response</span><span class="p">,</span> <span class="n">exception_response</span><span class="p">)</span>
</span><span id="AsyncioLoop-230"><a href="#AsyncioLoop-230"><span class="linenos">230</span></a>
</span><span id="AsyncioLoop-231"><a href="#AsyncioLoop-231"><span class="linenos">231</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">)()</span>
</span><span id="AsyncioLoop-232"><a href="#AsyncioLoop-232"><span class="linenos">232</span></a>
</span><span id="AsyncioLoop-233"><a href="#AsyncioLoop-233"><span class="linenos">233</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">response</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="AsyncioLoop-234"><a href="#AsyncioLoop-234"><span class="linenos">234</span></a>            <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">response</span>
</span><span id="AsyncioLoop-235"><a href="#AsyncioLoop-235"><span class="linenos">235</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="p">:</span>
</span><span id="AsyncioLoop-236"><a href="#AsyncioLoop-236"><span class="linenos">236</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop-237"><a href="#AsyncioLoop-237"><span class="linenos">237</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">DirectResponse</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">))</span>
</span><span id="AsyncioLoop-238"><a href="#AsyncioLoop-238"><span class="linenos">238</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-239"><a href="#AsyncioLoop-239"><span class="linenos">239</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="AsyncioLoop-240"><a href="#AsyncioLoop-240"><span class="linenos">240</span></a>        
</span><span id="AsyncioLoop-241"><a href="#AsyncioLoop-241"><span class="linenos">241</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)</span>
</span><span id="AsyncioLoop-242"><a href="#AsyncioLoop-242"><span class="linenos">242</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)()</span>
</span><span id="AsyncioLoop-243"><a href="#AsyncioLoop-243"><span class="linenos">243</span></a>        
</span><span id="AsyncioLoop-244"><a href="#AsyncioLoop-244"><span class="linenos">244</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="p">:</span>
</span><span id="AsyncioLoop-245"><a href="#AsyncioLoop-245"><span class="linenos">245</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="AsyncioLoop-246"><a href="#AsyncioLoop-246"><span class="linenos">246</span></a>    
</span><span id="AsyncioLoop-247"><a href="#AsyncioLoop-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="nf">is_low_latency</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="AsyncioLoop-248"><a href="#AsyncioLoop-248"><span class="linenos">248</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="AsyncioLoop-249"><a href="#AsyncioLoop-249"><span class="linenos">249</span></a>
</span><span id="AsyncioLoop-250"><a href="#AsyncioLoop-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="AsyncioLoop-251"><a href="#AsyncioLoop-251"><span class="linenos">251</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">)</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">)</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)</span>
</span><span id="AsyncioLoop-252"><a href="#AsyncioLoop-252"><span class="linenos">252</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="AsyncioLoop-253"><a href="#AsyncioLoop-253"><span class="linenos">253</span></a>    
</span><span id="AsyncioLoop-254"><a href="#AsyncioLoop-254"><span class="linenos">254</span></a>    <span class="k">def</span> <span class="nf">_on_inherit_surrounding_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="ne">Exception</span><span class="p">]:</span>
</span><span id="AsyncioLoop-255"><a href="#AsyncioLoop-255"><span class="linenos">255</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-256"><a href="#AsyncioLoop-256"><span class="linenos">256</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="AsyncioLoop-257"><a href="#AsyncioLoop-257"><span class="linenos">257</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="n">get_running_loop</span><span class="p">()</span>
</span><span id="AsyncioLoop-258"><a href="#AsyncioLoop-258"><span class="linenos">258</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="AsyncioLoop-259"><a href="#AsyncioLoop-259"><span class="linenos">259</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="AsyncioLoop-260"><a href="#AsyncioLoop-260"><span class="linenos">260</span></a>
</span><span id="AsyncioLoop-261"><a href="#AsyncioLoop-261"><span class="linenos">261</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="AsyncioLoop-262"><a href="#AsyncioLoop-262"><span class="linenos">262</span></a>    
</span><span id="AsyncioLoop-263"><a href="#AsyncioLoop-263"><span class="linenos">263</span></a>    <span class="k">def</span> <span class="nf">_on_start_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="ne">Exception</span><span class="p">]:</span>
</span><span id="AsyncioLoop-264"><a href="#AsyncioLoop-264"><span class="linenos">264</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span><span class="p">:</span>
</span><span id="AsyncioLoop-265"><a href="#AsyncioLoop-265"><span class="linenos">265</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span>
</span><span id="AsyncioLoop-266"><a href="#AsyncioLoop-266"><span class="linenos">266</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-267"><a href="#AsyncioLoop-267"><span class="linenos">267</span></a>        
</span><span id="AsyncioLoop-268"><a href="#AsyncioLoop-268"><span class="linenos">268</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="AsyncioLoop-269"><a href="#AsyncioLoop-269"><span class="linenos">269</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop-270"><a href="#AsyncioLoop-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-271"><a href="#AsyncioLoop-271"><span class="linenos">271</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-272"><a href="#AsyncioLoop-272"><span class="linenos">272</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-273"><a href="#AsyncioLoop-273"><span class="linenos">273</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="AsyncioLoop-274"><a href="#AsyncioLoop-274"><span class="linenos">274</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_asyncio_loop_has_run_once_method</span><span class="p">():</span>
</span><span id="AsyncioLoop-275"><a href="#AsyncioLoop-275"><span class="linenos">275</span></a>                    <span class="n">internal_loop_holding_coro_worker</span> <span class="o">=</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">CoroType</span><span class="o">.</span><span class="n">awaitable</span><span class="p">,</span> <span class="n">_internal_loop_holding_coro_run_once_based</span><span class="p">)</span>
</span><span id="AsyncioLoop-276"><a href="#AsyncioLoop-276"><span class="linenos">276</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-277"><a href="#AsyncioLoop-277"><span class="linenos">277</span></a>                    <span class="n">internal_loop_holding_coro_worker</span> <span class="o">=</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">CoroType</span><span class="o">.</span><span class="n">greenlet</span><span class="p">,</span> <span class="n">_internal_loop_holding_coro</span><span class="p">)</span>
</span><span id="AsyncioLoop-278"><a href="#AsyncioLoop-278"><span class="linenos">278</span></a>            <span class="k">except</span> <span class="n">ExternalAsyncioLoopAlreadyExistsError</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="AsyncioLoop-279"><a href="#AsyncioLoop-279"><span class="linenos">279</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ex</span>
</span><span id="AsyncioLoop-280"><a href="#AsyncioLoop-280"><span class="linenos">280</span></a>            
</span><span id="AsyncioLoop-281"><a href="#AsyncioLoop-281"><span class="linenos">281</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">internal_loop_holding_coro_worker</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">,</span> <span class="n">debug</span><span class="p">)</span>
</span><span id="AsyncioLoop-282"><a href="#AsyncioLoop-282"><span class="linenos">282</span></a>            <span class="k">if</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span>
</span><span id="AsyncioLoop-283"><a href="#AsyncioLoop-283"><span class="linenos">283</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="o">.</span><span class="n">is_background_coro</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AsyncioLoop-284"><a href="#AsyncioLoop-284"><span class="linenos">284</span></a>
</span><span id="AsyncioLoop-285"><a href="#AsyncioLoop-285"><span class="linenos">285</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-286"><a href="#AsyncioLoop-286"><span class="linenos">286</span></a>    
</span><span id="AsyncioLoop-287"><a href="#AsyncioLoop-287"><span class="linenos">287</span></a>    <span class="k">def</span> <span class="nf">_is_asyncio_loop_has_run_once_method</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="AsyncioLoop-288"><a href="#AsyncioLoop-288"><span class="linenos">288</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-289"><a href="#AsyncioLoop-289"><span class="linenos">289</span></a>        <span class="k">if</span> <span class="n">events</span><span class="o">.</span><span class="n">_get_running_loop</span><span class="p">()</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-290"><a href="#AsyncioLoop-290"><span class="linenos">290</span></a>            <span class="k">raise</span> <span class="n">ExternalAsyncioLoopAlreadyExistsError</span>
</span><span id="AsyncioLoop-291"><a href="#AsyncioLoop-291"><span class="linenos">291</span></a>
</span><span id="AsyncioLoop-292"><a href="#AsyncioLoop-292"><span class="linenos">292</span></a>        <span class="n">loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-293"><a href="#AsyncioLoop-293"><span class="linenos">293</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="AsyncioLoop-294"><a href="#AsyncioLoop-294"><span class="linenos">294</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">new_event_loop</span><span class="p">()</span>
</span><span id="AsyncioLoop-295"><a href="#AsyncioLoop-295"><span class="linenos">295</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="s1">&#39;_run_once&#39;</span><span class="p">):</span>
</span><span id="AsyncioLoop-296"><a href="#AsyncioLoop-296"><span class="linenos">296</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AsyncioLoop-297"><a href="#AsyncioLoop-297"><span class="linenos">297</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="AsyncioLoop-298"><a href="#AsyncioLoop-298"><span class="linenos">298</span></a>            <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-299"><a href="#AsyncioLoop-299"><span class="linenos">299</span></a>                <span class="n">loop</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="AsyncioLoop-300"><a href="#AsyncioLoop-300"><span class="linenos">300</span></a>        
</span><span id="AsyncioLoop-301"><a href="#AsyncioLoop-301"><span class="linenos">301</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="AsyncioLoop-302"><a href="#AsyncioLoop-302"><span class="linenos">302</span></a>    
</span><span id="AsyncioLoop-303"><a href="#AsyncioLoop-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="nf">_on_ensure_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="ne">Exception</span><span class="p">]:</span>
</span><span id="AsyncioLoop-304"><a href="#AsyncioLoop-304"><span class="linenos">304</span></a>        <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">()</span>
</span><span id="AsyncioLoop-305"><a href="#AsyncioLoop-305"><span class="linenos">305</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exception</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="AsyncioLoop-306"><a href="#AsyncioLoop-306"><span class="linenos">306</span></a>            <span class="k">return</span> <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="AsyncioLoop-307"><a href="#AsyncioLoop-307"><span class="linenos">307</span></a>
</span><span id="AsyncioLoop-308"><a href="#AsyncioLoop-308"><span class="linenos">308</span></a>        <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_inherit_surrounding_loop</span><span class="p">()</span>
</span><span id="AsyncioLoop-309"><a href="#AsyncioLoop-309"><span class="linenos">309</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exception</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="AsyncioLoop-310"><a href="#AsyncioLoop-310"><span class="linenos">310</span></a>            <span class="k">return</span> <span class="n">result_exists</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="AsyncioLoop-311"><a href="#AsyncioLoop-311"><span class="linenos">311</span></a>        
</span><span id="AsyncioLoop-312"><a href="#AsyncioLoop-312"><span class="linenos">312</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_start_internal_loop</span><span class="p">(</span><span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">)</span>
</span><span id="AsyncioLoop-313"><a href="#AsyncioLoop-313"><span class="linenos">313</span></a>
</span><span id="AsyncioLoop-314"><a href="#AsyncioLoop-314"><span class="linenos">314</span></a>    <span class="k">def</span> <span class="nf">_on_set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">):</span>
</span><span id="AsyncioLoop-315"><a href="#AsyncioLoop-315"><span class="linenos">315</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="n">async_loop</span>
</span><span id="AsyncioLoop-316"><a href="#AsyncioLoop-316"><span class="linenos">316</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-317"><a href="#AsyncioLoop-317"><span class="linenos">317</span></a>
</span><span id="AsyncioLoop-318"><a href="#AsyncioLoop-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AsyncioLoop-319"><a href="#AsyncioLoop-319"><span class="linenos">319</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-320"><a href="#AsyncioLoop-320"><span class="linenos">320</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">()</span>
</span><span id="AsyncioLoop-321"><a href="#AsyncioLoop-321"><span class="linenos">321</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-322"><a href="#AsyncioLoop-322"><span class="linenos">322</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-323"><a href="#AsyncioLoop-323"><span class="linenos">323</span></a>        
</span><span id="AsyncioLoop-324"><a href="#AsyncioLoop-324"><span class="linenos">324</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="AsyncioLoop-325"><a href="#AsyncioLoop-325"><span class="linenos">325</span></a>    
</span><span id="AsyncioLoop-326"><a href="#AsyncioLoop-326"><span class="linenos">326</span></a>    <span class="k">def</span> <span class="nf">register_await_response</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]):</span>
</span><span id="AsyncioLoop-327"><a href="#AsyncioLoop-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="AsyncioLoop-328"><a href="#AsyncioLoop-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop-329"><a href="#AsyncioLoop-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="AsyncioLoop-330"><a href="#AsyncioLoop-330"><span class="linenos">330</span></a>
</span><span id="AsyncioLoop-331"><a href="#AsyncioLoop-331"><span class="linenos">331</span></a>    <span class="k">def</span> <span class="nf">_on_await</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">intercommunication_request</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">prevent_idle</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]:</span>
</span><span id="AsyncioLoop-332"><a href="#AsyncioLoop-332"><span class="linenos">332</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-333"><a href="#AsyncioLoop-333"><span class="linenos">333</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">()</span>
</span><span id="AsyncioLoop-334"><a href="#AsyncioLoop-334"><span class="linenos">334</span></a>        
</span><span id="AsyncioLoop-335"><a href="#AsyncioLoop-335"><span class="linenos">335</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="AsyncioLoop-336"><a href="#AsyncioLoop-336"><span class="linenos">336</span></a>        <span class="k">if</span> <span class="n">intercommunication_request</span><span class="p">:</span>
</span><span id="AsyncioLoop-337"><a href="#AsyncioLoop-337"><span class="linenos">337</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop-338"><a href="#AsyncioLoop-338"><span class="linenos">338</span></a>        
</span><span id="AsyncioLoop-339"><a href="#AsyncioLoop-339"><span class="linenos">339</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">awaiting_worker</span><span class="p">(</span><span class="n">asyncio_loop_instance</span><span class="p">:</span> <span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">):</span>
</span><span id="AsyncioLoop-340"><a href="#AsyncioLoop-340"><span class="linenos">340</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-341"><a href="#AsyncioLoop-341"><span class="linenos">341</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-342"><a href="#AsyncioLoop-342"><span class="linenos">342</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="AsyncioLoop-343"><a href="#AsyncioLoop-343"><span class="linenos">343</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">awaitable</span>
</span><span id="AsyncioLoop-344"><a href="#AsyncioLoop-344"><span class="linenos">344</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="AsyncioLoop-345"><a href="#AsyncioLoop-345"><span class="linenos">345</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="AsyncioLoop-346"><a href="#AsyncioLoop-346"><span class="linenos">346</span></a>            
</span><span id="AsyncioLoop-347"><a href="#AsyncioLoop-347"><span class="linenos">347</span></a>            <span class="n">asyncio_loop_instance</span><span class="o">.</span><span class="n">register_await_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="AsyncioLoop-348"><a href="#AsyncioLoop-348"><span class="linenos">348</span></a>        
</span><span id="AsyncioLoop-349"><a href="#AsyncioLoop-349"><span class="linenos">349</span></a>        <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">awaiting_worker</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">)</span>
</span><span id="AsyncioLoop-350"><a href="#AsyncioLoop-350"><span class="linenos">350</span></a>        
</span><span id="AsyncioLoop-351"><a href="#AsyncioLoop-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="AsyncioLoop-352"><a href="#AsyncioLoop-352"><span class="linenos">352</span></a>        <span class="k">if</span> <span class="n">prevent_idle</span><span class="p">:</span>
</span><span id="AsyncioLoop-353"><a href="#AsyncioLoop-353"><span class="linenos">353</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop-354"><a href="#AsyncioLoop-354"><span class="linenos">354</span></a>        
</span><span id="AsyncioLoop-355"><a href="#AsyncioLoop-355"><span class="linenos">355</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="AsyncioLoop-356"><a href="#AsyncioLoop-356"><span class="linenos">356</span></a>        
</span><span id="AsyncioLoop-357"><a href="#AsyncioLoop-357"><span class="linenos">357</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-358"><a href="#AsyncioLoop-358"><span class="linenos">358</span></a>
</span><span id="AsyncioLoop-359"><a href="#AsyncioLoop-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="nf">_on_create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio_Task</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]:</span>
</span><span id="AsyncioLoop-360"><a href="#AsyncioLoop-360"><span class="linenos">360</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-361"><a href="#AsyncioLoop-361"><span class="linenos">361</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">()</span>
</span><span id="AsyncioLoop-362"><a href="#AsyncioLoop-362"><span class="linenos">362</span></a>
</span><span id="AsyncioLoop-363"><a href="#AsyncioLoop-363"><span class="linenos">363</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">awaiting_wrapper</span><span class="p">(</span><span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">):</span>
</span><span id="AsyncioLoop-364"><a href="#AsyncioLoop-364"><span class="linenos">364</span></a>            <span class="k">return</span> <span class="k">await</span> <span class="n">awaitable</span>
</span><span id="AsyncioLoop-365"><a href="#AsyncioLoop-365"><span class="linenos">365</span></a>
</span><span id="AsyncioLoop-366"><a href="#AsyncioLoop-366"><span class="linenos">366</span></a>        <span class="n">task</span><span class="p">:</span> <span class="n">asyncio_Task</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">,</span> <span class="n">awaiting_wrapper</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">)</span>
</span><span id="AsyncioLoop-367"><a href="#AsyncioLoop-367"><span class="linenos">367</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">task</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-368"><a href="#AsyncioLoop-368"><span class="linenos">368</span></a>    
</span><span id="AsyncioLoop-369"><a href="#AsyncioLoop-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">_on__internal_loop_yield</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="AsyncioLoop-370"><a href="#AsyncioLoop-370"><span class="linenos">370</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span>
</span><span id="AsyncioLoop-371"><a href="#AsyncioLoop-371"><span class="linenos">371</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-372"><a href="#AsyncioLoop-372"><span class="linenos">372</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-373"><a href="#AsyncioLoop-373"><span class="linenos">373</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AsyncioLoop-374"><a href="#AsyncioLoop-374"><span class="linenos">374</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-375"><a href="#AsyncioLoop-375"><span class="linenos">375</span></a>    
</span><span id="AsyncioLoop-376"><a href="#AsyncioLoop-376"><span class="linenos">376</span></a>    <span class="k">def</span> <span class="nf">_on__internal_wait_for_new_requests</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="AsyncioLoop-377"><a href="#AsyncioLoop-377"><span class="linenos">377</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span>
</span><span id="AsyncioLoop-378"><a href="#AsyncioLoop-378"><span class="linenos">378</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-379"><a href="#AsyncioLoop-379"><span class="linenos">379</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-380"><a href="#AsyncioLoop-380"><span class="linenos">380</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_new_requests</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AsyncioLoop-381"><a href="#AsyncioLoop-381"><span class="linenos">381</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-382"><a href="#AsyncioLoop-382"><span class="linenos">382</span></a>    
</span><span id="AsyncioLoop-383"><a href="#AsyncioLoop-383"><span class="linenos">383</span></a>    <span class="k">def</span> <span class="nf">register_new_asyncio_request</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-384"><a href="#AsyncioLoop-384"><span class="linenos">384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="AsyncioLoop-385"><a href="#AsyncioLoop-385"><span class="linenos">385</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="AsyncioLoop-386"><a href="#AsyncioLoop-386"><span class="linenos">386</span></a>    
</span><span id="AsyncioLoop-387"><a href="#AsyncioLoop-387"><span class="linenos">387</span></a>    <span class="k">def</span> <span class="nf">add_on_idle_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-388"><a href="#AsyncioLoop-388"><span class="linenos">388</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">:</span>
</span><span id="AsyncioLoop-389"><a href="#AsyncioLoop-389"><span class="linenos">389</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span>
</span><span id="AsyncioLoop-390"><a href="#AsyncioLoop-390"><span class="linenos">390</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span><span class="p">)</span>
</span><span id="AsyncioLoop-391"><a href="#AsyncioLoop-391"><span class="linenos">391</span></a>    
</span><span id="AsyncioLoop-392"><a href="#AsyncioLoop-392"><span class="linenos">392</span></a>    <span class="k">def</span> <span class="nf">discard_on_idle_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-393"><a href="#AsyncioLoop-393"><span class="linenos">393</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span><span class="p">)</span>
</span><span id="AsyncioLoop-394"><a href="#AsyncioLoop-394"><span class="linenos">394</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-395"><a href="#AsyncioLoop-395"><span class="linenos">395</span></a>    
</span><span id="AsyncioLoop-396"><a href="#AsyncioLoop-396"><span class="linenos">396</span></a>    <span class="k">def</span> <span class="nf">_on__use_higher_level_sleep_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="kc">None</span><span class="p">],</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="AsyncioLoop-397"><a href="#AsyncioLoop-397"><span class="linenos">397</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span> <span class="o">=</span> <span class="n">use_higher_level_sleep_manager</span>
</span><span id="AsyncioLoop-398"><a href="#AsyncioLoop-398"><span class="linenos">398</span></a>        <span class="k">if</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">:</span>
</span><span id="AsyncioLoop-399"><a href="#AsyncioLoop-399"><span class="linenos">399</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-400"><a href="#AsyncioLoop-400"><span class="linenos">400</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span><span class="p">)</span>
</span><span id="AsyncioLoop-401"><a href="#AsyncioLoop-401"><span class="linenos">401</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-402"><a href="#AsyncioLoop-402"><span class="linenos">402</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">discard_on_idle_handler</span><span class="p">()</span>
</span><span id="AsyncioLoop-403"><a href="#AsyncioLoop-403"><span class="linenos">403</span></a>        
</span><span id="AsyncioLoop-404"><a href="#AsyncioLoop-404"><span class="linenos">404</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-405"><a href="#AsyncioLoop-405"><span class="linenos">405</span></a>
</span><span id="AsyncioLoop-406"><a href="#AsyncioLoop-406"><span class="linenos">406</span></a>    <span class="k">def</span> <span class="nf">_on__low_latency_io_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">],</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="AsyncioLoop-407"><a href="#AsyncioLoop-407"><span class="linenos">407</span></a>        <span class="n">buff_low_latency_io_mode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span> <span class="o">&gt;</span> <span class="mi">0</span>
</span><span id="AsyncioLoop-408"><a href="#AsyncioLoop-408"><span class="linenos">408</span></a>        <span class="k">if</span> <span class="n">low_latency_io_mode</span><span class="p">:</span>
</span><span id="AsyncioLoop-409"><a href="#AsyncioLoop-409"><span class="linenos">409</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="AsyncioLoop-410"><a href="#AsyncioLoop-410"><span class="linenos">410</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-411"><a href="#AsyncioLoop-411"><span class="linenos">411</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="AsyncioLoop-412"><a href="#AsyncioLoop-412"><span class="linenos">412</span></a>        
</span><span id="AsyncioLoop-413"><a href="#AsyncioLoop-413"><span class="linenos">413</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">buff_low_latency_io_mode</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-414"><a href="#AsyncioLoop-414"><span class="linenos">414</span></a>    
</span><span id="AsyncioLoop-415"><a href="#AsyncioLoop-415"><span class="linenos">415</span></a>    <span class="k">def</span> <span class="nf">_on_turn_on_loops_intercommunication</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">],</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="AsyncioLoop-416"><a href="#AsyncioLoop-416"><span class="linenos">416</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span>
</span><span id="AsyncioLoop-417"><a href="#AsyncioLoop-417"><span class="linenos">417</span></a>        <span class="k">if</span> <span class="n">turn_on</span><span class="p">:</span>
</span><span id="AsyncioLoop-418"><a href="#AsyncioLoop-418"><span class="linenos">418</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span>
</span><span id="AsyncioLoop-419"><a href="#AsyncioLoop-419"><span class="linenos">419</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AsyncioLoop-420"><a href="#AsyncioLoop-420"><span class="linenos">420</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wrong_request</span>
</span><span id="AsyncioLoop-421"><a href="#AsyncioLoop-421"><span class="linenos">421</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-422"><a href="#AsyncioLoop-422"><span class="linenos">422</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span><span class="p">:</span>
</span><span id="AsyncioLoop-423"><a href="#AsyncioLoop-423"><span class="linenos">423</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_wrong_request</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span>
</span><span id="AsyncioLoop-424"><a href="#AsyncioLoop-424"><span class="linenos">424</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop-425"><a href="#AsyncioLoop-425"><span class="linenos">425</span></a>            
</span><span id="AsyncioLoop-426"><a href="#AsyncioLoop-426"><span class="linenos">426</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-427"><a href="#AsyncioLoop-427"><span class="linenos">427</span></a>        
</span><span id="AsyncioLoop-428"><a href="#AsyncioLoop-428"><span class="linenos">428</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="AsyncioLoop-429"><a href="#AsyncioLoop-429"><span class="linenos">429</span></a>    
</span><span id="AsyncioLoop-430"><a href="#AsyncioLoop-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">_on_wrong_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Request</span><span class="p">:</span>
</span><span id="AsyncioLoop-431"><a href="#AsyncioLoop-431"><span class="linenos">431</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-432"><a href="#AsyncioLoop-432"><span class="linenos">432</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">args_kwargs</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_wait_intercommunication</span><span class="p">(</span><span class="n">asyncio_coro_sleep_0</span><span class="p">()))</span>
</span><span id="AsyncioLoop-433"><a href="#AsyncioLoop-433"><span class="linenos">433</span></a>            <span class="n">result</span><span class="p">:</span> <span class="n">Request</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="AsyncioLoop-434"><a href="#AsyncioLoop-434"><span class="linenos">434</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-435"><a href="#AsyncioLoop-435"><span class="linenos">435</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">args_kwargs</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">_wait_intercommunication</span><span class="p">(</span><span class="n">asyncio_coro_request</span><span class="p">(</span><span class="n">request</span><span class="p">)))</span>
</span><span id="AsyncioLoop-436"><a href="#AsyncioLoop-436"><span class="linenos">436</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="AsyncioLoop-437"><a href="#AsyncioLoop-437"><span class="linenos">437</span></a>
</span><span id="AsyncioLoop-438"><a href="#AsyncioLoop-438"><span class="linenos">438</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="AsyncioLoop-439"><a href="#AsyncioLoop-439"><span class="linenos">439</span></a>    
</span><span id="AsyncioLoop-440"><a href="#AsyncioLoop-440"><span class="linenos">440</span></a>    <span class="k">def</span> <span class="nf">inline_get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AsyncioLoop-441"><a href="#AsyncioLoop-441"><span class="linenos">441</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop-442"><a href="#AsyncioLoop-442"><span class="linenos">442</span></a>            <span class="k">raise</span> <span class="n">AsyncioLoopWasNotSetError</span>
</span><span id="AsyncioLoop-443"><a href="#AsyncioLoop-443"><span class="linenos">443</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop-444"><a href="#AsyncioLoop-444"><span class="linenos">444</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span>
</span><span id="AsyncioLoop-445"><a href="#AsyncioLoop-445"><span class="linenos">445</span></a>    
</span><span id="AsyncioLoop-446"><a href="#AsyncioLoop-446"><span class="linenos">446</span></a>    <span class="k">def</span> <span class="nf">inline_set_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]):</span>
</span><span id="AsyncioLoop-447"><a href="#AsyncioLoop-447"><span class="linenos">447</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="o">=</span> <span class="n">loop</span>
</span><span id="AsyncioLoop-448"><a href="#AsyncioLoop-448"><span class="linenos">448</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="o">=</span> <span class="n">exception</span>
</span><span id="AsyncioLoop-449"><a href="#AsyncioLoop-449"><span class="linenos">449</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="AsyncioLoop-450"><a href="#AsyncioLoop-450"><span class="linenos">450</span></a>    
</span><span id="AsyncioLoop-451"><a href="#AsyncioLoop-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">is_need_to_yield_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="AsyncioLoop-452"><a href="#AsyncioLoop-452"><span class="linenos">452</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span>
</span></pre></div>


    

                            <div id="AsyncioLoop.__init__" class="classattr">
                                        <input id="AsyncioLoop.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">AsyncioLoop</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="AsyncioLoop.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.__init__-141"><a href="#AsyncioLoop.__init__-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="AsyncioLoop.__init__-142"><a href="#AsyncioLoop.__init__-142"><span class="linenos">142</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="AsyncioLoop.__init__-143"><a href="#AsyncioLoop.__init__-143"><span class="linenos">143</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-144"><a href="#AsyncioLoop.__init__-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-145"><a href="#AsyncioLoop.__init__-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroWrapperBase</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-146"><a href="#AsyncioLoop.__init__-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="AsyncioLoop.__init__-147"><a href="#AsyncioLoop.__init__-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_internal_loop</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop.__init__-148"><a href="#AsyncioLoop.__init__-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-149"><a href="#AsyncioLoop.__init__-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop.__init__-150"><a href="#AsyncioLoop.__init__-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_new_requests</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop.__init__-151"><a href="#AsyncioLoop.__init__-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loops_intercommunication</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop.__init__-152"><a href="#AsyncioLoop.__init__-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_previous_on_wrong_request</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-153"><a href="#AsyncioLoop.__init__-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="AsyncioLoop.__init__-154"><a href="#AsyncioLoop.__init__-154"><span class="linenos">154</span></a>
</span><span id="AsyncioLoop.__init__-155"><a href="#AsyncioLoop.__init__-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="AsyncioLoop.__init__-156"><a href="#AsyncioLoop.__init__-156"><span class="linenos">156</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_inherit_surrounding_loop</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-157"><a href="#AsyncioLoop.__init__-157"><span class="linenos">157</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_start_internal_loop</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-158"><a href="#AsyncioLoop.__init__-158"><span class="linenos">158</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_ensure_loop</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-159"><a href="#AsyncioLoop.__init__-159"><span class="linenos">159</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-160"><a href="#AsyncioLoop.__init__-160"><span class="linenos">160</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-161"><a href="#AsyncioLoop.__init__-161"><span class="linenos">161</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-162"><a href="#AsyncioLoop.__init__-162"><span class="linenos">162</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_create_task</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-163"><a href="#AsyncioLoop.__init__-163"><span class="linenos">163</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__internal_loop_yield</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-164"><a href="#AsyncioLoop.__init__-164"><span class="linenos">164</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_turn_on_loops_intercommunication</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-165"><a href="#AsyncioLoop.__init__-165"><span class="linenos">165</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-166"><a href="#AsyncioLoop.__init__-166"><span class="linenos">166</span></a>            <span class="mi">10</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_await</span><span class="p">,</span>
</span><span id="AsyncioLoop.__init__-167"><a href="#AsyncioLoop.__init__-167"><span class="linenos">167</span></a>            <span class="mi">11</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__internal_wait_for_new_requests</span><span class="p">,</span> 
</span><span id="AsyncioLoop.__init__-168"><a href="#AsyncioLoop.__init__-168"><span class="linenos">168</span></a>            <span class="mi">12</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__use_higher_level_sleep_manager</span><span class="p">,</span> 
</span><span id="AsyncioLoop.__init__-169"><a href="#AsyncioLoop.__init__-169"><span class="linenos">169</span></a>            <span class="mi">13</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on__low_latency_io_mode</span><span class="p">,</span> 
</span><span id="AsyncioLoop.__init__-170"><a href="#AsyncioLoop.__init__-170"><span class="linenos">170</span></a>        <span class="p">}</span>
</span><span id="AsyncioLoop.__init__-171"><a href="#AsyncioLoop.__init__-171"><span class="linenos">171</span></a>        
</span><span id="AsyncioLoop.__init__-172"><a href="#AsyncioLoop.__init__-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AsyncioLoop.__init__-173"><a href="#AsyncioLoop.__init__-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AsyncioLoop.__init__-174"><a href="#AsyncioLoop.__init__-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="AsyncioLoop.__init__-175"><a href="#AsyncioLoop.__init__-175"><span class="linenos">175</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="AsyncioLoop.__init__-176"><a href="#AsyncioLoop.__init__-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-177"><a href="#AsyncioLoop.__init__-177"><span class="linenos">177</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_original_loop_class</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-178"><a href="#AsyncioLoop.__init__-178"><span class="linenos">178</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_idle_for</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RationalNumber</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># in seconds</span>
</span><span id="AsyncioLoop.__init__-179"><a href="#AsyncioLoop.__init__-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop.__init__-180"><a href="#AsyncioLoop.__init__-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.__init__-181"><a href="#AsyncioLoop.__init__-181"><span class="linenos">181</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.async_loop" class="classattr">
                                <div class="attr variable">
            <span class="name">async_loop</span><span class="annotation">: Union[asyncio.events.AbstractEventLoop, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.async_loop"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.internal_async_loop" class="classattr">
                                <div class="attr variable">
            <span class="name">internal_async_loop</span><span class="annotation">: Union[asyncio.events.AbstractEventLoop, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.internal_async_loop"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.internal_loop_start_waiters" class="classattr">
                                <div class="attr variable">
            <span class="name">internal_loop_start_waiters</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.internal_loop_start_waiters"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.need_to_stop_internal_loop" class="classattr">
                                <div class="attr variable">
            <span class="name">need_to_stop_internal_loop</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.need_to_stop_internal_loop"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.internal_loop_creation_error" class="classattr">
                                <div class="attr variable">
            <span class="name">internal_loop_creation_error</span><span class="annotation">: Union[Exception, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.internal_loop_creation_error"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.internal_loop_in_yield" class="classattr">
                                <div class="attr variable">
            <span class="name">internal_loop_in_yield</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.internal_loop_in_yield"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.waiting_for_new_requests" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_new_requests</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.waiting_for_new_requests"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.loops_intercommunication" class="classattr">
                                <div class="attr variable">
            <span class="name">loops_intercommunication</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.loops_intercommunication"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.intercommunication_requests_coro_ids" class="classattr">
                                <div class="attr variable">
            <span class="name">intercommunication_requests_coro_ids</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.intercommunication_requests_coro_ids"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.pending_requests_num" class="classattr">
                                <div class="attr variable">
            <span class="name">pending_requests_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.pending_requests_num"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.new_requests_num" class="classattr">
                                <div class="attr variable">
            <span class="name">new_requests_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.new_requests_num"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.no_idle_calls" class="classattr">
                                <div class="attr variable">
            <span class="name">no_idle_calls</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.no_idle_calls"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.results" class="classattr">
                                <div class="attr variable">
            <span class="name">results</span><span class="annotation">: Dict[int, Tuple[Any, Exception]]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.results"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.use_higher_level_sleep_manager" class="classattr">
                                <div class="attr variable">
            <span class="name">use_higher_level_sleep_manager</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.use_higher_level_sleep_manager"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.current_on_idle_handler" class="classattr">
                                <div class="attr variable">
            <span class="name">current_on_idle_handler</span><span class="annotation">: Union[Callable, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.current_on_idle_handler"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.low_latency_io_mode" class="classattr">
                                <div class="attr variable">
            <span class="name">low_latency_io_mode</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoop.low_latency_io_mode"></a>
    
    

                            </div>
                            <div id="AsyncioLoop.destroy" class="classattr">
                                        <input id="AsyncioLoop.destroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AsyncioLoop.destroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.destroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.destroy-183"><a href="#AsyncioLoop.destroy-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AsyncioLoop.destroy-184"><a href="#AsyncioLoop.destroy-184"><span class="linenos">184</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.destroy-185"><a href="#AsyncioLoop.destroy-185"><span class="linenos">185</span></a>            <span class="n">events</span><span class="o">.</span><span class="n">_set_running_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.get_entity_stats" class="classattr">
                                        <input id="AsyncioLoop.get_entity_stats-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_entity_stats</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">stats_level</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.get_entity_stats-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.get_entity_stats"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.get_entity_stats-193"><a href="#AsyncioLoop.get_entity_stats-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="AsyncioLoop.get_entity_stats-194"><a href="#AsyncioLoop.get_entity_stats-194"><span class="linenos">194</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="AsyncioLoop.get_entity_stats-195"><a href="#AsyncioLoop.get_entity_stats-195"><span class="linenos">195</span></a>            <span class="s1">&#39;pending requests num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span>
</span><span id="AsyncioLoop.get_entity_stats-196"><a href="#AsyncioLoop.get_entity_stats-196"><span class="linenos">196</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="AsyncioLoop.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#AsyncioLoopRequest">AsyncioLoopRequest</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.single_task_registration_or_immediate_processing-198"><a href="#AsyncioLoop.single_task_registration_or_immediate_processing-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="AsyncioLoop.single_task_registration_or_immediate_processing-199"><a href="#AsyncioLoop.single_task_registration_or_immediate_processing-199"><span class="linenos">199</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AsyncioLoopRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="AsyncioLoop.single_task_registration_or_immediate_processing-200"><a href="#AsyncioLoop.single_task_registration_or_immediate_processing-200"><span class="linenos">200</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.single_task_registration_or_immediate_processing-201"><a href="#AsyncioLoop.single_task_registration_or_immediate_processing-201"><span class="linenos">201</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="AsyncioLoop.single_task_registration_or_immediate_processing-202"><a href="#AsyncioLoop.single_task_registration_or_immediate_processing-202"><span class="linenos">202</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.full_processing_iteration" class="classattr">
                                        <input id="AsyncioLoop.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AsyncioLoop.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.full_processing_iteration-204"><a href="#AsyncioLoop.full_processing_iteration-204"><span class="linenos">204</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AsyncioLoop.full_processing_iteration-205"><a href="#AsyncioLoop.full_processing_iteration-205"><span class="linenos">205</span></a>        <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus</span> <span class="kn">import</span> <span class="n">AsyncEventBusRequest</span><span class="p">,</span> <span class="n">try_send_async_event</span>
</span><span id="AsyncioLoop.full_processing_iteration-206"><a href="#AsyncioLoop.full_processing_iteration-206"><span class="linenos">206</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-207"><a href="#AsyncioLoop.full_processing_iteration-207"><span class="linenos">207</span></a>            <span class="c1"># throw_coro_service: ThrowCoro = self._loop.get_service_instance(ThrowCoro)</span>
</span><span id="AsyncioLoop.full_processing_iteration-208"><a href="#AsyncioLoop.full_processing_iteration-208"><span class="linenos">208</span></a>            <span class="c1"># throw_coro_service._add_direct_request(self._waiting_coro_id, WaitingCancelled)</span>
</span><span id="AsyncioLoop.full_processing_iteration-209"><a href="#AsyncioLoop.full_processing_iteration-209"><span class="linenos">209</span></a>            <span class="n">kill_coro_service</span><span class="p">:</span> <span class="n">KillCoro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">KillCoro</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-210"><a href="#AsyncioLoop.full_processing_iteration-210"><span class="linenos">210</span></a>            <span class="n">kill_coro_service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-211"><a href="#AsyncioLoop.full_processing_iteration-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_waiting_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.full_processing_iteration-212"><a href="#AsyncioLoop.full_processing_iteration-212"><span class="linenos">212</span></a>            <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span> <span class="n">WAITING_FOR_NEW_REQUESTS_EVENT</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-213"><a href="#AsyncioLoop.full_processing_iteration-213"><span class="linenos">213</span></a>
</span><span id="AsyncioLoop.full_processing_iteration-214"><a href="#AsyncioLoop.full_processing_iteration-214"><span class="linenos">214</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-215"><a href="#AsyncioLoop.full_processing_iteration-215"><span class="linenos">215</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-216"><a href="#AsyncioLoop.full_processing_iteration-216"><span class="linenos">216</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_loop_holding_coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-217"><a href="#AsyncioLoop.full_processing_iteration-217"><span class="linenos">217</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_in_yield</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AsyncioLoop.full_processing_iteration-218"><a href="#AsyncioLoop.full_processing_iteration-218"><span class="linenos">218</span></a>
</span><span id="AsyncioLoop.full_processing_iteration-219"><a href="#AsyncioLoop.full_processing_iteration-219"><span class="linenos">219</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-220"><a href="#AsyncioLoop.full_processing_iteration-220"><span class="linenos">220</span></a>            <span class="n">loop_response</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.full_processing_iteration-221"><a href="#AsyncioLoop.full_processing_iteration-221"><span class="linenos">221</span></a>            <span class="n">exception_response</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AsyncioLoop.full_processing_iteration-222"><a href="#AsyncioLoop.full_processing_iteration-222"><span class="linenos">222</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-223"><a href="#AsyncioLoop.full_processing_iteration-223"><span class="linenos">223</span></a>                <span class="n">loop_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span>
</span><span id="AsyncioLoop.full_processing_iteration-224"><a href="#AsyncioLoop.full_processing_iteration-224"><span class="linenos">224</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-225"><a href="#AsyncioLoop.full_processing_iteration-225"><span class="linenos">225</span></a>                <span class="n">exception_response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span>
</span><span id="AsyncioLoop.full_processing_iteration-226"><a href="#AsyncioLoop.full_processing_iteration-226"><span class="linenos">226</span></a>            
</span><span id="AsyncioLoop.full_processing_iteration-227"><a href="#AsyncioLoop.full_processing_iteration-227"><span class="linenos">227</span></a>            <span class="k">if</span> <span class="n">loop_response</span> <span class="ow">or</span> <span class="n">exception_response</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-228"><a href="#AsyncioLoop.full_processing_iteration-228"><span class="linenos">228</span></a>                <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-229"><a href="#AsyncioLoop.full_processing_iteration-229"><span class="linenos">229</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">loop_response</span><span class="p">,</span> <span class="n">exception_response</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-230"><a href="#AsyncioLoop.full_processing_iteration-230"><span class="linenos">230</span></a>
</span><span id="AsyncioLoop.full_processing_iteration-231"><a href="#AsyncioLoop.full_processing_iteration-231"><span class="linenos">231</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">)()</span>
</span><span id="AsyncioLoop.full_processing_iteration-232"><a href="#AsyncioLoop.full_processing_iteration-232"><span class="linenos">232</span></a>
</span><span id="AsyncioLoop.full_processing_iteration-233"><a href="#AsyncioLoop.full_processing_iteration-233"><span class="linenos">233</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">response</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="AsyncioLoop.full_processing_iteration-234"><a href="#AsyncioLoop.full_processing_iteration-234"><span class="linenos">234</span></a>            <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">response</span>
</span><span id="AsyncioLoop.full_processing_iteration-235"><a href="#AsyncioLoop.full_processing_iteration-235"><span class="linenos">235</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-236"><a href="#AsyncioLoop.full_processing_iteration-236"><span class="linenos">236</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">intercommunication_requests_coro_ids</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-237"><a href="#AsyncioLoop.full_processing_iteration-237"><span class="linenos">237</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">DirectResponse</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">))</span>
</span><span id="AsyncioLoop.full_processing_iteration-238"><a href="#AsyncioLoop.full_processing_iteration-238"><span class="linenos">238</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-239"><a href="#AsyncioLoop.full_processing_iteration-239"><span class="linenos">239</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-240"><a href="#AsyncioLoop.full_processing_iteration-240"><span class="linenos">240</span></a>        
</span><span id="AsyncioLoop.full_processing_iteration-241"><a href="#AsyncioLoop.full_processing_iteration-241"><span class="linenos">241</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)</span>
</span><span id="AsyncioLoop.full_processing_iteration-242"><a href="#AsyncioLoop.full_processing_iteration-242"><span class="linenos">242</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)()</span>
</span><span id="AsyncioLoop.full_processing_iteration-243"><a href="#AsyncioLoop.full_processing_iteration-243"><span class="linenos">243</span></a>        
</span><span id="AsyncioLoop.full_processing_iteration-244"><a href="#AsyncioLoop.full_processing_iteration-244"><span class="linenos">244</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="p">:</span>
</span><span id="AsyncioLoop.full_processing_iteration-245"><a href="#AsyncioLoop.full_processing_iteration-245"><span class="linenos">245</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.is_low_latency" class="classattr">
                                        <input id="AsyncioLoop.is_low_latency-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_low_latency</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.is_low_latency-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.is_low_latency"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.is_low_latency-247"><a href="#AsyncioLoop.is_low_latency-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="nf">is_low_latency</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="AsyncioLoop.is_low_latency-248"><a href="#AsyncioLoop.is_low_latency-248"><span class="linenos">248</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.in_work" class="classattr">
                                        <input id="AsyncioLoop.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.in_work-250"><a href="#AsyncioLoop.in_work-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="AsyncioLoop.in_work-251"><a href="#AsyncioLoop.in_work-251"><span class="linenos">251</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_start_waiters</span><span class="p">)</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span><span class="p">)</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)</span>
</span><span id="AsyncioLoop.in_work-252"><a href="#AsyncioLoop.in_work-252"><span class="linenos">252</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="AsyncioLoop.register_await_response" class="classattr">
                                        <input id="AsyncioLoop.register_await_response-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_await_response</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">response</span><span class="p">:</span> <span class="n">Any</span>,</span><span class="param">	<span class="n">exception</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="ne">Exception</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AsyncioLoop.register_await_response-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.register_await_response"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.register_await_response-326"><a href="#AsyncioLoop.register_await_response-326"><span class="linenos">326</span></a>    <span class="k">def</span> <span class="nf">register_await_response</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]):</span>
</span><span id="AsyncioLoop.register_await_response-327"><a href="#AsyncioLoop.register_await_response-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="AsyncioLoop.register_await_response-328"><a href="#AsyncioLoop.register_await_response-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">no_idle_calls</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="AsyncioLoop.register_await_response-329"><a href="#AsyncioLoop.register_await_response-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.register_new_asyncio_request" class="classattr">
                                        <input id="AsyncioLoop.register_new_asyncio_request-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_new_asyncio_request</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.register_new_asyncio_request-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.register_new_asyncio_request"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.register_new_asyncio_request-383"><a href="#AsyncioLoop.register_new_asyncio_request-383"><span class="linenos">383</span></a>    <span class="k">def</span> <span class="nf">register_new_asyncio_request</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.register_new_asyncio_request-384"><a href="#AsyncioLoop.register_new_asyncio_request-384"><span class="linenos">384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_requests_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="AsyncioLoop.register_new_asyncio_request-385"><a href="#AsyncioLoop.register_new_asyncio_request-385"><span class="linenos">385</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.add_on_idle_handler" class="classattr">
                                        <input id="AsyncioLoop.add_on_idle_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_on_idle_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.add_on_idle_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.add_on_idle_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.add_on_idle_handler-387"><a href="#AsyncioLoop.add_on_idle_handler-387"><span class="linenos">387</span></a>    <span class="k">def</span> <span class="nf">add_on_idle_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.add_on_idle_handler-388"><a href="#AsyncioLoop.add_on_idle_handler-388"><span class="linenos">388</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">:</span>
</span><span id="AsyncioLoop.add_on_idle_handler-389"><a href="#AsyncioLoop.add_on_idle_handler-389"><span class="linenos">389</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span>
</span><span id="AsyncioLoop.add_on_idle_handler-390"><a href="#AsyncioLoop.add_on_idle_handler-390"><span class="linenos">390</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.discard_on_idle_handler" class="classattr">
                                        <input id="AsyncioLoop.discard_on_idle_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">discard_on_idle_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.discard_on_idle_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.discard_on_idle_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.discard_on_idle_handler-392"><a href="#AsyncioLoop.discard_on_idle_handler-392"><span class="linenos">392</span></a>    <span class="k">def</span> <span class="nf">discard_on_idle_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.discard_on_idle_handler-393"><a href="#AsyncioLoop.discard_on_idle_handler-393"><span class="linenos">393</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">on_idle_handlers</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_system_loop_idle</span><span class="p">)</span>
</span><span id="AsyncioLoop.discard_on_idle_handler-394"><a href="#AsyncioLoop.discard_on_idle_handler-394"><span class="linenos">394</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_on_idle_handler</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.inline_get" class="classattr">
                                        <input id="AsyncioLoop.inline_get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">inline_get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AsyncioLoop.inline_get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.inline_get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.inline_get-440"><a href="#AsyncioLoop.inline_get-440"><span class="linenos">440</span></a>    <span class="k">def</span> <span class="nf">inline_get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AsyncioLoop.inline_get-441"><a href="#AsyncioLoop.inline_get-441"><span class="linenos">441</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoop.inline_get-442"><a href="#AsyncioLoop.inline_get-442"><span class="linenos">442</span></a>            <span class="k">raise</span> <span class="n">AsyncioLoopWasNotSetError</span>
</span><span id="AsyncioLoop.inline_get-443"><a href="#AsyncioLoop.inline_get-443"><span class="linenos">443</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AsyncioLoop.inline_get-444"><a href="#AsyncioLoop.inline_get-444"><span class="linenos">444</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.inline_set_internal_loop" class="classattr">
                                        <input id="AsyncioLoop.inline_set_internal_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">inline_set_internal_loop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">loop</span>, </span><span class="param"><span class="n">exception</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="ne">Exception</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AsyncioLoop.inline_set_internal_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.inline_set_internal_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.inline_set_internal_loop-446"><a href="#AsyncioLoop.inline_set_internal_loop-446"><span class="linenos">446</span></a>    <span class="k">def</span> <span class="nf">inline_set_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]):</span>
</span><span id="AsyncioLoop.inline_set_internal_loop-447"><a href="#AsyncioLoop.inline_set_internal_loop-447"><span class="linenos">447</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_async_loop</span> <span class="o">=</span> <span class="n">loop</span>
</span><span id="AsyncioLoop.inline_set_internal_loop-448"><a href="#AsyncioLoop.inline_set_internal_loop-448"><span class="linenos">448</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">internal_loop_creation_error</span> <span class="o">=</span> <span class="n">exception</span>
</span><span id="AsyncioLoop.inline_set_internal_loop-449"><a href="#AsyncioLoop.inline_set_internal_loop-449"><span class="linenos">449</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoop.is_need_to_yield_internal_loop" class="classattr">
                                        <input id="AsyncioLoop.is_need_to_yield_internal_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_need_to_yield_internal_loop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoop.is_need_to_yield_internal_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoop.is_need_to_yield_internal_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoop.is_need_to_yield_internal_loop-451"><a href="#AsyncioLoop.is_need_to_yield_internal_loop-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">is_need_to_yield_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="AsyncioLoop.is_need_to_yield_internal_loop-452"><a href="#AsyncioLoop.is_need_to_yield_internal_loop-452"><span class="linenos">452</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_num</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="AsyncioLoop.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="AsyncioLoop.iteration" class="function">iteration</dd>
                <dd id="AsyncioLoop.make_response" class="function">make_response</dd>
                <dd id="AsyncioLoop.register_response" class="function">register_response</dd>
                <dd id="AsyncioLoop.put_task" class="function">put_task</dd>
                <dd id="AsyncioLoop.resolve_request" class="function">resolve_request</dd>
                <dd id="AsyncioLoop.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="AsyncioLoop.in_forground_work" class="function">in_forground_work</dd>
                <dd id="AsyncioLoop.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="AsyncioLoop.time_left_before_next_event" class="function">time_left_before_next_event</dd>
                <dd id="AsyncioLoop.make_live" class="function">make_live</dd>
                <dd id="AsyncioLoop.make_dead" class="function">make_dead</dd>
                <dd id="AsyncioLoop.service_id_impl" class="function">service_id_impl</dd>
                <dd id="AsyncioLoop.service_id" class="function">service_id</dd>

            </div>
            <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="AsyncioLoop.StatsLevel" class="class">StatsLevel</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="AsyncioLoopRequest">
                            <input id="AsyncioLoopRequest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">AsyncioLoopRequest</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</span>):

                <label class="view-source-button" for="AsyncioLoopRequest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest-85"><a href="#AsyncioLoopRequest-85"><span class="linenos"> 85</span></a><span class="k">class</span> <span class="nc">AsyncioLoopRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="AsyncioLoopRequest-86"><a href="#AsyncioLoopRequest-86"><span class="linenos"> 86</span></a>    <span class="k">def</span> <span class="nf">inherit_surrounding_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-87"><a href="#AsyncioLoopRequest-87"><span class="linenos"> 87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-88"><a href="#AsyncioLoopRequest-88"><span class="linenos"> 88</span></a>
</span><span id="AsyncioLoopRequest-89"><a href="#AsyncioLoopRequest-89"><span class="linenos"> 89</span></a>    <span class="k">def</span> <span class="nf">start_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-90"><a href="#AsyncioLoopRequest-90"><span class="linenos"> 90</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">,</span> <span class="n">debug</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-91"><a href="#AsyncioLoopRequest-91"><span class="linenos"> 91</span></a>
</span><span id="AsyncioLoopRequest-92"><a href="#AsyncioLoopRequest-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="nf">ensure_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-93"><a href="#AsyncioLoopRequest-93"><span class="linenos"> 93</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-94"><a href="#AsyncioLoopRequest-94"><span class="linenos"> 94</span></a>
</span><span id="AsyncioLoopRequest-95"><a href="#AsyncioLoopRequest-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-96"><a href="#AsyncioLoopRequest-96"><span class="linenos"> 96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-97"><a href="#AsyncioLoopRequest-97"><span class="linenos"> 97</span></a>
</span><span id="AsyncioLoopRequest-98"><a href="#AsyncioLoopRequest-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-99"><a href="#AsyncioLoopRequest-99"><span class="linenos"> 99</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-100"><a href="#AsyncioLoopRequest-100"><span class="linenos">100</span></a>
</span><span id="AsyncioLoopRequest-101"><a href="#AsyncioLoopRequest-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">wait</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-102"><a href="#AsyncioLoopRequest-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-103"><a href="#AsyncioLoopRequest-103"><span class="linenos">103</span></a>
</span><span id="AsyncioLoopRequest-104"><a href="#AsyncioLoopRequest-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio_Task</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-105"><a href="#AsyncioLoopRequest-105"><span class="linenos">105</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-106"><a href="#AsyncioLoopRequest-106"><span class="linenos">106</span></a>
</span><span id="AsyncioLoopRequest-107"><a href="#AsyncioLoopRequest-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">_internal_loop_yield</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-108"><a href="#AsyncioLoopRequest-108"><span class="linenos">108</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-109"><a href="#AsyncioLoopRequest-109"><span class="linenos">109</span></a>
</span><span id="AsyncioLoopRequest-110"><a href="#AsyncioLoopRequest-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">turn_on_loops_intercommunication</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="AsyncioLoopRequest-111"><a href="#AsyncioLoopRequest-111"><span class="linenos">111</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-112"><a href="#AsyncioLoopRequest-112"><span class="linenos">112</span></a>
</span><span id="AsyncioLoopRequest-113"><a href="#AsyncioLoopRequest-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="nf">_wait_intercommunication</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-114"><a href="#AsyncioLoopRequest-114"><span class="linenos">114</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-115"><a href="#AsyncioLoopRequest-115"><span class="linenos">115</span></a>
</span><span id="AsyncioLoopRequest-116"><a href="#AsyncioLoopRequest-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="nf">wait_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-117"><a href="#AsyncioLoopRequest-117"><span class="linenos">117</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-118"><a href="#AsyncioLoopRequest-118"><span class="linenos">118</span></a>
</span><span id="AsyncioLoopRequest-119"><a href="#AsyncioLoopRequest-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">use_higher_level_sleep_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-120"><a href="#AsyncioLoopRequest-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">)</span>
</span><span id="AsyncioLoopRequest-121"><a href="#AsyncioLoopRequest-121"><span class="linenos">121</span></a>
</span><span id="AsyncioLoopRequest-122"><a href="#AsyncioLoopRequest-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">turn_on_low_latency_io_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest-123"><a href="#AsyncioLoopRequest-123"><span class="linenos">123</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">13</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="AsyncioLoopRequest.inherit_surrounding_loop" class="classattr">
                                        <input id="AsyncioLoopRequest.inherit_surrounding_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">inherit_surrounding_loop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.inherit_surrounding_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.inherit_surrounding_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.inherit_surrounding_loop-86"><a href="#AsyncioLoopRequest.inherit_surrounding_loop-86"><span class="linenos">86</span></a>    <span class="k">def</span> <span class="nf">inherit_surrounding_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.inherit_surrounding_loop-87"><a href="#AsyncioLoopRequest.inherit_surrounding_loop-87"><span class="linenos">87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.start_internal_loop" class="classattr">
                                        <input id="AsyncioLoopRequest.start_internal_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start_internal_loop</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">priority</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.start_internal_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.start_internal_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.start_internal_loop-89"><a href="#AsyncioLoopRequest.start_internal_loop-89"><span class="linenos">89</span></a>    <span class="k">def</span> <span class="nf">start_internal_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">debug</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.start_internal_loop-90"><a href="#AsyncioLoopRequest.start_internal_loop-90"><span class="linenos">90</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">,</span> <span class="n">debug</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.ensure_loop" class="classattr">
                                        <input id="AsyncioLoopRequest.ensure_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ensure_loop</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">priority</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.ensure_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.ensure_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.ensure_loop-92"><a href="#AsyncioLoopRequest.ensure_loop-92"><span class="linenos">92</span></a>    <span class="k">def</span> <span class="nf">ensure_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.ensure_loop-93"><a href="#AsyncioLoopRequest.ensure_loop-93"><span class="linenos">93</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">main_awaitable</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="n">interrupt_when_no_requests</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.set" class="classattr">
                                        <input id="AsyncioLoopRequest.set-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">async_loop</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.set-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.set"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.set-95"><a href="#AsyncioLoopRequest.set-95"><span class="linenos">95</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.set-96"><a href="#AsyncioLoopRequest.set-96"><span class="linenos">96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">async_loop</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.get" class="classattr">
                                        <input id="AsyncioLoopRequest.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.get-98"><a href="#AsyncioLoopRequest.get-98"><span class="linenos">98</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AbstractEventLoop</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.get-99"><a href="#AsyncioLoopRequest.get-99"><span class="linenos">99</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.wait" class="classattr">
                                        <input id="AsyncioLoopRequest.wait-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wait</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.wait-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.wait"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.wait-101"><a href="#AsyncioLoopRequest.wait-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">wait</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.wait-102"><a href="#AsyncioLoopRequest.wait-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.create_task" class="classattr">
                                        <input id="AsyncioLoopRequest.create_task-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create_task</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Task</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.create_task-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.create_task"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.create_task-104"><a href="#AsyncioLoopRequest.create_task-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio_Task</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.create_task-105"><a href="#AsyncioLoopRequest.create_task-105"><span class="linenos">105</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.turn_on_loops_intercommunication" class="classattr">
                                        <input id="AsyncioLoopRequest.turn_on_loops_intercommunication-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">turn_on_loops_intercommunication</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">turn_on</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.turn_on_loops_intercommunication-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.turn_on_loops_intercommunication"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.turn_on_loops_intercommunication-110"><a href="#AsyncioLoopRequest.turn_on_loops_intercommunication-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">turn_on_loops_intercommunication</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="AsyncioLoopRequest.turn_on_loops_intercommunication-111"><a href="#AsyncioLoopRequest.turn_on_loops_intercommunication-111"><span class="linenos">111</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">turn_on</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.wait_idle" class="classattr">
                                        <input id="AsyncioLoopRequest.wait_idle-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wait_idle</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.wait_idle-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.wait_idle"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.wait_idle-116"><a href="#AsyncioLoopRequest.wait_idle-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="nf">wait_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.wait_idle-117"><a href="#AsyncioLoopRequest.wait_idle-117"><span class="linenos">117</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">awaitable</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.use_higher_level_sleep_manager" class="classattr">
                                        <input id="AsyncioLoopRequest.use_higher_level_sleep_manager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">use_higher_level_sleep_manager</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.use_higher_level_sleep_manager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.use_higher_level_sleep_manager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.use_higher_level_sleep_manager-119"><a href="#AsyncioLoopRequest.use_higher_level_sleep_manager-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">use_higher_level_sleep_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.use_higher_level_sleep_manager-120"><a href="#AsyncioLoopRequest.use_higher_level_sleep_manager-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="n">use_higher_level_sleep_manager</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.turn_on_low_latency_io_mode" class="classattr">
                                        <input id="AsyncioLoopRequest.turn_on_low_latency_io_mode-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">turn_on_low_latency_io_mode</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="AsyncioLoopRequest.turn_on_low_latency_io_mode-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.turn_on_low_latency_io_mode"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopRequest.turn_on_low_latency_io_mode-122"><a href="#AsyncioLoopRequest.turn_on_low_latency_io_mode-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">turn_on_low_latency_io_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AsyncioLoopRequest.turn_on_low_latency_io_mode-123"><a href="#AsyncioLoopRequest.turn_on_low_latency_io_mode-123"><span class="linenos">123</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">13</span><span class="p">,</span> <span class="n">low_latency_io_mode</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AsyncioLoopRequest.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<input id="AsyncioLoopRequest.default_service_type-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="AsyncioLoopRequest.default_service_type-view-value"></label><span class="default_value">&lt;class &#39;<a href="#AsyncioLoop">AsyncioLoop</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#AsyncioLoopRequest.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="AsyncioLoopRequest.default__request__type__" class="variable">default__request__type__</dd>
                <dd id="AsyncioLoopRequest.request_type" class="variable">request_type</dd>
                <dd id="AsyncioLoopRequest.args" class="variable">args</dd>
                <dd id="AsyncioLoopRequest.kwargs" class="variable">kwargs</dd>
                <dd id="AsyncioLoopRequest.provide_to_request_handler" class="variable">provide_to_request_handler</dd>
                <dd id="AsyncioLoopRequest.interface" class="function">interface</dd>
                <dd id="AsyncioLoopRequest.i" class="function">i</dd>
                <dd id="AsyncioLoopRequest.async_interface" class="function">async_interface</dd>
                <dd id="AsyncioLoopRequest.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="AsyncioLoopWasNotSetError">
                            <input id="AsyncioLoopWasNotSetError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">AsyncioLoopWasNotSetError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="AsyncioLoopWasNotSetError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AsyncioLoopWasNotSetError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AsyncioLoopWasNotSetError-70"><a href="#AsyncioLoopWasNotSetError-70"><span class="linenos">70</span></a><span class="k">class</span> <span class="nc">AsyncioLoopWasNotSetError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="AsyncioLoopWasNotSetError-71"><a href="#AsyncioLoopWasNotSetError-71"><span class="linenos">71</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="AsyncioLoopWasNotSetError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="AsyncioLoopWasNotSetError.with_traceback" class="function">with_traceback</dd>
                <dd id="AsyncioLoopWasNotSetError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="run_in_thread_pool">
                            <input id="run_in_thread_pool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run_in_thread_pool</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">function</span><span class="p">:</span> <span class="n">Callable</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="run_in_thread_pool-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#run_in_thread_pool"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="run_in_thread_pool-658"><a href="#run_in_thread_pool-658"><span class="linenos">658</span></a><span class="k">def</span> <span class="nf">run_in_thread_pool</span><span class="p">(</span><span class="n">function</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="run_in_thread_pool-659"><a href="#run_in_thread_pool-659"><span class="linenos">659</span></a>    <span class="k">return</span> <span class="n">run_in_thread_pool_fast</span><span class="p">(</span><span class="n">current_interface</span><span class="p">(),</span> <span class="n">function</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="run_in_thread_pool_fast">
                            <input id="run_in_thread_pool_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run_in_thread_pool_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">interface</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="n">function</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="run_in_thread_pool_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#run_in_thread_pool_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="run_in_thread_pool_fast-649"><a href="#run_in_thread_pool_fast-649"><span class="linenos">649</span></a><span class="k">def</span> <span class="nf">run_in_thread_pool_fast</span><span class="p">(</span><span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">function</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="run_in_thread_pool_fast-650"><a href="#run_in_thread_pool_fast-650"><span class="linenos">650</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">task_wrapper</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="run_in_thread_pool_fast-651"><a href="#run_in_thread_pool_fast-651"><span class="linenos">651</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">function</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="run_in_thread_pool_fast-652"><a href="#run_in_thread_pool_fast-652"><span class="linenos">652</span></a>
</span><span id="run_in_thread_pool_fast-653"><a href="#run_in_thread_pool_fast-653"><span class="linenos">653</span></a>    <span class="k">return</span> <span class="n">interface</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">task_wrapper</span><span class="p">(</span>
</span><span id="run_in_thread_pool_fast-654"><a href="#run_in_thread_pool_fast-654"><span class="linenos">654</span></a>        <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">(),</span> 
</span><span id="run_in_thread_pool_fast-655"><a href="#run_in_thread_pool_fast-655"><span class="linenos">655</span></a>        <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)))</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>