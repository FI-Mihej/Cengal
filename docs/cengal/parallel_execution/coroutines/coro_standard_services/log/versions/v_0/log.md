---
title: log
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.log<wbr>.versions<wbr>.v_0<wbr>.log    </h1>

                
                        <input id="mod-log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-log-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;InfoFields&#39;</span><span class="p">,</span> <span class="s1">&#39;default_info_gatherer&#39;</span><span class="p">,</span> <span class="s1">&#39;LogExtended&#39;</span><span class="p">,</span> <span class="s1">&#39;LogEx&#39;</span><span class="p">,</span> <span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="s1">&#39;LogRequest&#39;</span><span class="p">,</span> 
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>           <span class="s1">&#39;view_log&#39;</span><span class="p">,</span> <span class="s1">&#39;clear_log&#39;</span><span class="p">,</span> <span class="s1">&#39;LogClient&#39;</span><span class="p">,</span> <span class="s1">&#39;default_log_client&#39;</span><span class="p">,</span> <span class="s1">&#39;log_fast&#39;</span><span class="p">,</span> <span class="s1">&#39;alog_fast&#39;</span><span class="p">,</span> 
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>           <span class="s1">&#39;log&#39;</span><span class="p">,</span> <span class="s1">&#39;alog&#39;</span><span class="p">,</span> <span class="s1">&#39;put_log_fast&#39;</span><span class="p">,</span> <span class="s1">&#39;plog_fast&#39;</span><span class="p">,</span> <span class="s1">&#39;put_log&#39;</span><span class="p">,</span> <span class="s1">&#39;plog&#39;</span><span class="p">]</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.await_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">CoroPriority</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.instance</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.app_fs_structure.app_dir_path</span> <span class="kn">import</span> <span class="n">AppDirPath</span><span class="p">,</span> <span class="n">AppDirectoryType</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.path_manager</span> <span class="kn">import</span> <span class="n">RelativePath</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.file_manager</span> <span class="kn">import</span> <span class="n">path_relative_to_current_dir</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.cpu_clock_cycles</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.serialization</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span><span class="p">,</span> <span class="n">frame</span><span class="p">,</span> <span class="n">entity_repr_owner_based</span><span class="p">,</span> <span class="n">entity_name</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.python_bytecode_manipulator</span> <span class="kn">import</span> <span class="n">get_code</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.args_manager</span> <span class="kn">import</span> <span class="n">args_kwargs_to_str</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values</span> <span class="kn">import</span> <span class="n">ValueExistence</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">IntEnum</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">traceback</span> <span class="kn">import</span> <span class="n">format_stack</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Callable</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">import</span> <span class="nn">logging</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">import</span> <span class="nn">os</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="kn">import</span> <span class="nn">lmdb</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="kn">from</span> <span class="nn">warnings</span> <span class="kn">import</span> <span class="n">warn</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="n">warn</span><span class="p">(</span><span class="s1">&#39;&#39;&#39;WARNING: `lmdb` library is not installed. Log service will not work.</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="s1">         To install `lmdb` use: `pip install lmdb`&#39;&#39;&#39;</span><span class="p">)</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="k">raise</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="sd">Module Docstring</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="k">def</span> <span class="nf">get_coro_parents_path</span><span class="p">(</span><span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]:</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="n">parents</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="n">result</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">deep</span><span class="p">,</span> <span class="n">child</span><span class="p">,</span> <span class="n">parent</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="k">if</span> <span class="n">parent</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>            <span class="n">coro_id</span> <span class="o">=</span> <span class="n">parent</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>            <span class="n">parents</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="n">try_travers_through_all_coro_parents</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="k">def</span> <span class="nf">coro_info_string</span><span class="p">(</span><span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="n">coro</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroWrapperBase</span><span class="p">]</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_coro</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="k">if</span> <span class="n">coro</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;  CoroID: </span><span class="si">{</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="n">GreenletWorkerWrapper</span><span class="p">):</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>            <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;  CoroID: </span><span class="si">{</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">; Type: </span><span class="si">{</span><span class="s2">&quot;Awaitable&quot;</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="nb">isinstance</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span><span class="w"> </span><span class="n">CoroWrapperAsyncAwait</span><span class="p">)</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s2">&quot;Greenlet&quot;</span><span class="si">}</span><span class="s1">; Worker: </span><span class="si">{</span><span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a><span class="k">def</span> <span class="nf">get_coro_parents_strings</span><span class="p">(</span><span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="n">coro_parents_path</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_coro_parents_path</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">if</span> <span class="n">coro_parents_path</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">get_current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="k">if</span> <span class="n">cs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;  CoroID: </span><span class="si">{</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">coro_parents_path</span><span class="p">])</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">([</span><span class="n">coro_info_string</span><span class="p">(</span><span class="n">cs</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span> <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">coro_parents_path</span><span class="p">])</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a><span class="k">class</span> <span class="nc">InfoFields</span><span class="p">(</span><span class="n">IntEnum</span><span class="p">):</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    <span class="n">current_time</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="n">file_name</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="n">line_number</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>    <span class="n">caller_info</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    <span class="n">traceback_strings</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>    <span class="n">perf_counter_time</span> <span class="o">=</span> <span class="mi">5</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>    <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="mi">6</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="n">logging_level</span> <span class="o">=</span> <span class="mi">7</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a><span class="k">def</span> <span class="nf">default_info_gatherer</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="n">interested_frame</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="k">except</span> <span class="n">OutsideCoroSchedulerContext</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="n">caller_info</span> <span class="o">=</span> <span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">interested_frame</span><span class="p">)</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_coro</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="n">GreenletWorkerWrapper</span><span class="p">):</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>            <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="n">caller_info</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;CoroID: </span><span class="si">{</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">; Type: </span><span class="si">{</span><span class="s2">&quot;Awaitable&quot;</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">_coro</span><span class="p">,</span><span class="w"> </span><span class="n">CoroWrapperAsyncAwait</span><span class="p">)</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s2">&quot;Greenlet&quot;</span><span class="si">}</span><span class="s1">; Worker: </span><span class="si">{</span><span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="n">get_coro_parents_strings</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">return</span> <span class="p">{</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">current_time</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(),</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">perf_counter_time</span><span class="p">:</span> <span class="n">perf_counter</span><span class="p">(),</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">file_name</span><span class="p">:</span> <span class="n">interested_frame</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">line_number</span><span class="p">:</span> <span class="n">interested_frame</span><span class="o">.</span><span class="n">f_lineno</span><span class="p">,</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">caller_info</span><span class="p">:</span> <span class="n">caller_info</span><span class="p">,</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">traceback_strings</span><span class="p">:</span> <span class="n">format_stack</span><span class="p">(</span><span class="n">interested_frame</span><span class="p">),</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">coro_parents_strings</span><span class="p">:</span> <span class="n">coro_parents_strings</span><span class="p">,</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="p">}</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a><span class="k">class</span> <span class="nc">LogExtended</span><span class="p">(</span><span class="n">TypedServiceRequest</span><span class="p">[</span><span class="kc">None</span><span class="p">]):</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="n">default__request__type__</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">info_gatherer</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">depth</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LogExtended&#39;</span><span class="p">:</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="k">return</span> <span class="n">LogExtended</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">depth</span><span class="p">)</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LogEx&#39;</span><span class="p">:</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>            <span class="n">info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="n">info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save_to_copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default__request__type__</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">)</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="n">LogEx</span> <span class="o">=</span> <span class="n">LogExtended</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="k">class</span> <span class="nc">LogRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>    
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>    <span class="k">def</span> <span class="nf">sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>    <span class="k">def</span> <span class="nf">add_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="nf">remove_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="k">return</span> <span class="n">LogEx</span><span class="p">[</span><span class="kc">None</span><span class="p">](</span><span class="n">default_info_gatherer</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">2</span><span class="p">)(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>    <span class="k">def</span> <span class="nf">connect_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">)</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="nf">disconnect_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">)</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>    
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a><span class="k">class</span> <span class="nc">Log</span><span class="p">(</span><span class="n">TypedService</span><span class="p">[</span><span class="kc">None</span><span class="p">],</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_logs_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;log.db&#39;</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">root_path_to_log_environment_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">:</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">Environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">=</span> <span class="mf">0.5</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span> <span class="o">=</span> <span class="mi">16</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">,</span> <span class="n">LoggingHandler</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="c1"># self.serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="c1">#                                    Tags.can_use_bytes,</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="c1">#                                    Tags.decode_str_as_str,</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="c1">#                                    Tags.decode_list_as_list,</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="c1">#                                    Tags.decode_bytes_as_bytes,</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="c1">#                                    Tags.superficial,</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>        <span class="c1">#                                    Tags.current_platform,</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="c1">#                                    Tags.multi_platform),</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="c1">#                                   TestDataType.small,</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="c1">#                                   0.1)</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_db_environment_path</span><span class="p">,</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_sync</span><span class="p">,</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_add_iteration_handler</span><span class="p">,</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_remove_iteration_handler</span><span class="p">,</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_log_extended</span><span class="p">,</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_connect_to_logger</span><span class="p">,</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_disconnect_from_logger</span><span class="p">,</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>        <span class="p">}</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">inject_handler_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>            <span class="s1">&#39;log counter&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="s1">&#39;current counter state key&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="p">}</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>    
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="c1"># self.make_live</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>    
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>    <span class="k">def</span> <span class="nf">put_log_ex</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">):</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="c1"># TODO: we need to use some loop destroy service in order to put our coro which will write all pending queues,</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="c1"># sync envirounments and close them. Also we need to prevent new requests from being processed. (see DB service)</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="n">loggers_instancess</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="k">for</span> <span class="n">logger_instance</span> <span class="ow">in</span> <span class="n">loggers_instancess</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">eject_handler_from_logger</span><span class="p">(</span><span class="n">logger_instance</span><span class="p">)</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_resolve_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="n">coro_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="n">GreenletWorkerWrapper</span><span class="p">):</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>                <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>            
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>            <span class="n">caller_info</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;CoroID: </span><span class="si">{</span><span class="n">coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">; Type: </span><span class="si">{</span><span class="s2">&quot;Awaitable&quot;</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="nb">issubclass</span><span class="p">(</span><span class="n">coro_info</span><span class="o">.</span><span class="n">coro_type</span><span class="p">,</span><span class="w"> </span><span class="n">CoroWrapperAsyncAwait</span><span class="p">)</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s2">&quot;Greenlet&quot;</span><span class="si">}</span><span class="s1">; Worker: </span><span class="si">{</span><span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="n">coro_worker_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>            <span class="n">info</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">current_time</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(),</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">perf_counter_time</span><span class="p">:</span> <span class="n">perf_counter</span><span class="p">(),</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">file_name</span><span class="p">:</span> <span class="n">coro_worker_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">line_number</span><span class="p">:</span> <span class="n">coro_worker_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">caller_info</span><span class="p">:</span> <span class="n">caller_info</span><span class="p">,</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">traceback_strings</span><span class="p">:</span> <span class="nb">list</span><span class="p">(),</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                <span class="c1"># InfoFields.coro_parents_strings: get_coro_parents_strings(coro_info.coro_id),</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">coro_parents_strings</span><span class="p">:</span> <span class="nb">list</span><span class="p">(),</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>            <span class="p">}</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>            <span class="c1"># self.make_live()</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>            <span class="c1"># TODO: we need to implement backpressure mechanism here. If we have too many pending requests, we need to put request to queue instead of responding immediately.</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>            <span class="c1"># However this will not be enough for a direct requests. We need to implement some kind of backpressure mechanism for direct requests too.</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>    <span class="k">def</span> <span class="nf">_ensure_default_db_environment</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>                    <span class="k">async</span> <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">):</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>                        <span class="n">app_name_for_fs</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="s1">&#39;app_name_for_fs&#39;</span><span class="p">))</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>                        <span class="n">app_data_dir_path_type</span><span class="p">:</span> <span class="n">AppDirectoryType</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="s1">&#39;app_data_dir_path_type&#39;</span><span class="p">))</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>                        <span class="n">app_dir_path</span><span class="p">:</span> <span class="n">AppDirPath</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">AppDirPath</span><span class="p">))</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>                        <span class="n">app_data_dir_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">app_dir_path</span><span class="o">.</span><span class="n">cached</span><span class="p">(</span><span class="n">app_data_dir_path_type</span><span class="p">,</span> <span class="n">app_name_for_fs</span><span class="p">)</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">app_data_dir_path</span><span class="p">)(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_logs_dir</span><span class="p">)</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>                    
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span> <span class="o">=</span> <span class="n">put_root_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>                
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_default_db_environment</span><span class="p">():</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>            <span class="k">return</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>        
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="n">log_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">log_queue_buff</span><span class="p">)()</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        <span class="n">current_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="n">current_time_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">current_time</span><span class="p">)</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="k">for</span> <span class="n">iteration_handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="p">:</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>            <span class="n">iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">log_queue_buff</span><span class="p">,</span> <span class="n">current_time</span><span class="p">,</span> <span class="n">current_time_str</span><span class="p">)</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>                <span class="k">for</span> <span class="n">log_info</span> <span class="ow">in</span> <span class="n">log_queue_buff</span><span class="p">:</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                    <span class="n">key</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">get</span><span class="p">())</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span><span class="p">)</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="n">current_time_str</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>                    <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">log_info</span><span class="p">)</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>                    <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">dupdata</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>                
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">),</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>        
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">)</span> \
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> \
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span><span class="p">)</span> \
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>            <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> \
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="ow">or</span> <span class="p">((</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">)</span> <span class="ow">and</span> <span class="p">((</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">)))</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>    
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        <span class="n">time_since_last_sync_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">&gt;</span> <span class="n">time_since_last_sync_time</span><span class="p">:</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">-</span> <span class="n">time_since_last_sync_time</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="mi">0</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>    <span class="k">def</span> <span class="nf">_init_db</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Path to Log DB Env: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>                                        <span class="n">map_async</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">lock</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">metasync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">sync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">meminit</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;logs&#39;</span><span class="p">)</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>        <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>                <span class="n">current_counter_state</span> <span class="o">=</span> <span class="n">txn</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>                <span class="k">if</span> <span class="n">current_counter_state</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>                    <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">),</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">current_counter_state</span><span class="p">)</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>    <span class="k">def</span> <span class="nf">_on_set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">:</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>        
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_to_db_environment</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>    
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="nf">_on_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">:</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>                <span class="c1"># self.db_environment.sync(True)</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>    <span class="k">def</span> <span class="nf">_on_log_extended</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">):</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>    <span class="k">def</span> <span class="nf">_on_add_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]):</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>    
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>    <span class="k">def</span> <span class="nf">_on_remove_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]):</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="n">removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>            <span class="n">removed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>            <span class="k">pass</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">removed</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>    <span class="k">def</span> <span class="nf">sync_in_thread_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>            <span class="k">if</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>                <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">,</span> <span class="kc">True</span><span class="p">))</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>                <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>                    <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>            
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>            <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">):</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>                <span class="k">def</span> <span class="nf">sync_worker</span><span class="p">():</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>                
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>                <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">sync_worker</span><span class="p">)</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">)))</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>            <span class="k">def</span> <span class="nf">make_service_live_for_a_next_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">):</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>            
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">,</span> <span class="n">make_service_live_for_a_next_sync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>        <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">()</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>        <span class="k">except</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">:</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>            <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>        <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">sync_db_coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">)</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>    
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>    <span class="k">def</span> <span class="nf">get_last_n_logs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">number</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]:</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>        
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>        <span class="k">if</span> <span class="n">number</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>            <span class="n">number</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>        <span class="k">elif</span> <span class="n">number</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>        
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>            <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span><span class="o">.</span><span class="n">last</span><span class="p">()</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span><span class="o">.</span><span class="n">iterprev</span><span class="p">():</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>                <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">:</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>                    <span class="k">continue</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>                <span class="k">if</span> <span class="n">number</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>                    <span class="k">break</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>                <span class="n">number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>        
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">reverse</span><span class="p">()</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>    <span class="k">def</span> <span class="nf">inject_handler_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>        <span class="k">if</span> <span class="n">logger_instance</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>            <span class="n">logger_handler</span><span class="p">:</span> <span class="n">LoggingHandler</span> <span class="o">=</span> <span class="n">LoggingHandler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">]</span> <span class="o">=</span> <span class="n">logger_handler</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>            <span class="n">logger_instance</span><span class="o">.</span><span class="n">addHandler</span><span class="p">(</span><span class="n">logger_handler</span><span class="p">)</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>    <span class="k">def</span> <span class="nf">_on_connect_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">):</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">inject_handler_to_logger</span><span class="p">(</span><span class="n">logger_instance</span><span class="p">)</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>    <span class="k">def</span> <span class="nf">eject_handler_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>        <span class="k">if</span> <span class="n">logger_instance</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>            <span class="n">logger_instance</span><span class="o">.</span><span class="n">removeHandler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">])</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">]</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>    <span class="k">def</span> <span class="nf">_on_disconnect_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">):</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">eject_handler_from_logger</span><span class="p">(</span><span class="n">logger_instance</span><span class="p">)</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a><span class="n">LogExtended</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">Log</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a><span class="n">LogRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">Log</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a><span class="k">class</span> <span class="nc">LogClient</span><span class="p">:</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">info_gatherer</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">:</span> <span class="n">LogEx</span> <span class="o">=</span> <span class="n">LogEx</span><span class="p">(</span><span class="n">default_info_gatherer</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>    <span class="k">def</span> <span class="nf">log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>            <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>        
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>        
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>        
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>        
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>    <span class="k">def</span> <span class="nf">put_log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>            <span class="n">log_ex_request</span><span class="p">:</span> <span class="n">LogExtended</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log_ex</span><span class="p">(</span><span class="o">*</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>        
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>    <span class="n">plog_fast</span> <span class="o">=</span> <span class="n">put_log_fast</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>    <span class="c1"># async def aput_log_fast(self, scheduler: CoroSchedulerType, *args, **kwargs):</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>    <span class="c1">#     if self.extended:</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>    <span class="c1">#         log_ex_request: LogExtended = self.log_extended_request(*args, **kwargs)</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>    <span class="c1">#         scheduler.get_service_instance_fast(Log).put_log_ex(*log_ex_request.args, **log_ex_request.kwargs)</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>    <span class="c1">#     else:</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>    <span class="c1">#         scheduler.get_service_instance_fast(Log).put_log(args, kwargs)</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>    <span class="c1"># aplog_fast = aput_log_fast</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">put_log_fast</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>    <span class="n">plog</span> <span class="o">=</span> <span class="n">put_log</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>    <span class="c1"># async def aput_log(self, *args, **kwargs):</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>    <span class="c1">#     self.put_log_fast(current_coro_scheduler(), *args, **kwargs)</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>    <span class="c1"># aplog = aput_log</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a><span class="n">default_log_client</span><span class="p">:</span> <span class="n">LogClient</span> <span class="o">=</span> <span class="n">LogClient</span><span class="p">(</span><span class="n">default_info_gatherer</span><span class="p">)</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a><span class="n">log_fast</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">log_fast</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a><span class="n">alog_fast</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">alog_fast</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a><span class="n">log</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">log</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a><span class="n">alog</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">alog</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a><span class="n">put_log_fast</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">put_log_fast</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a><span class="n">plog_fast</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">plog_fast</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a><span class="n">put_log</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">put_log</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a><span class="n">plog</span> <span class="o">=</span> <span class="n">default_log_client</span><span class="o">.</span><span class="n">plog</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a><span class="c1"># aput_log_fast = default_log_client.aput_log_fast</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a><span class="c1"># aplog_fast = default_log_client.aplog_fast</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a><span class="c1"># aput_log = default_log_client.aput_log</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a><span class="c1"># aplog = default_log_client.aplog</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a><span class="k">def</span> <span class="nf">view_log</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">file_to_redirect_output</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>    <span class="k">if</span> <span class="n">path_to_db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>        <span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_relative_to_current_dir</span><span class="p">(</span><span class="s1">&#39;log.db&#39;</span><span class="p">)</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>    <span class="n">output_file</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>    <span class="k">if</span> <span class="n">file_to_redirect_output</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>        <span class="n">output_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_to_redirect_output</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>        <span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span> <span class="o">**</span> <span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>        <span class="n">db</span> <span class="o">=</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;logs&#39;</span><span class="p">)</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>        <span class="c1"># serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>        <span class="c1">#                               Tags.can_use_bytes,</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>        <span class="c1">#                               Tags.decode_str_as_str,</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>        <span class="c1">#                               Tags.decode_list_as_list,</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>        <span class="c1">#                               Tags.decode_bytes_as_bytes, </span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>        <span class="c1">#                               Tags.superficial,</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>        <span class="c1">#                               Tags.current_platform,</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>        <span class="c1">#                               Tags.multi_platform),</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>        <span class="c1">#                              TestDataType.small,</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>        <span class="c1">#                              0.1)</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>        <span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>        <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">()</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">db</span><span class="p">):</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>                <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">16</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">():</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>                    <span class="k">if</span> <span class="n">output_file</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λλλ &lt;&lt;&lt; </span><span class="si">{</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1"> &gt;&gt;&gt;&#39;</span><span class="p">)</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>                        <span class="nb">print</span><span class="p">()</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λλλ &lt;&lt;&lt; </span><span class="si">{</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1"> &gt;&gt;&gt;&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>                    <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span> <span class="o">=</span> <span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>                    <span class="k">if</span> <span class="n">output_file</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ &gt;&gt;&gt;</span><span class="se">\t</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="s2">&quot;~&quot;</span><span class="o">*</span><span class="mi">8</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="n">info</span><span class="p">)</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>                        <span class="nb">print</span><span class="p">()</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ &gt;&gt;&gt;</span><span class="se">\t</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="s2">&quot;~&quot;</span><span class="o">*</span><span class="mi">8</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">args_kwargs_to_str</span><span class="p">(</span><span class="n">args</span><span class="p">,</span><span class="w"> </span><span class="n">kwargs</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>        <span class="k">if</span> <span class="n">output_file</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>            <span class="n">output_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a><span class="k">def</span> <span class="nf">clear_log</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>    <span class="k">if</span> <span class="n">path_to_db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>        <span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_relative_to_current_dir</span><span class="p">(</span><span class="s1">&#39;log.db&#39;</span><span class="p">)</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>    <span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span> <span class="o">**</span> <span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>    <span class="n">db</span> <span class="o">=</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;logs&#39;</span><span class="p">)</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>    <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>        <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>            <span class="n">txn</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">db</span><span class="p">,</span> <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>    <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a><span class="k">def</span> <span class="nf">lmdb_reapplier</span><span class="p">(</span><span class="n">environment</span><span class="p">:</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">Environment</span><span class="p">,</span> <span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>    <span class="n">failed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>    <span class="k">while</span> <span class="n">failed</span><span class="p">:</span>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a>        <span class="n">need_to_drop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>            <span class="n">handler</span><span class="p">()</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>            <span class="n">failed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>        <span class="k">except</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">:</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a>            <span class="n">need_to_drop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>        
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>        <span class="k">if</span> <span class="n">need_to_drop</span><span class="p">:</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>            <span class="n">environment</span><span class="o">.</span><span class="n">set_mapsize</span><span class="p">(</span><span class="n">environment</span><span class="o">.</span><span class="n">info</span><span class="p">()[</span><span class="s1">&#39;map_size&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">2</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>            <span class="k">with</span> <span class="n">environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>                <span class="n">txn</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">db</span><span class="p">,</span> <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a><span class="k">class</span> <span class="nc">LoggingHandler</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">Handler</span><span class="p">):</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">log_service</span><span class="p">:</span> <span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_service</span><span class="p">:</span> <span class="n">Log</span> <span class="o">=</span> <span class="n">log_service</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">log_service</span><span class="o">.</span><span class="n">_loop</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>    <span class="k">def</span> <span class="nf">emit</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">record</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">LogRecord</span><span class="p">):</span>
</span><span id="L-685"><a href="#L-685"><span class="linenos">685</span></a>        <span class="n">log_entry</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">record</span><span class="p">)</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos">686</span></a>        <span class="n">interested_frame</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span>  <span class="c1"># TODO: mostly correct at least for a Python 3.8.10 (wrong at least for `warn()` and `exception()` logger methods)</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos">687</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-688"><a href="#L-688"><span class="linenos">688</span></a>            <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos">689</span></a>        <span class="k">except</span> <span class="n">OutsideCoroSchedulerContext</span><span class="p">:</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos">690</span></a>            <span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos">691</span></a>
</span><span id="L-692"><a href="#L-692"><span class="linenos">692</span></a>        <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos">693</span></a>            <span class="n">caller_info</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;FuncName: </span><span class="si">{</span><span class="n">record</span><span class="o">.</span><span class="n">funcName</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos">694</span></a>            <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos">695</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos">696</span></a>            <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_coro</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos">697</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="n">GreenletWorkerWrapper</span><span class="p">):</span>
</span><span id="L-698"><a href="#L-698"><span class="linenos">698</span></a>                <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="o">.</span><span class="n">worker</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos">699</span></a>            
</span><span id="L-700"><a href="#L-700"><span class="linenos">700</span></a>            <span class="n">caller_info</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;FuncName: </span><span class="si">{</span><span class="n">record</span><span class="o">.</span><span class="n">funcName</span><span class="si">}</span><span class="s1">; CoroID: </span><span class="si">{</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">; Type: </span><span class="si">{</span><span class="s2">&quot;Awaitable&quot;</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">_coro</span><span class="p">,</span><span class="w"> </span><span class="n">CoroWrapperAsyncAwait</span><span class="p">)</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s2">&quot;Greenlet&quot;</span><span class="si">}</span><span class="s1">; Worker: </span><span class="si">{</span><span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-701"><a href="#L-701"><span class="linenos">701</span></a>            <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="n">get_coro_parents_strings</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos">702</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_service</span><span class="o">.</span><span class="n">put_log_ex</span><span class="p">((</span><span class="n">log_entry</span><span class="p">,</span> <span class="p">),</span> <span class="nb">dict</span><span class="p">(),</span> <span class="p">{</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos">703</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">current_time</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">record</span><span class="o">.</span><span class="n">created</span><span class="p">),</span>
</span><span id="L-704"><a href="#L-704"><span class="linenos">704</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">perf_counter_time</span><span class="p">:</span> <span class="n">perf_counter</span><span class="p">(),</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos">705</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">file_name</span><span class="p">:</span> <span class="n">record</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos">706</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">line_number</span><span class="p">:</span> <span class="n">record</span><span class="o">.</span><span class="n">lineno</span><span class="p">,</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos">707</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">caller_info</span><span class="p">:</span> <span class="n">caller_info</span><span class="p">,</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos">708</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">traceback_strings</span><span class="p">:</span> <span class="n">format_stack</span><span class="p">(</span><span class="n">interested_frame</span><span class="p">),</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos">709</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">coro_parents_strings</span><span class="p">:</span> <span class="n">coro_parents_strings</span><span class="p">,</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos">710</span></a>            <span class="n">InfoFields</span><span class="o">.</span><span class="n">logging_level</span><span class="p">:</span> <span class="n">record</span><span class="o">.</span><span class="n">levelname</span><span class="p">,</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos">711</span></a>        <span class="p">})</span>
</span></pre></div>


            </section>
                <section id="InfoFields">
                            <input id="InfoFields-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">InfoFields</span><wbr>(<span class="base">enum.IntEnum</span>):

                <label class="view-source-button" for="InfoFields-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InfoFields"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InfoFields-111"><a href="#InfoFields-111"><span class="linenos">111</span></a><span class="k">class</span> <span class="nc">InfoFields</span><span class="p">(</span><span class="n">IntEnum</span><span class="p">):</span>
</span><span id="InfoFields-112"><a href="#InfoFields-112"><span class="linenos">112</span></a>    <span class="n">current_time</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="InfoFields-113"><a href="#InfoFields-113"><span class="linenos">113</span></a>    <span class="n">file_name</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="InfoFields-114"><a href="#InfoFields-114"><span class="linenos">114</span></a>    <span class="n">line_number</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="InfoFields-115"><a href="#InfoFields-115"><span class="linenos">115</span></a>    <span class="n">caller_info</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="InfoFields-116"><a href="#InfoFields-116"><span class="linenos">116</span></a>    <span class="n">traceback_strings</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="InfoFields-117"><a href="#InfoFields-117"><span class="linenos">117</span></a>    <span class="n">perf_counter_time</span> <span class="o">=</span> <span class="mi">5</span>
</span><span id="InfoFields-118"><a href="#InfoFields-118"><span class="linenos">118</span></a>    <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="mi">6</span>
</span><span id="InfoFields-119"><a href="#InfoFields-119"><span class="linenos">119</span></a>    <span class="n">logging_level</span> <span class="o">=</span> <span class="mi">7</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="InfoFields.current_time" class="classattr">
                                <div class="attr variable">
            <span class="name">current_time</span>        =
<span class="default_value">&lt;<a href="#InfoFields.current_time">InfoFields.current_time</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.current_time"></a>
    
    

                            </div>
                            <div id="InfoFields.file_name" class="classattr">
                                <div class="attr variable">
            <span class="name">file_name</span>        =
<span class="default_value">&lt;<a href="#InfoFields.file_name">InfoFields.file_name</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.file_name"></a>
    
    

                            </div>
                            <div id="InfoFields.line_number" class="classattr">
                                <div class="attr variable">
            <span class="name">line_number</span>        =
<span class="default_value">&lt;<a href="#InfoFields.line_number">InfoFields.line_number</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.line_number"></a>
    
    

                            </div>
                            <div id="InfoFields.caller_info" class="classattr">
                                <div class="attr variable">
            <span class="name">caller_info</span>        =
<span class="default_value">&lt;<a href="#InfoFields.caller_info">InfoFields.caller_info</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.caller_info"></a>
    
    

                            </div>
                            <div id="InfoFields.traceback_strings" class="classattr">
                                <div class="attr variable">
            <span class="name">traceback_strings</span>        =
<span class="default_value">&lt;<a href="#InfoFields.traceback_strings">InfoFields.traceback_strings</a>: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.traceback_strings"></a>
    
    

                            </div>
                            <div id="InfoFields.perf_counter_time" class="classattr">
                                <div class="attr variable">
            <span class="name">perf_counter_time</span>        =
<span class="default_value">&lt;<a href="#InfoFields.perf_counter_time">InfoFields.perf_counter_time</a>: 5&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.perf_counter_time"></a>
    
    

                            </div>
                            <div id="InfoFields.coro_parents_strings" class="classattr">
                                <div class="attr variable">
            <span class="name">coro_parents_strings</span>        =
<span class="default_value">&lt;<a href="#InfoFields.coro_parents_strings">InfoFields.coro_parents_strings</a>: 6&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.coro_parents_strings"></a>
    
    

                            </div>
                            <div id="InfoFields.logging_level" class="classattr">
                                <div class="attr variable">
            <span class="name">logging_level</span>        =
<span class="default_value">&lt;<a href="#InfoFields.logging_level">InfoFields.logging_level</a>: 7&gt;</span>

        
    </div>
    <a class="headerlink" href="#InfoFields.logging_level"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="InfoFields.name" class="variable">name</dd>
                <dd id="InfoFields.value" class="variable">value</dd>

            </div>
            <div><dt>builtins.int</dt>
                                <dd id="InfoFields.conjugate" class="function">conjugate</dd>
                <dd id="InfoFields.bit_length" class="function">bit_length</dd>
                <dd id="InfoFields.to_bytes" class="function">to_bytes</dd>
                <dd id="InfoFields.from_bytes" class="function">from_bytes</dd>
                <dd id="InfoFields.as_integer_ratio" class="function">as_integer_ratio</dd>
                <dd id="InfoFields.real" class="variable">real</dd>
                <dd id="InfoFields.imag" class="variable">imag</dd>
                <dd id="InfoFields.numerator" class="variable">numerator</dd>
                <dd id="InfoFields.denominator" class="variable">denominator</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="default_info_gatherer">
                            <input id="default_info_gatherer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">default_info_gatherer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="default_info_gatherer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#default_info_gatherer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="default_info_gatherer-122"><a href="#default_info_gatherer-122"><span class="linenos">122</span></a><span class="k">def</span> <span class="nf">default_info_gatherer</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="default_info_gatherer-123"><a href="#default_info_gatherer-123"><span class="linenos">123</span></a>    <span class="n">interested_frame</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="default_info_gatherer-124"><a href="#default_info_gatherer-124"><span class="linenos">124</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="default_info_gatherer-125"><a href="#default_info_gatherer-125"><span class="linenos">125</span></a>        <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="default_info_gatherer-126"><a href="#default_info_gatherer-126"><span class="linenos">126</span></a>    <span class="k">except</span> <span class="n">OutsideCoroSchedulerContext</span><span class="p">:</span>
</span><span id="default_info_gatherer-127"><a href="#default_info_gatherer-127"><span class="linenos">127</span></a>        <span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="default_info_gatherer-128"><a href="#default_info_gatherer-128"><span class="linenos">128</span></a>
</span><span id="default_info_gatherer-129"><a href="#default_info_gatherer-129"><span class="linenos">129</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="default_info_gatherer-130"><a href="#default_info_gatherer-130"><span class="linenos">130</span></a>        <span class="n">caller_info</span> <span class="o">=</span> <span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">interested_frame</span><span class="p">)</span>
</span><span id="default_info_gatherer-131"><a href="#default_info_gatherer-131"><span class="linenos">131</span></a>        <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="default_info_gatherer-132"><a href="#default_info_gatherer-132"><span class="linenos">132</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="default_info_gatherer-133"><a href="#default_info_gatherer-133"><span class="linenos">133</span></a>        <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_coro</span><span class="o">.</span><span class="n">worker</span>
</span><span id="default_info_gatherer-134"><a href="#default_info_gatherer-134"><span class="linenos">134</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="n">GreenletWorkerWrapper</span><span class="p">):</span>
</span><span id="default_info_gatherer-135"><a href="#default_info_gatherer-135"><span class="linenos">135</span></a>            <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="o">.</span><span class="n">worker</span>
</span><span id="default_info_gatherer-136"><a href="#default_info_gatherer-136"><span class="linenos">136</span></a>        
</span><span id="default_info_gatherer-137"><a href="#default_info_gatherer-137"><span class="linenos">137</span></a>        <span class="n">caller_info</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;CoroID: </span><span class="si">{</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">; Type: </span><span class="si">{</span><span class="s2">&quot;Awaitable&quot;</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">_coro</span><span class="p">,</span><span class="w"> </span><span class="n">CoroWrapperAsyncAwait</span><span class="p">)</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s2">&quot;Greenlet&quot;</span><span class="si">}</span><span class="s1">; Worker: </span><span class="si">{</span><span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="default_info_gatherer-138"><a href="#default_info_gatherer-138"><span class="linenos">138</span></a>        <span class="n">coro_parents_strings</span> <span class="o">=</span> <span class="n">get_coro_parents_strings</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="default_info_gatherer-139"><a href="#default_info_gatherer-139"><span class="linenos">139</span></a>    
</span><span id="default_info_gatherer-140"><a href="#default_info_gatherer-140"><span class="linenos">140</span></a>    <span class="k">return</span> <span class="p">{</span>
</span><span id="default_info_gatherer-141"><a href="#default_info_gatherer-141"><span class="linenos">141</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">current_time</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(),</span>
</span><span id="default_info_gatherer-142"><a href="#default_info_gatherer-142"><span class="linenos">142</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">perf_counter_time</span><span class="p">:</span> <span class="n">perf_counter</span><span class="p">(),</span>
</span><span id="default_info_gatherer-143"><a href="#default_info_gatherer-143"><span class="linenos">143</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">file_name</span><span class="p">:</span> <span class="n">interested_frame</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="default_info_gatherer-144"><a href="#default_info_gatherer-144"><span class="linenos">144</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">line_number</span><span class="p">:</span> <span class="n">interested_frame</span><span class="o">.</span><span class="n">f_lineno</span><span class="p">,</span>
</span><span id="default_info_gatherer-145"><a href="#default_info_gatherer-145"><span class="linenos">145</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">caller_info</span><span class="p">:</span> <span class="n">caller_info</span><span class="p">,</span>
</span><span id="default_info_gatherer-146"><a href="#default_info_gatherer-146"><span class="linenos">146</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">traceback_strings</span><span class="p">:</span> <span class="n">format_stack</span><span class="p">(</span><span class="n">interested_frame</span><span class="p">),</span>
</span><span id="default_info_gatherer-147"><a href="#default_info_gatherer-147"><span class="linenos">147</span></a>        <span class="n">InfoFields</span><span class="o">.</span><span class="n">coro_parents_strings</span><span class="p">:</span> <span class="n">coro_parents_strings</span><span class="p">,</span>
</span><span id="default_info_gatherer-148"><a href="#default_info_gatherer-148"><span class="linenos">148</span></a>    <span class="p">}</span>
</span></pre></div>


    

                </section>
                <section id="LogExtended">
                            <input id="LogExtended-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LogExtended</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.TypedServiceRequest[NoneType]</span>):

                <label class="view-source-button" for="LogExtended-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogExtended"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogExtended-151"><a href="#LogExtended-151"><span class="linenos">151</span></a><span class="k">class</span> <span class="nc">LogExtended</span><span class="p">(</span><span class="n">TypedServiceRequest</span><span class="p">[</span><span class="kc">None</span><span class="p">]):</span>
</span><span id="LogExtended-152"><a href="#LogExtended-152"><span class="linenos">152</span></a>    <span class="n">default__request__type__</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="LogExtended-153"><a href="#LogExtended-153"><span class="linenos">153</span></a>
</span><span id="LogExtended-154"><a href="#LogExtended-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="LogExtended-155"><a href="#LogExtended-155"><span class="linenos">155</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="LogExtended-156"><a href="#LogExtended-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">info_gatherer</span>
</span><span id="LogExtended-157"><a href="#LogExtended-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">depth</span>
</span><span id="LogExtended-158"><a href="#LogExtended-158"><span class="linenos">158</span></a>    
</span><span id="LogExtended-159"><a href="#LogExtended-159"><span class="linenos">159</span></a>    <span class="k">def</span> <span class="nf">_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LogExtended&#39;</span><span class="p">:</span>
</span><span id="LogExtended-160"><a href="#LogExtended-160"><span class="linenos">160</span></a>        <span class="k">return</span> <span class="n">LogExtended</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">depth</span><span class="p">)</span>
</span><span id="LogExtended-161"><a href="#LogExtended-161"><span class="linenos">161</span></a>
</span><span id="LogExtended-162"><a href="#LogExtended-162"><span class="linenos">162</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LogEx&#39;</span><span class="p">:</span>
</span><span id="LogExtended-163"><a href="#LogExtended-163"><span class="linenos">163</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LogExtended-164"><a href="#LogExtended-164"><span class="linenos">164</span></a>            <span class="n">info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LogExtended-165"><a href="#LogExtended-165"><span class="linenos">165</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogExtended-166"><a href="#LogExtended-166"><span class="linenos">166</span></a>            <span class="n">info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="LogExtended-167"><a href="#LogExtended-167"><span class="linenos">167</span></a>        
</span><span id="LogExtended-168"><a href="#LogExtended-168"><span class="linenos">168</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save_to_copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default__request__type__</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">)</span>
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


                            <div id="LogExtended.__init__" class="classattr">
                                        <input id="LogExtended.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LogExtended</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">depth</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span>)</span>

                <label class="view-source-button" for="LogExtended.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogExtended.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogExtended.__init__-154"><a href="#LogExtended.__init__-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="LogExtended.__init__-155"><a href="#LogExtended.__init__-155"><span class="linenos">155</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="LogExtended.__init__-156"><a href="#LogExtended.__init__-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">info_gatherer</span>
</span><span id="LogExtended.__init__-157"><a href="#LogExtended.__init__-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">depth</span>
</span></pre></div>


    

                            </div>
                            <div id="LogExtended.default__request__type__" class="classattr">
                                <div class="attr variable">
            <span class="name">default__request__type__</span><span class="annotation">: int</span>        =
<span class="default_value">4</span>

        
    </div>
    <a class="headerlink" href="#LogExtended.default__request__type__"></a>
    
    

                            </div>
                            <div id="LogExtended.info_gatherer" class="classattr">
                                <div class="attr variable">
            <span class="name">info_gatherer</span><span class="annotation">: Union[Callable, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#LogExtended.info_gatherer"></a>
    
    

                            </div>
                            <div id="LogExtended.depth" class="classattr">
                                <div class="attr variable">
            <span class="name">depth</span><span class="annotation">: Union[int, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#LogExtended.depth"></a>
    
    

                            </div>
                            <div id="LogExtended.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<span class="default_value">&lt;class &#39;<a href="#Log">Log</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#LogExtended.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="LogExtended.request_type" class="variable">request_type</dd>
                <dd id="LogExtended.args" class="variable">args</dd>
                <dd id="LogExtended.kwargs" class="variable">kwargs</dd>
                <dd id="LogExtended.provide_to_request_handler" class="variable">provide_to_request_handler</dd>
                <dd id="LogExtended.interface" class="function">interface</dd>
                <dd id="LogExtended.i" class="function">i</dd>
                <dd id="LogExtended.async_interface" class="function">async_interface</dd>
                <dd id="LogExtended.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LogEx">
                    <div class="attr variable">
            <span class="name">LogEx</span>        =
<input id="LogEx-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="LogEx-view-value"></label><span class="default_value">&lt;class &#39;<a href="#LogExtended">LogExtended</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#LogEx"></a>
    
    

                </section>
                <section id="Log">
                            <input id="Log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Log</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.TypedService[NoneType]</span>, <span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="Log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log-197"><a href="#Log-197"><span class="linenos">197</span></a><span class="k">class</span> <span class="nc">Log</span><span class="p">(</span><span class="n">TypedService</span><span class="p">[</span><span class="kc">None</span><span class="p">],</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="Log-198"><a href="#Log-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Log-199"><a href="#Log-199"><span class="linenos">199</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="Log-200"><a href="#Log-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_logs_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;log.db&#39;</span>
</span><span id="Log-201"><a href="#Log-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-202"><a href="#Log-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-203"><a href="#Log-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">root_path_to_log_environment_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-204"><a href="#Log-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">:</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">Environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-205"><a href="#Log-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-206"><a href="#Log-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log-207"><a href="#Log-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-208"><a href="#Log-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="Log-209"><a href="#Log-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">=</span> <span class="mf">0.5</span>
</span><span id="Log-210"><a href="#Log-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span> <span class="o">=</span> <span class="mi">16</span>
</span><span id="Log-211"><a href="#Log-211"><span class="linenos">211</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span>
</span><span id="Log-212"><a href="#Log-212"><span class="linenos">212</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Log-213"><a href="#Log-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-214"><a href="#Log-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-215"><a href="#Log-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-216"><a href="#Log-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-217"><a href="#Log-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log-218"><a href="#Log-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Log-219"><a href="#Log-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">,</span> <span class="n">LoggingHandler</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Log-220"><a href="#Log-220"><span class="linenos">220</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span>
</span><span id="Log-221"><a href="#Log-221"><span class="linenos">221</span></a>        <span class="c1"># self.serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="Log-222"><a href="#Log-222"><span class="linenos">222</span></a>        <span class="c1">#                                    Tags.can_use_bytes,</span>
</span><span id="Log-223"><a href="#Log-223"><span class="linenos">223</span></a>        <span class="c1">#                                    Tags.decode_str_as_str,</span>
</span><span id="Log-224"><a href="#Log-224"><span class="linenos">224</span></a>        <span class="c1">#                                    Tags.decode_list_as_list,</span>
</span><span id="Log-225"><a href="#Log-225"><span class="linenos">225</span></a>        <span class="c1">#                                    Tags.decode_bytes_as_bytes,</span>
</span><span id="Log-226"><a href="#Log-226"><span class="linenos">226</span></a>        <span class="c1">#                                    Tags.superficial,</span>
</span><span id="Log-227"><a href="#Log-227"><span class="linenos">227</span></a>        <span class="c1">#                                    Tags.current_platform,</span>
</span><span id="Log-228"><a href="#Log-228"><span class="linenos">228</span></a>        <span class="c1">#                                    Tags.multi_platform),</span>
</span><span id="Log-229"><a href="#Log-229"><span class="linenos">229</span></a>        <span class="c1">#                                   TestDataType.small,</span>
</span><span id="Log-230"><a href="#Log-230"><span class="linenos">230</span></a>        <span class="c1">#                                   0.1)</span>
</span><span id="Log-231"><a href="#Log-231"><span class="linenos">231</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="Log-232"><a href="#Log-232"><span class="linenos">232</span></a>
</span><span id="Log-233"><a href="#Log-233"><span class="linenos">233</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Log-234"><a href="#Log-234"><span class="linenos">234</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_db_environment_path</span><span class="p">,</span>
</span><span id="Log-235"><a href="#Log-235"><span class="linenos">235</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_sync</span><span class="p">,</span>
</span><span id="Log-236"><a href="#Log-236"><span class="linenos">236</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_add_iteration_handler</span><span class="p">,</span>
</span><span id="Log-237"><a href="#Log-237"><span class="linenos">237</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_remove_iteration_handler</span><span class="p">,</span>
</span><span id="Log-238"><a href="#Log-238"><span class="linenos">238</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_log_extended</span><span class="p">,</span>
</span><span id="Log-239"><a href="#Log-239"><span class="linenos">239</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_connect_to_logger</span><span class="p">,</span>
</span><span id="Log-240"><a href="#Log-240"><span class="linenos">240</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_disconnect_from_logger</span><span class="p">,</span>
</span><span id="Log-241"><a href="#Log-241"><span class="linenos">241</span></a>        <span class="p">}</span>
</span><span id="Log-242"><a href="#Log-242"><span class="linenos">242</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">inject_handler_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="p">)</span>
</span><span id="Log-243"><a href="#Log-243"><span class="linenos">243</span></a>
</span><span id="Log-244"><a href="#Log-244"><span class="linenos">244</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="Log-245"><a href="#Log-245"><span class="linenos">245</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="Log-246"><a href="#Log-246"><span class="linenos">246</span></a>            <span class="s1">&#39;log counter&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
</span><span id="Log-247"><a href="#Log-247"><span class="linenos">247</span></a>            <span class="s1">&#39;current counter state key&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span>
</span><span id="Log-248"><a href="#Log-248"><span class="linenos">248</span></a>        <span class="p">}</span>
</span><span id="Log-249"><a href="#Log-249"><span class="linenos">249</span></a>    
</span><span id="Log-250"><a href="#Log-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="Log-251"><a href="#Log-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="Log-252"><a href="#Log-252"><span class="linenos">252</span></a>        <span class="c1"># self.make_live</span>
</span><span id="Log-253"><a href="#Log-253"><span class="linenos">253</span></a>    
</span><span id="Log-254"><a href="#Log-254"><span class="linenos">254</span></a>    <span class="k">def</span> <span class="nf">put_log_ex</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">):</span>
</span><span id="Log-255"><a href="#Log-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span><span id="Log-256"><a href="#Log-256"><span class="linenos">256</span></a>
</span><span id="Log-257"><a href="#Log-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log-258"><a href="#Log-258"><span class="linenos">258</span></a>        <span class="c1"># TODO: we need to use some loop destroy service in order to put our coro which will write all pending queues,</span>
</span><span id="Log-259"><a href="#Log-259"><span class="linenos">259</span></a>        <span class="c1"># sync envirounments and close them. Also we need to prevent new requests from being processed. (see DB service)</span>
</span><span id="Log-260"><a href="#Log-260"><span class="linenos">260</span></a>        <span class="n">loggers_instancess</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="Log-261"><a href="#Log-261"><span class="linenos">261</span></a>        <span class="k">for</span> <span class="n">logger_instance</span> <span class="ow">in</span> <span class="n">loggers_instancess</span><span class="p">:</span>
</span><span id="Log-262"><a href="#Log-262"><span class="linenos">262</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">eject_handler_from_logger</span><span class="p">(</span><span class="n">logger_instance</span><span class="p">)</span>
</span><span id="Log-263"><a href="#Log-263"><span class="linenos">263</span></a>
</span><span id="Log-264"><a href="#Log-264"><span class="linenos">264</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-265"><a href="#Log-265"><span class="linenos">265</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="Log-266"><a href="#Log-266"><span class="linenos">266</span></a>
</span><span id="Log-267"><a href="#Log-267"><span class="linenos">267</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Log-268"><a href="#Log-268"><span class="linenos">268</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="Log-269"><a href="#Log-269"><span class="linenos">269</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_resolve_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Log-270"><a href="#Log-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-271"><a href="#Log-271"><span class="linenos">271</span></a>            <span class="n">coro_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span>
</span><span id="Log-272"><a href="#Log-272"><span class="linenos">272</span></a>            <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">worker</span>
</span><span id="Log-273"><a href="#Log-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="n">GreenletWorkerWrapper</span><span class="p">):</span>
</span><span id="Log-274"><a href="#Log-274"><span class="linenos">274</span></a>                <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="o">.</span><span class="n">worker</span>
</span><span id="Log-275"><a href="#Log-275"><span class="linenos">275</span></a>            
</span><span id="Log-276"><a href="#Log-276"><span class="linenos">276</span></a>            <span class="n">caller_info</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;CoroID: </span><span class="si">{</span><span class="n">coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">; Type: </span><span class="si">{</span><span class="s2">&quot;Awaitable&quot;</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="nb">issubclass</span><span class="p">(</span><span class="n">coro_info</span><span class="o">.</span><span class="n">coro_type</span><span class="p">,</span><span class="w"> </span><span class="n">CoroWrapperAsyncAwait</span><span class="p">)</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s2">&quot;Greenlet&quot;</span><span class="si">}</span><span class="s1">; Worker: </span><span class="si">{</span><span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="Log-277"><a href="#Log-277"><span class="linenos">277</span></a>            <span class="n">coro_worker_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="Log-278"><a href="#Log-278"><span class="linenos">278</span></a>            <span class="n">info</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Log-279"><a href="#Log-279"><span class="linenos">279</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">current_time</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(),</span>
</span><span id="Log-280"><a href="#Log-280"><span class="linenos">280</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">perf_counter_time</span><span class="p">:</span> <span class="n">perf_counter</span><span class="p">(),</span>
</span><span id="Log-281"><a href="#Log-281"><span class="linenos">281</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">file_name</span><span class="p">:</span> <span class="n">coro_worker_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="Log-282"><a href="#Log-282"><span class="linenos">282</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">line_number</span><span class="p">:</span> <span class="n">coro_worker_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="Log-283"><a href="#Log-283"><span class="linenos">283</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">caller_info</span><span class="p">:</span> <span class="n">caller_info</span><span class="p">,</span>
</span><span id="Log-284"><a href="#Log-284"><span class="linenos">284</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">traceback_strings</span><span class="p">:</span> <span class="nb">list</span><span class="p">(),</span>
</span><span id="Log-285"><a href="#Log-285"><span class="linenos">285</span></a>                <span class="c1"># InfoFields.coro_parents_strings: get_coro_parents_strings(coro_info.coro_id),</span>
</span><span id="Log-286"><a href="#Log-286"><span class="linenos">286</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">coro_parents_strings</span><span class="p">:</span> <span class="nb">list</span><span class="p">(),</span>
</span><span id="Log-287"><a href="#Log-287"><span class="linenos">287</span></a>            <span class="p">}</span>
</span><span id="Log-288"><a href="#Log-288"><span class="linenos">288</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span><span id="Log-289"><a href="#Log-289"><span class="linenos">289</span></a>            <span class="c1"># self.make_live()</span>
</span><span id="Log-290"><a href="#Log-290"><span class="linenos">290</span></a>
</span><span id="Log-291"><a href="#Log-291"><span class="linenos">291</span></a>            <span class="c1"># TODO: we need to implement backpressure mechanism here. If we have too many pending requests, we need to put request to queue instead of responding immediately.</span>
</span><span id="Log-292"><a href="#Log-292"><span class="linenos">292</span></a>            <span class="c1"># However this will not be enough for a direct requests. We need to implement some kind of backpressure mechanism for direct requests too.</span>
</span><span id="Log-293"><a href="#Log-293"><span class="linenos">293</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-294"><a href="#Log-294"><span class="linenos">294</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log-295"><a href="#Log-295"><span class="linenos">295</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="Log-296"><a href="#Log-296"><span class="linenos">296</span></a>
</span><span id="Log-297"><a href="#Log-297"><span class="linenos">297</span></a>    <span class="k">def</span> <span class="nf">_ensure_default_db_environment</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Log-298"><a href="#Log-298"><span class="linenos">298</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-299"><a href="#Log-299"><span class="linenos">299</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-300"><a href="#Log-300"><span class="linenos">300</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-301"><a href="#Log-301"><span class="linenos">301</span></a>                    <span class="k">async</span> <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">):</span>
</span><span id="Log-302"><a href="#Log-302"><span class="linenos">302</span></a>                        <span class="n">app_name_for_fs</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="s1">&#39;app_name_for_fs&#39;</span><span class="p">))</span>
</span><span id="Log-303"><a href="#Log-303"><span class="linenos">303</span></a>                        <span class="n">app_data_dir_path_type</span><span class="p">:</span> <span class="n">AppDirectoryType</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="s1">&#39;app_data_dir_path_type&#39;</span><span class="p">))</span>
</span><span id="Log-304"><a href="#Log-304"><span class="linenos">304</span></a>                        <span class="n">app_dir_path</span><span class="p">:</span> <span class="n">AppDirPath</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">AppDirPath</span><span class="p">))</span>
</span><span id="Log-305"><a href="#Log-305"><span class="linenos">305</span></a>                        <span class="n">app_data_dir_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">app_dir_path</span><span class="o">.</span><span class="n">cached</span><span class="p">(</span><span class="n">app_data_dir_path_type</span><span class="p">,</span> <span class="n">app_name_for_fs</span><span class="p">)</span>
</span><span id="Log-306"><a href="#Log-306"><span class="linenos">306</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">app_data_dir_path</span><span class="p">)(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_logs_dir</span><span class="p">)</span>
</span><span id="Log-307"><a href="#Log-307"><span class="linenos">307</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="Log-308"><a href="#Log-308"><span class="linenos">308</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-309"><a href="#Log-309"><span class="linenos">309</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Log-310"><a href="#Log-310"><span class="linenos">310</span></a>                    
</span><span id="Log-311"><a href="#Log-311"><span class="linenos">311</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span> <span class="o">=</span> <span class="n">put_root_from_other_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="Log-312"><a href="#Log-312"><span class="linenos">312</span></a>                
</span><span id="Log-313"><a href="#Log-313"><span class="linenos">313</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="Log-314"><a href="#Log-314"><span class="linenos">314</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="Log-315"><a href="#Log-315"><span class="linenos">315</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Log-316"><a href="#Log-316"><span class="linenos">316</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="Log-317"><a href="#Log-317"><span class="linenos">317</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="Log-318"><a href="#Log-318"><span class="linenos">318</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log-319"><a href="#Log-319"><span class="linenos">319</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="Log-320"><a href="#Log-320"><span class="linenos">320</span></a>
</span><span id="Log-321"><a href="#Log-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log-322"><a href="#Log-322"><span class="linenos">322</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_default_db_environment</span><span class="p">():</span>
</span><span id="Log-323"><a href="#Log-323"><span class="linenos">323</span></a>            <span class="k">return</span>
</span><span id="Log-324"><a href="#Log-324"><span class="linenos">324</span></a>        
</span><span id="Log-325"><a href="#Log-325"><span class="linenos">325</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-326"><a href="#Log-326"><span class="linenos">326</span></a>        <span class="n">log_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span>
</span><span id="Log-327"><a href="#Log-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">log_queue_buff</span><span class="p">)()</span>
</span><span id="Log-328"><a href="#Log-328"><span class="linenos">328</span></a>        <span class="n">current_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Log-329"><a href="#Log-329"><span class="linenos">329</span></a>        <span class="n">current_time_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">current_time</span><span class="p">)</span>
</span><span id="Log-330"><a href="#Log-330"><span class="linenos">330</span></a>        <span class="k">for</span> <span class="n">iteration_handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="p">:</span>
</span><span id="Log-331"><a href="#Log-331"><span class="linenos">331</span></a>            <span class="n">iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">log_queue_buff</span><span class="p">,</span> <span class="n">current_time</span><span class="p">,</span> <span class="n">current_time_str</span><span class="p">)</span>
</span><span id="Log-332"><a href="#Log-332"><span class="linenos">332</span></a>        
</span><span id="Log-333"><a href="#Log-333"><span class="linenos">333</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Log-334"><a href="#Log-334"><span class="linenos">334</span></a>
</span><span id="Log-335"><a href="#Log-335"><span class="linenos">335</span></a>        <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="Log-336"><a href="#Log-336"><span class="linenos">336</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Log-337"><a href="#Log-337"><span class="linenos">337</span></a>                <span class="k">for</span> <span class="n">log_info</span> <span class="ow">in</span> <span class="n">log_queue_buff</span><span class="p">:</span>
</span><span id="Log-338"><a href="#Log-338"><span class="linenos">338</span></a>                    <span class="n">key</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">get</span><span class="p">())</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span><span class="p">)</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="n">current_time_str</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span>
</span><span id="Log-339"><a href="#Log-339"><span class="linenos">339</span></a>                    <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">log_info</span><span class="p">)</span>
</span><span id="Log-340"><a href="#Log-340"><span class="linenos">340</span></a>                    <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">dupdata</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Log-341"><a href="#Log-341"><span class="linenos">341</span></a>                
</span><span id="Log-342"><a href="#Log-342"><span class="linenos">342</span></a>                <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">),</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span>
</span><span id="Log-343"><a href="#Log-343"><span class="linenos">343</span></a>        
</span><span id="Log-344"><a href="#Log-344"><span class="linenos">344</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="Log-345"><a href="#Log-345"><span class="linenos">345</span></a>        
</span><span id="Log-346"><a href="#Log-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="Log-347"><a href="#Log-347"><span class="linenos">347</span></a>        
</span><span id="Log-348"><a href="#Log-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Log-349"><a href="#Log-349"><span class="linenos">349</span></a>
</span><span id="Log-350"><a href="#Log-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="Log-351"><a href="#Log-351"><span class="linenos">351</span></a>
</span><span id="Log-352"><a href="#Log-352"><span class="linenos">352</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Log-353"><a href="#Log-353"><span class="linenos">353</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">)</span> \
</span><span id="Log-354"><a href="#Log-354"><span class="linenos">354</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> \
</span><span id="Log-355"><a href="#Log-355"><span class="linenos">355</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span><span class="p">)</span> \
</span><span id="Log-356"><a href="#Log-356"><span class="linenos">356</span></a>            <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> \
</span><span id="Log-357"><a href="#Log-357"><span class="linenos">357</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="ow">or</span> <span class="p">((</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">)</span> <span class="ow">and</span> <span class="p">((</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">)))</span>
</span><span id="Log-358"><a href="#Log-358"><span class="linenos">358</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="Log-359"><a href="#Log-359"><span class="linenos">359</span></a>    
</span><span id="Log-360"><a href="#Log-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="Log-361"><a href="#Log-361"><span class="linenos">361</span></a>        <span class="n">time_since_last_sync_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span>
</span><span id="Log-362"><a href="#Log-362"><span class="linenos">362</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">&gt;</span> <span class="n">time_since_last_sync_time</span><span class="p">:</span>
</span><span id="Log-363"><a href="#Log-363"><span class="linenos">363</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">-</span> <span class="n">time_since_last_sync_time</span>
</span><span id="Log-364"><a href="#Log-364"><span class="linenos">364</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log-365"><a href="#Log-365"><span class="linenos">365</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="mi">0</span>
</span><span id="Log-366"><a href="#Log-366"><span class="linenos">366</span></a>
</span><span id="Log-367"><a href="#Log-367"><span class="linenos">367</span></a>    <span class="k">def</span> <span class="nf">_init_db</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log-368"><a href="#Log-368"><span class="linenos">368</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Path to Log DB Env: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="Log-369"><a href="#Log-369"><span class="linenos">369</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
</span><span id="Log-370"><a href="#Log-370"><span class="linenos">370</span></a>                                        <span class="n">map_async</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">lock</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">metasync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">sync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">meminit</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="Log-371"><a href="#Log-371"><span class="linenos">371</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;logs&#39;</span><span class="p">)</span>
</span><span id="Log-372"><a href="#Log-372"><span class="linenos">372</span></a>        <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="Log-373"><a href="#Log-373"><span class="linenos">373</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Log-374"><a href="#Log-374"><span class="linenos">374</span></a>                <span class="n">current_counter_state</span> <span class="o">=</span> <span class="n">txn</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span>
</span><span id="Log-375"><a href="#Log-375"><span class="linenos">375</span></a>                <span class="k">if</span> <span class="n">current_counter_state</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-376"><a href="#Log-376"><span class="linenos">376</span></a>                    <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">),</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span>
</span><span id="Log-377"><a href="#Log-377"><span class="linenos">377</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="Log-378"><a href="#Log-378"><span class="linenos">378</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">current_counter_state</span><span class="p">)</span>
</span><span id="Log-379"><a href="#Log-379"><span class="linenos">379</span></a>        
</span><span id="Log-380"><a href="#Log-380"><span class="linenos">380</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="Log-381"><a href="#Log-381"><span class="linenos">381</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Log-382"><a href="#Log-382"><span class="linenos">382</span></a>
</span><span id="Log-383"><a href="#Log-383"><span class="linenos">383</span></a>    <span class="k">def</span> <span class="nf">_on_set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="Log-384"><a href="#Log-384"><span class="linenos">384</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">:</span>
</span><span id="Log-385"><a href="#Log-385"><span class="linenos">385</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-386"><a href="#Log-386"><span class="linenos">386</span></a>        
</span><span id="Log-387"><a href="#Log-387"><span class="linenos">387</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-388"><a href="#Log-388"><span class="linenos">388</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_to_db_environment</span>
</span><span id="Log-389"><a href="#Log-389"><span class="linenos">389</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Log-390"><a href="#Log-390"><span class="linenos">390</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="Log-391"><a href="#Log-391"><span class="linenos">391</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="Log-392"><a href="#Log-392"><span class="linenos">392</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Log-393"><a href="#Log-393"><span class="linenos">393</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="Log-394"><a href="#Log-394"><span class="linenos">394</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-395"><a href="#Log-395"><span class="linenos">395</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log-396"><a href="#Log-396"><span class="linenos">396</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-397"><a href="#Log-397"><span class="linenos">397</span></a>    
</span><span id="Log-398"><a href="#Log-398"><span class="linenos">398</span></a>    <span class="k">def</span> <span class="nf">_on_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log-399"><a href="#Log-399"><span class="linenos">399</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-400"><a href="#Log-400"><span class="linenos">400</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Log-401"><a href="#Log-401"><span class="linenos">401</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log-402"><a href="#Log-402"><span class="linenos">402</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">:</span>
</span><span id="Log-403"><a href="#Log-403"><span class="linenos">403</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Log-404"><a href="#Log-404"><span class="linenos">404</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Log-405"><a href="#Log-405"><span class="linenos">405</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Log-406"><a href="#Log-406"><span class="linenos">406</span></a>                <span class="c1"># self.db_environment.sync(True)</span>
</span><span id="Log-407"><a href="#Log-407"><span class="linenos">407</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="Log-408"><a href="#Log-408"><span class="linenos">408</span></a>        
</span><span id="Log-409"><a href="#Log-409"><span class="linenos">409</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-410"><a href="#Log-410"><span class="linenos">410</span></a>
</span><span id="Log-411"><a href="#Log-411"><span class="linenos">411</span></a>    <span class="k">def</span> <span class="nf">_on_log_extended</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">):</span>
</span><span id="Log-412"><a href="#Log-412"><span class="linenos">412</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span><span id="Log-413"><a href="#Log-413"><span class="linenos">413</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-414"><a href="#Log-414"><span class="linenos">414</span></a>
</span><span id="Log-415"><a href="#Log-415"><span class="linenos">415</span></a>    <span class="k">def</span> <span class="nf">_on_add_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]):</span>
</span><span id="Log-416"><a href="#Log-416"><span class="linenos">416</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="Log-417"><a href="#Log-417"><span class="linenos">417</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Log-418"><a href="#Log-418"><span class="linenos">418</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-419"><a href="#Log-419"><span class="linenos">419</span></a>    
</span><span id="Log-420"><a href="#Log-420"><span class="linenos">420</span></a>    <span class="k">def</span> <span class="nf">_on_remove_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]):</span>
</span><span id="Log-421"><a href="#Log-421"><span class="linenos">421</span></a>        <span class="n">removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-422"><a href="#Log-422"><span class="linenos">422</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="Log-423"><a href="#Log-423"><span class="linenos">423</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="Log-424"><a href="#Log-424"><span class="linenos">424</span></a>            <span class="n">removed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Log-425"><a href="#Log-425"><span class="linenos">425</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="Log-426"><a href="#Log-426"><span class="linenos">426</span></a>            <span class="k">pass</span>
</span><span id="Log-427"><a href="#Log-427"><span class="linenos">427</span></a>
</span><span id="Log-428"><a href="#Log-428"><span class="linenos">428</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">removed</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-429"><a href="#Log-429"><span class="linenos">429</span></a>
</span><span id="Log-430"><a href="#Log-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">sync_in_thread_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log-431"><a href="#Log-431"><span class="linenos">431</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Log-432"><a href="#Log-432"><span class="linenos">432</span></a>            <span class="k">if</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span>
</span><span id="Log-433"><a href="#Log-433"><span class="linenos">433</span></a>                <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">,</span> <span class="kc">True</span><span class="p">))</span>
</span><span id="Log-434"><a href="#Log-434"><span class="linenos">434</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Log-435"><a href="#Log-435"><span class="linenos">435</span></a>                <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-436"><a href="#Log-436"><span class="linenos">436</span></a>                    <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="Log-437"><a href="#Log-437"><span class="linenos">437</span></a>            
</span><span id="Log-438"><a href="#Log-438"><span class="linenos">438</span></a>            <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">):</span>
</span><span id="Log-439"><a href="#Log-439"><span class="linenos">439</span></a>                <span class="k">def</span> <span class="nf">sync_worker</span><span class="p">():</span>
</span><span id="Log-440"><a href="#Log-440"><span class="linenos">440</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Log-441"><a href="#Log-441"><span class="linenos">441</span></a>                
</span><span id="Log-442"><a href="#Log-442"><span class="linenos">442</span></a>                <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">sync_worker</span><span class="p">)</span>
</span><span id="Log-443"><a href="#Log-443"><span class="linenos">443</span></a>
</span><span id="Log-444"><a href="#Log-444"><span class="linenos">444</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">)))</span>
</span><span id="Log-445"><a href="#Log-445"><span class="linenos">445</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-446"><a href="#Log-446"><span class="linenos">446</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-447"><a href="#Log-447"><span class="linenos">447</span></a>            <span class="k">def</span> <span class="nf">make_service_live_for_a_next_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">):</span>
</span><span id="Log-448"><a href="#Log-448"><span class="linenos">448</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-449"><a href="#Log-449"><span class="linenos">449</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Log-450"><a href="#Log-450"><span class="linenos">450</span></a>            
</span><span id="Log-451"><a href="#Log-451"><span class="linenos">451</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">,</span> <span class="n">make_service_live_for_a_next_sync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="Log-452"><a href="#Log-452"><span class="linenos">452</span></a>
</span><span id="Log-453"><a href="#Log-453"><span class="linenos">453</span></a>        <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log-454"><a href="#Log-454"><span class="linenos">454</span></a>        <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log-455"><a href="#Log-455"><span class="linenos">455</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="Log-456"><a href="#Log-456"><span class="linenos">456</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">()</span>
</span><span id="Log-457"><a href="#Log-457"><span class="linenos">457</span></a>        <span class="k">except</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">:</span>
</span><span id="Log-458"><a href="#Log-458"><span class="linenos">458</span></a>            <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Log-459"><a href="#Log-459"><span class="linenos">459</span></a>
</span><span id="Log-460"><a href="#Log-460"><span class="linenos">460</span></a>        <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">sync_db_coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">)</span>
</span><span id="Log-461"><a href="#Log-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Log-462"><a href="#Log-462"><span class="linenos">462</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="Log-463"><a href="#Log-463"><span class="linenos">463</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Log-464"><a href="#Log-464"><span class="linenos">464</span></a>    
</span><span id="Log-465"><a href="#Log-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">get_last_n_logs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">number</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]:</span>
</span><span id="Log-466"><a href="#Log-466"><span class="linenos">466</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-467"><a href="#Log-467"><span class="linenos">467</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log-468"><a href="#Log-468"><span class="linenos">468</span></a>        
</span><span id="Log-469"><a href="#Log-469"><span class="linenos">469</span></a>        <span class="k">if</span> <span class="n">number</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log-470"><a href="#Log-470"><span class="linenos">470</span></a>            <span class="n">number</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="Log-471"><a href="#Log-471"><span class="linenos">471</span></a>        <span class="k">elif</span> <span class="n">number</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="Log-472"><a href="#Log-472"><span class="linenos">472</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log-473"><a href="#Log-473"><span class="linenos">473</span></a>        
</span><span id="Log-474"><a href="#Log-474"><span class="linenos">474</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log-475"><a href="#Log-475"><span class="linenos">475</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Log-476"><a href="#Log-476"><span class="linenos">476</span></a>            <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span><span class="o">.</span><span class="n">last</span><span class="p">()</span>
</span><span id="Log-477"><a href="#Log-477"><span class="linenos">477</span></a>            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span><span class="o">.</span><span class="n">iterprev</span><span class="p">():</span>
</span><span id="Log-478"><a href="#Log-478"><span class="linenos">478</span></a>                <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">:</span>
</span><span id="Log-479"><a href="#Log-479"><span class="linenos">479</span></a>                    <span class="k">continue</span>
</span><span id="Log-480"><a href="#Log-480"><span class="linenos">480</span></a>
</span><span id="Log-481"><a href="#Log-481"><span class="linenos">481</span></a>                <span class="k">if</span> <span class="n">number</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="Log-482"><a href="#Log-482"><span class="linenos">482</span></a>                    <span class="k">break</span>
</span><span id="Log-483"><a href="#Log-483"><span class="linenos">483</span></a>
</span><span id="Log-484"><a href="#Log-484"><span class="linenos">484</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>
</span><span id="Log-485"><a href="#Log-485"><span class="linenos">485</span></a>                <span class="n">number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="Log-486"><a href="#Log-486"><span class="linenos">486</span></a>        
</span><span id="Log-487"><a href="#Log-487"><span class="linenos">487</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">reverse</span><span class="p">()</span>
</span><span id="Log-488"><a href="#Log-488"><span class="linenos">488</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Log-489"><a href="#Log-489"><span class="linenos">489</span></a>
</span><span id="Log-490"><a href="#Log-490"><span class="linenos">490</span></a>    <span class="k">def</span> <span class="nf">inject_handler_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Log-491"><a href="#Log-491"><span class="linenos">491</span></a>        <span class="k">if</span> <span class="n">logger_instance</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span>
</span><span id="Log-492"><a href="#Log-492"><span class="linenos">492</span></a>            <span class="n">logger_handler</span><span class="p">:</span> <span class="n">LoggingHandler</span> <span class="o">=</span> <span class="n">LoggingHandler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="Log-493"><a href="#Log-493"><span class="linenos">493</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">]</span> <span class="o">=</span> <span class="n">logger_handler</span>
</span><span id="Log-494"><a href="#Log-494"><span class="linenos">494</span></a>            <span class="n">logger_instance</span><span class="o">.</span><span class="n">addHandler</span><span class="p">(</span><span class="n">logger_handler</span><span class="p">)</span>
</span><span id="Log-495"><a href="#Log-495"><span class="linenos">495</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="Log-496"><a href="#Log-496"><span class="linenos">496</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log-497"><a href="#Log-497"><span class="linenos">497</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="Log-498"><a href="#Log-498"><span class="linenos">498</span></a>
</span><span id="Log-499"><a href="#Log-499"><span class="linenos">499</span></a>    <span class="k">def</span> <span class="nf">_on_connect_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">):</span>
</span><span id="Log-500"><a href="#Log-500"><span class="linenos">500</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">inject_handler_to_logger</span><span class="p">(</span><span class="n">logger_instance</span><span class="p">)</span>
</span><span id="Log-501"><a href="#Log-501"><span class="linenos">501</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log-502"><a href="#Log-502"><span class="linenos">502</span></a>
</span><span id="Log-503"><a href="#Log-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="nf">eject_handler_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Log-504"><a href="#Log-504"><span class="linenos">504</span></a>        <span class="k">if</span> <span class="n">logger_instance</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span>
</span><span id="Log-505"><a href="#Log-505"><span class="linenos">505</span></a>            <span class="n">logger_instance</span><span class="o">.</span><span class="n">removeHandler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">])</span>
</span><span id="Log-506"><a href="#Log-506"><span class="linenos">506</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">]</span>
</span><span id="Log-507"><a href="#Log-507"><span class="linenos">507</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="Log-508"><a href="#Log-508"><span class="linenos">508</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log-509"><a href="#Log-509"><span class="linenos">509</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="Log-510"><a href="#Log-510"><span class="linenos">510</span></a>
</span><span id="Log-511"><a href="#Log-511"><span class="linenos">511</span></a>    <span class="k">def</span> <span class="nf">_on_disconnect_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">):</span>
</span><span id="Log-512"><a href="#Log-512"><span class="linenos">512</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">eject_handler_from_logger</span><span class="p">(</span><span class="n">logger_instance</span><span class="p">)</span>
</span><span id="Log-513"><a href="#Log-513"><span class="linenos">513</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
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


                            <div id="Log.__init__" class="classattr">
                                        <input id="Log.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Log</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="Log.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.__init__-198"><a href="#Log.__init__-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Log.__init__-199"><a href="#Log.__init__-199"><span class="linenos">199</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="Log.__init__-200"><a href="#Log.__init__-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_logs_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;log.db&#39;</span>
</span><span id="Log.__init__-201"><a href="#Log.__init__-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.__init__-202"><a href="#Log.__init__-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">app_name_waiter</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.__init__-203"><a href="#Log.__init__-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">root_path_to_log_environment_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.__init__-204"><a href="#Log.__init__-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">:</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">Environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.__init__-205"><a href="#Log.__init__-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.__init__-206"><a href="#Log.__init__-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log.__init__-207"><a href="#Log.__init__-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.__init__-208"><a href="#Log.__init__-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="Log.__init__-209"><a href="#Log.__init__-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">=</span> <span class="mf">0.5</span>
</span><span id="Log.__init__-210"><a href="#Log.__init__-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span> <span class="o">=</span> <span class="mi">16</span>
</span><span id="Log.__init__-211"><a href="#Log.__init__-211"><span class="linenos">211</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span>
</span><span id="Log.__init__-212"><a href="#Log.__init__-212"><span class="linenos">212</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Log.__init__-213"><a href="#Log.__init__-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log.__init__-214"><a href="#Log.__init__-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log.__init__-215"><a href="#Log.__init__-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.__init__-216"><a href="#Log.__init__-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log.__init__-217"><a href="#Log.__init__-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log.__init__-218"><a href="#Log.__init__-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Log.__init__-219"><a href="#Log.__init__-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">,</span> <span class="n">LoggingHandler</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Log.__init__-220"><a href="#Log.__init__-220"><span class="linenos">220</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">logger</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span>
</span><span id="Log.__init__-221"><a href="#Log.__init__-221"><span class="linenos">221</span></a>        <span class="c1"># self.serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="Log.__init__-222"><a href="#Log.__init__-222"><span class="linenos">222</span></a>        <span class="c1">#                                    Tags.can_use_bytes,</span>
</span><span id="Log.__init__-223"><a href="#Log.__init__-223"><span class="linenos">223</span></a>        <span class="c1">#                                    Tags.decode_str_as_str,</span>
</span><span id="Log.__init__-224"><a href="#Log.__init__-224"><span class="linenos">224</span></a>        <span class="c1">#                                    Tags.decode_list_as_list,</span>
</span><span id="Log.__init__-225"><a href="#Log.__init__-225"><span class="linenos">225</span></a>        <span class="c1">#                                    Tags.decode_bytes_as_bytes,</span>
</span><span id="Log.__init__-226"><a href="#Log.__init__-226"><span class="linenos">226</span></a>        <span class="c1">#                                    Tags.superficial,</span>
</span><span id="Log.__init__-227"><a href="#Log.__init__-227"><span class="linenos">227</span></a>        <span class="c1">#                                    Tags.current_platform,</span>
</span><span id="Log.__init__-228"><a href="#Log.__init__-228"><span class="linenos">228</span></a>        <span class="c1">#                                    Tags.multi_platform),</span>
</span><span id="Log.__init__-229"><a href="#Log.__init__-229"><span class="linenos">229</span></a>        <span class="c1">#                                   TestDataType.small,</span>
</span><span id="Log.__init__-230"><a href="#Log.__init__-230"><span class="linenos">230</span></a>        <span class="c1">#                                   0.1)</span>
</span><span id="Log.__init__-231"><a href="#Log.__init__-231"><span class="linenos">231</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="Log.__init__-232"><a href="#Log.__init__-232"><span class="linenos">232</span></a>
</span><span id="Log.__init__-233"><a href="#Log.__init__-233"><span class="linenos">233</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Log.__init__-234"><a href="#Log.__init__-234"><span class="linenos">234</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_db_environment_path</span><span class="p">,</span>
</span><span id="Log.__init__-235"><a href="#Log.__init__-235"><span class="linenos">235</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_sync</span><span class="p">,</span>
</span><span id="Log.__init__-236"><a href="#Log.__init__-236"><span class="linenos">236</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_add_iteration_handler</span><span class="p">,</span>
</span><span id="Log.__init__-237"><a href="#Log.__init__-237"><span class="linenos">237</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_remove_iteration_handler</span><span class="p">,</span>
</span><span id="Log.__init__-238"><a href="#Log.__init__-238"><span class="linenos">238</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_log_extended</span><span class="p">,</span>
</span><span id="Log.__init__-239"><a href="#Log.__init__-239"><span class="linenos">239</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_connect_to_logger</span><span class="p">,</span>
</span><span id="Log.__init__-240"><a href="#Log.__init__-240"><span class="linenos">240</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_disconnect_from_logger</span><span class="p">,</span>
</span><span id="Log.__init__-241"><a href="#Log.__init__-241"><span class="linenos">241</span></a>        <span class="p">}</span>
</span><span id="Log.__init__-242"><a href="#Log.__init__-242"><span class="linenos">242</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">inject_handler_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.default_logs_dir" class="classattr">
                                <div class="attr variable">
            <span class="name">default_logs_dir</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#Log.default_logs_dir"></a>
    
    

                            </div>
                            <div id="Log.path_to_db_environment" class="classattr">
                                <div class="attr variable">
            <span class="name">path_to_db_environment</span>

        
    </div>
    <a class="headerlink" href="#Log.path_to_db_environment"></a>
    
    

                            </div>
                            <div id="Log.app_name_waiter" class="classattr">
                                <div class="attr variable">
            <span class="name">app_name_waiter</span><span class="annotation">: cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.CoroWrapperBase</span>

        
    </div>
    <a class="headerlink" href="#Log.app_name_waiter"></a>
    
    

                            </div>
                            <div id="Log.root_path_to_log_environment_rel" class="classattr">
                                <div class="attr variable">
            <span class="name">root_path_to_log_environment_rel</span><span class="annotation">: cengal.file_system.path_manager.versions.v_0.path_manager.RelativePath</span>

        
    </div>
    <a class="headerlink" href="#Log.root_path_to_log_environment_rel"></a>
    
    

                            </div>
                            <div id="Log.db_environment" class="classattr">
                                <div class="attr variable">
            <span class="name">db_environment</span><span class="annotation">: Environment</span>

        
    </div>
    <a class="headerlink" href="#Log.db_environment"></a>
    
    

                            </div>
                            <div id="Log.db" class="classattr">
                                <div class="attr variable">
            <span class="name">db</span>

        
    </div>
    <a class="headerlink" href="#Log.db"></a>
    
    

                            </div>
                            <div id="Log.log_queue" class="classattr">
                                <div class="attr variable">
            <span class="name">log_queue</span><span class="annotation">: List[Tuple[Tuple, Dict, Dict[str, Any]]]</span>

        
    </div>
    <a class="headerlink" href="#Log.log_queue"></a>
    
    

                            </div>
                            <div id="Log.async_loop" class="classattr">
                                <div class="attr variable">
            <span class="name">async_loop</span>

        
    </div>
    <a class="headerlink" href="#Log.async_loop"></a>
    
    

                            </div>
                            <div id="Log.log_counter" class="classattr">
                                <div class="attr variable">
            <span class="name">log_counter</span>

        
    </div>
    <a class="headerlink" href="#Log.log_counter"></a>
    
    

                            </div>
                            <div id="Log.sync_time_interval" class="classattr">
                                <div class="attr variable">
            <span class="name">sync_time_interval</span>

        
    </div>
    <a class="headerlink" href="#Log.sync_time_interval"></a>
    
    

                            </div>
                            <div id="Log.characters_in_counter" class="classattr">
                                <div class="attr variable">
            <span class="name">characters_in_counter</span>

        
    </div>
    <a class="headerlink" href="#Log.characters_in_counter"></a>
    
    

                            </div>
                            <div id="Log.current_counter_state_key" class="classattr">
                                <div class="attr variable">
            <span class="name">current_counter_state_key</span>

        
    </div>
    <a class="headerlink" href="#Log.current_counter_state_key"></a>
    
    

                            </div>
                            <div id="Log.last_sync_time" class="classattr">
                                <div class="attr variable">
            <span class="name">last_sync_time</span>

        
    </div>
    <a class="headerlink" href="#Log.last_sync_time"></a>
    
    

                            </div>
                            <div id="Log.force_sync" class="classattr">
                                <div class="attr variable">
            <span class="name">force_sync</span>

        
    </div>
    <a class="headerlink" href="#Log.force_sync"></a>
    
    

                            </div>
                            <div id="Log.write_locked" class="classattr">
                                <div class="attr variable">
            <span class="name">write_locked</span>

        
    </div>
    <a class="headerlink" href="#Log.write_locked"></a>
    
    

                            </div>
                            <div id="Log.write_locked_coro_id" class="classattr">
                                <div class="attr variable">
            <span class="name">write_locked_coro_id</span><span class="annotation">: Union[int, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#Log.write_locked_coro_id"></a>
    
    

                            </div>
                            <div id="Log.periodic_sync_started" class="classattr">
                                <div class="attr variable">
            <span class="name">periodic_sync_started</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#Log.periodic_sync_started"></a>
    
    

                            </div>
                            <div id="Log.iteration_handlers" class="classattr">
                                <div class="attr variable">
            <span class="name">iteration_handlers</span><span class="annotation">: list[collections.abc.Callable[<a href="#Log">Log</a>, typing.List[typing.Tuple[typing.Tuple, typing.Dict]], float, str, NoneType]]</span>

        
    </div>
    <a class="headerlink" href="#Log.iteration_handlers"></a>
    
    

                            </div>
                            <div id="Log.new_iteration_handlers_num" class="classattr">
                                <div class="attr variable">
            <span class="name">new_iteration_handlers_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#Log.new_iteration_handlers_num"></a>
    
    

                            </div>
                            <div id="Log.logger_handlers" class="classattr">
                                <div class="attr variable">
            <span class="name">logger_handlers</span><span class="annotation">: Dict[logging.Logger, cengal.parallel_execution.coroutines.coro_standard_services.log.versions.v_0.log.LoggingHandler]</span>

        
    </div>
    <a class="headerlink" href="#Log.logger_handlers"></a>
    
    

                            </div>
                            <div id="Log.logger" class="classattr">
                                <div class="attr variable">
            <span class="name">logger</span><span class="annotation">: logging.Logger</span>

        
    </div>
    <a class="headerlink" href="#Log.logger"></a>
    
    

                            </div>
                            <div id="Log.serializer" class="classattr">
                                <div class="attr variable">
            <span class="name">serializer</span>

        
    </div>
    <a class="headerlink" href="#Log.serializer"></a>
    
    

                            </div>
                            <div id="Log.put_log" class="classattr">
                                        <input id="Log.put_log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_log</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">args</span>, </span><span class="param"><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Log.put_log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.put_log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.put_log-250"><a href="#Log.put_log-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="Log.put_log-251"><a href="#Log.put_log-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="Log.put_log-252"><a href="#Log.put_log-252"><span class="linenos">252</span></a>        <span class="c1"># self.make_live</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.put_log_ex" class="classattr">
                                        <input id="Log.put_log_ex-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_log_ex</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">args</span>, </span><span class="param"><span class="n">kwargs</span>, </span><span class="param"><span class="n">info</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Log.put_log_ex-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.put_log_ex"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.put_log_ex-254"><a href="#Log.put_log_ex-254"><span class="linenos">254</span></a>    <span class="k">def</span> <span class="nf">put_log_ex</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">):</span>
</span><span id="Log.put_log_ex-255"><a href="#Log.put_log_ex-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.destroy" class="classattr">
                                        <input id="Log.destroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Log.destroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.destroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.destroy-257"><a href="#Log.destroy-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log.destroy-258"><a href="#Log.destroy-258"><span class="linenos">258</span></a>        <span class="c1"># TODO: we need to use some loop destroy service in order to put our coro which will write all pending queues,</span>
</span><span id="Log.destroy-259"><a href="#Log.destroy-259"><span class="linenos">259</span></a>        <span class="c1"># sync envirounments and close them. Also we need to prevent new requests from being processed. (see DB service)</span>
</span><span id="Log.destroy-260"><a href="#Log.destroy-260"><span class="linenos">260</span></a>        <span class="n">loggers_instancess</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="Log.destroy-261"><a href="#Log.destroy-261"><span class="linenos">261</span></a>        <span class="k">for</span> <span class="n">logger_instance</span> <span class="ow">in</span> <span class="n">loggers_instancess</span><span class="p">:</span>
</span><span id="Log.destroy-262"><a href="#Log.destroy-262"><span class="linenos">262</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">eject_handler_from_logger</span><span class="p">(</span><span class="n">logger_instance</span><span class="p">)</span>
</span><span id="Log.destroy-263"><a href="#Log.destroy-263"><span class="linenos">263</span></a>
</span><span id="Log.destroy-264"><a href="#Log.destroy-264"><span class="linenos">264</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log.destroy-265"><a href="#Log.destroy-265"><span class="linenos">265</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="Log.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="Log.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.single_task_registration_or_immediate_processing-267"><a href="#Log.single_task_registration_or_immediate_processing-267"><span class="linenos">267</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Log.single_task_registration_or_immediate_processing-268"><a href="#Log.single_task_registration_or_immediate_processing-268"><span class="linenos">268</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="Log.single_task_registration_or_immediate_processing-269"><a href="#Log.single_task_registration_or_immediate_processing-269"><span class="linenos">269</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_resolve_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Log.single_task_registration_or_immediate_processing-270"><a href="#Log.single_task_registration_or_immediate_processing-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log.single_task_registration_or_immediate_processing-271"><a href="#Log.single_task_registration_or_immediate_processing-271"><span class="linenos">271</span></a>            <span class="n">coro_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span>
</span><span id="Log.single_task_registration_or_immediate_processing-272"><a href="#Log.single_task_registration_or_immediate_processing-272"><span class="linenos">272</span></a>            <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">worker</span>
</span><span id="Log.single_task_registration_or_immediate_processing-273"><a href="#Log.single_task_registration_or_immediate_processing-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="n">GreenletWorkerWrapper</span><span class="p">):</span>
</span><span id="Log.single_task_registration_or_immediate_processing-274"><a href="#Log.single_task_registration_or_immediate_processing-274"><span class="linenos">274</span></a>                <span class="n">coro_worker</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="o">.</span><span class="n">worker</span>
</span><span id="Log.single_task_registration_or_immediate_processing-275"><a href="#Log.single_task_registration_or_immediate_processing-275"><span class="linenos">275</span></a>            
</span><span id="Log.single_task_registration_or_immediate_processing-276"><a href="#Log.single_task_registration_or_immediate_processing-276"><span class="linenos">276</span></a>            <span class="n">caller_info</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;CoroID: </span><span class="si">{</span><span class="n">coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="si">:</span><span class="s1">10</span><span class="si">}</span><span class="s1">; Type: </span><span class="si">{</span><span class="s2">&quot;Awaitable&quot;</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="nb">issubclass</span><span class="p">(</span><span class="n">coro_info</span><span class="o">.</span><span class="n">coro_type</span><span class="p">,</span><span class="w"> </span><span class="n">CoroWrapperAsyncAwait</span><span class="p">)</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s2">&quot;Greenlet&quot;</span><span class="si">}</span><span class="s1">; Worker: </span><span class="si">{</span><span class="n">entity_repr_owner_based</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="Log.single_task_registration_or_immediate_processing-277"><a href="#Log.single_task_registration_or_immediate_processing-277"><span class="linenos">277</span></a>            <span class="n">coro_worker_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="Log.single_task_registration_or_immediate_processing-278"><a href="#Log.single_task_registration_or_immediate_processing-278"><span class="linenos">278</span></a>            <span class="n">info</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Log.single_task_registration_or_immediate_processing-279"><a href="#Log.single_task_registration_or_immediate_processing-279"><span class="linenos">279</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">current_time</span><span class="p">:</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(),</span>
</span><span id="Log.single_task_registration_or_immediate_processing-280"><a href="#Log.single_task_registration_or_immediate_processing-280"><span class="linenos">280</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">perf_counter_time</span><span class="p">:</span> <span class="n">perf_counter</span><span class="p">(),</span>
</span><span id="Log.single_task_registration_or_immediate_processing-281"><a href="#Log.single_task_registration_or_immediate_processing-281"><span class="linenos">281</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">file_name</span><span class="p">:</span> <span class="n">coro_worker_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="Log.single_task_registration_or_immediate_processing-282"><a href="#Log.single_task_registration_or_immediate_processing-282"><span class="linenos">282</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">line_number</span><span class="p">:</span> <span class="n">coro_worker_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="Log.single_task_registration_or_immediate_processing-283"><a href="#Log.single_task_registration_or_immediate_processing-283"><span class="linenos">283</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">caller_info</span><span class="p">:</span> <span class="n">caller_info</span><span class="p">,</span>
</span><span id="Log.single_task_registration_or_immediate_processing-284"><a href="#Log.single_task_registration_or_immediate_processing-284"><span class="linenos">284</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">traceback_strings</span><span class="p">:</span> <span class="nb">list</span><span class="p">(),</span>
</span><span id="Log.single_task_registration_or_immediate_processing-285"><a href="#Log.single_task_registration_or_immediate_processing-285"><span class="linenos">285</span></a>                <span class="c1"># InfoFields.coro_parents_strings: get_coro_parents_strings(coro_info.coro_id),</span>
</span><span id="Log.single_task_registration_or_immediate_processing-286"><a href="#Log.single_task_registration_or_immediate_processing-286"><span class="linenos">286</span></a>                <span class="n">InfoFields</span><span class="o">.</span><span class="n">coro_parents_strings</span><span class="p">:</span> <span class="nb">list</span><span class="p">(),</span>
</span><span id="Log.single_task_registration_or_immediate_processing-287"><a href="#Log.single_task_registration_or_immediate_processing-287"><span class="linenos">287</span></a>            <span class="p">}</span>
</span><span id="Log.single_task_registration_or_immediate_processing-288"><a href="#Log.single_task_registration_or_immediate_processing-288"><span class="linenos">288</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span><span class="p">))</span>
</span><span id="Log.single_task_registration_or_immediate_processing-289"><a href="#Log.single_task_registration_or_immediate_processing-289"><span class="linenos">289</span></a>            <span class="c1"># self.make_live()</span>
</span><span id="Log.single_task_registration_or_immediate_processing-290"><a href="#Log.single_task_registration_or_immediate_processing-290"><span class="linenos">290</span></a>
</span><span id="Log.single_task_registration_or_immediate_processing-291"><a href="#Log.single_task_registration_or_immediate_processing-291"><span class="linenos">291</span></a>            <span class="c1"># TODO: we need to implement backpressure mechanism here. If we have too many pending requests, we need to put request to queue instead of responding immediately.</span>
</span><span id="Log.single_task_registration_or_immediate_processing-292"><a href="#Log.single_task_registration_or_immediate_processing-292"><span class="linenos">292</span></a>            <span class="c1"># However this will not be enough for a direct requests. We need to implement some kind of backpressure mechanism for direct requests too.</span>
</span><span id="Log.single_task_registration_or_immediate_processing-293"><a href="#Log.single_task_registration_or_immediate_processing-293"><span class="linenos">293</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Log.single_task_registration_or_immediate_processing-294"><a href="#Log.single_task_registration_or_immediate_processing-294"><span class="linenos">294</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log.single_task_registration_or_immediate_processing-295"><a href="#Log.single_task_registration_or_immediate_processing-295"><span class="linenos">295</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.full_processing_iteration" class="classattr">
                                        <input id="Log.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Log.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.full_processing_iteration-321"><a href="#Log.full_processing_iteration-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log.full_processing_iteration-322"><a href="#Log.full_processing_iteration-322"><span class="linenos">322</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ensure_default_db_environment</span><span class="p">():</span>
</span><span id="Log.full_processing_iteration-323"><a href="#Log.full_processing_iteration-323"><span class="linenos">323</span></a>            <span class="k">return</span>
</span><span id="Log.full_processing_iteration-324"><a href="#Log.full_processing_iteration-324"><span class="linenos">324</span></a>        
</span><span id="Log.full_processing_iteration-325"><a href="#Log.full_processing_iteration-325"><span class="linenos">325</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log.full_processing_iteration-326"><a href="#Log.full_processing_iteration-326"><span class="linenos">326</span></a>        <span class="n">log_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span>
</span><span id="Log.full_processing_iteration-327"><a href="#Log.full_processing_iteration-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">log_queue_buff</span><span class="p">)()</span>
</span><span id="Log.full_processing_iteration-328"><a href="#Log.full_processing_iteration-328"><span class="linenos">328</span></a>        <span class="n">current_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Log.full_processing_iteration-329"><a href="#Log.full_processing_iteration-329"><span class="linenos">329</span></a>        <span class="n">current_time_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">current_time</span><span class="p">)</span>
</span><span id="Log.full_processing_iteration-330"><a href="#Log.full_processing_iteration-330"><span class="linenos">330</span></a>        <span class="k">for</span> <span class="n">iteration_handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">iteration_handlers</span><span class="p">:</span>
</span><span id="Log.full_processing_iteration-331"><a href="#Log.full_processing_iteration-331"><span class="linenos">331</span></a>            <span class="n">iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">log_queue_buff</span><span class="p">,</span> <span class="n">current_time</span><span class="p">,</span> <span class="n">current_time_str</span><span class="p">)</span>
</span><span id="Log.full_processing_iteration-332"><a href="#Log.full_processing_iteration-332"><span class="linenos">332</span></a>        
</span><span id="Log.full_processing_iteration-333"><a href="#Log.full_processing_iteration-333"><span class="linenos">333</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Log.full_processing_iteration-334"><a href="#Log.full_processing_iteration-334"><span class="linenos">334</span></a>
</span><span id="Log.full_processing_iteration-335"><a href="#Log.full_processing_iteration-335"><span class="linenos">335</span></a>        <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="Log.full_processing_iteration-336"><a href="#Log.full_processing_iteration-336"><span class="linenos">336</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Log.full_processing_iteration-337"><a href="#Log.full_processing_iteration-337"><span class="linenos">337</span></a>                <span class="k">for</span> <span class="n">log_info</span> <span class="ow">in</span> <span class="n">log_queue_buff</span><span class="p">:</span>
</span><span id="Log.full_processing_iteration-338"><a href="#Log.full_processing_iteration-338"><span class="linenos">338</span></a>                    <span class="n">key</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">get</span><span class="p">())</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">characters_in_counter</span><span class="p">)</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="n">current_time_str</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span>
</span><span id="Log.full_processing_iteration-339"><a href="#Log.full_processing_iteration-339"><span class="linenos">339</span></a>                    <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">log_info</span><span class="p">)</span>
</span><span id="Log.full_processing_iteration-340"><a href="#Log.full_processing_iteration-340"><span class="linenos">340</span></a>                    <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">dupdata</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Log.full_processing_iteration-341"><a href="#Log.full_processing_iteration-341"><span class="linenos">341</span></a>                
</span><span id="Log.full_processing_iteration-342"><a href="#Log.full_processing_iteration-342"><span class="linenos">342</span></a>                <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">),</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span>
</span><span id="Log.full_processing_iteration-343"><a href="#Log.full_processing_iteration-343"><span class="linenos">343</span></a>        
</span><span id="Log.full_processing_iteration-344"><a href="#Log.full_processing_iteration-344"><span class="linenos">344</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="Log.full_processing_iteration-345"><a href="#Log.full_processing_iteration-345"><span class="linenos">345</span></a>        
</span><span id="Log.full_processing_iteration-346"><a href="#Log.full_processing_iteration-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="Log.full_processing_iteration-347"><a href="#Log.full_processing_iteration-347"><span class="linenos">347</span></a>        
</span><span id="Log.full_processing_iteration-348"><a href="#Log.full_processing_iteration-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Log.full_processing_iteration-349"><a href="#Log.full_processing_iteration-349"><span class="linenos">349</span></a>
</span><span id="Log.full_processing_iteration-350"><a href="#Log.full_processing_iteration-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.in_work" class="classattr">
                                        <input id="Log.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="Log.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.in_work-352"><a href="#Log.in_work-352"><span class="linenos">352</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Log.in_work-353"><a href="#Log.in_work-353"><span class="linenos">353</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">)</span> \
</span><span id="Log.in_work-354"><a href="#Log.in_work-354"><span class="linenos">354</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> \
</span><span id="Log.in_work-355"><a href="#Log.in_work-355"><span class="linenos">355</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span><span class="p">)</span> \
</span><span id="Log.in_work-356"><a href="#Log.in_work-356"><span class="linenos">356</span></a>            <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_iteration_handlers_num</span> \
</span><span id="Log.in_work-357"><a href="#Log.in_work-357"><span class="linenos">357</span></a>            <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="ow">or</span> <span class="p">((</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_queue</span><span class="p">)</span> <span class="ow">and</span> <span class="p">((</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">)))</span>
</span><span id="Log.in_work-358"><a href="#Log.in_work-358"><span class="linenos">358</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="Log.time_left_before_next_event" class="classattr">
                                        <input id="Log.time_left_before_next_event-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">time_left_before_next_event</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="Log.time_left_before_next_event-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.time_left_before_next_event"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.time_left_before_next_event-360"><a href="#Log.time_left_before_next_event-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="Log.time_left_before_next_event-361"><a href="#Log.time_left_before_next_event-361"><span class="linenos">361</span></a>        <span class="n">time_since_last_sync_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span>
</span><span id="Log.time_left_before_next_event-362"><a href="#Log.time_left_before_next_event-362"><span class="linenos">362</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">&gt;</span> <span class="n">time_since_last_sync_time</span><span class="p">:</span>
</span><span id="Log.time_left_before_next_event-363"><a href="#Log.time_left_before_next_event-363"><span class="linenos">363</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">-</span> <span class="n">time_since_last_sync_time</span>
</span><span id="Log.time_left_before_next_event-364"><a href="#Log.time_left_before_next_event-364"><span class="linenos">364</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log.time_left_before_next_event-365"><a href="#Log.time_left_before_next_event-365"><span class="linenos">365</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.sync_in_thread_pool" class="classattr">
                                        <input id="Log.sync_in_thread_pool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sync_in_thread_pool</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Log.sync_in_thread_pool-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.sync_in_thread_pool"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.sync_in_thread_pool-430"><a href="#Log.sync_in_thread_pool-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">sync_in_thread_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Log.sync_in_thread_pool-431"><a href="#Log.sync_in_thread_pool-431"><span class="linenos">431</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Log.sync_in_thread_pool-432"><a href="#Log.sync_in_thread_pool-432"><span class="linenos">432</span></a>            <span class="k">if</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span>
</span><span id="Log.sync_in_thread_pool-433"><a href="#Log.sync_in_thread_pool-433"><span class="linenos">433</span></a>                <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">,</span> <span class="kc">True</span><span class="p">))</span>
</span><span id="Log.sync_in_thread_pool-434"><a href="#Log.sync_in_thread_pool-434"><span class="linenos">434</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Log.sync_in_thread_pool-435"><a href="#Log.sync_in_thread_pool-435"><span class="linenos">435</span></a>                <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log.sync_in_thread_pool-436"><a href="#Log.sync_in_thread_pool-436"><span class="linenos">436</span></a>                    <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="Log.sync_in_thread_pool-437"><a href="#Log.sync_in_thread_pool-437"><span class="linenos">437</span></a>            
</span><span id="Log.sync_in_thread_pool-438"><a href="#Log.sync_in_thread_pool-438"><span class="linenos">438</span></a>            <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">):</span>
</span><span id="Log.sync_in_thread_pool-439"><a href="#Log.sync_in_thread_pool-439"><span class="linenos">439</span></a>                <span class="k">def</span> <span class="nf">sync_worker</span><span class="p">():</span>
</span><span id="Log.sync_in_thread_pool-440"><a href="#Log.sync_in_thread_pool-440"><span class="linenos">440</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Log.sync_in_thread_pool-441"><a href="#Log.sync_in_thread_pool-441"><span class="linenos">441</span></a>                
</span><span id="Log.sync_in_thread_pool-442"><a href="#Log.sync_in_thread_pool-442"><span class="linenos">442</span></a>                <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">sync_worker</span><span class="p">)</span>
</span><span id="Log.sync_in_thread_pool-443"><a href="#Log.sync_in_thread_pool-443"><span class="linenos">443</span></a>
</span><span id="Log.sync_in_thread_pool-444"><a href="#Log.sync_in_thread_pool-444"><span class="linenos">444</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">)))</span>
</span><span id="Log.sync_in_thread_pool-445"><a href="#Log.sync_in_thread_pool-445"><span class="linenos">445</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.sync_in_thread_pool-446"><a href="#Log.sync_in_thread_pool-446"><span class="linenos">446</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log.sync_in_thread_pool-447"><a href="#Log.sync_in_thread_pool-447"><span class="linenos">447</span></a>            <span class="k">def</span> <span class="nf">make_service_live_for_a_next_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">:</span> <span class="s1">&#39;Log&#39;</span><span class="p">):</span>
</span><span id="Log.sync_in_thread_pool-448"><a href="#Log.sync_in_thread_pool-448"><span class="linenos">448</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log.sync_in_thread_pool-449"><a href="#Log.sync_in_thread_pool-449"><span class="linenos">449</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Log.sync_in_thread_pool-450"><a href="#Log.sync_in_thread_pool-450"><span class="linenos">450</span></a>            
</span><span id="Log.sync_in_thread_pool-451"><a href="#Log.sync_in_thread_pool-451"><span class="linenos">451</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">,</span> <span class="n">make_service_live_for_a_next_sync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="Log.sync_in_thread_pool-452"><a href="#Log.sync_in_thread_pool-452"><span class="linenos">452</span></a>
</span><span id="Log.sync_in_thread_pool-453"><a href="#Log.sync_in_thread_pool-453"><span class="linenos">453</span></a>        <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Log.sync_in_thread_pool-454"><a href="#Log.sync_in_thread_pool-454"><span class="linenos">454</span></a>        <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Log.sync_in_thread_pool-455"><a href="#Log.sync_in_thread_pool-455"><span class="linenos">455</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="Log.sync_in_thread_pool-456"><a href="#Log.sync_in_thread_pool-456"><span class="linenos">456</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">()</span>
</span><span id="Log.sync_in_thread_pool-457"><a href="#Log.sync_in_thread_pool-457"><span class="linenos">457</span></a>        <span class="k">except</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">:</span>
</span><span id="Log.sync_in_thread_pool-458"><a href="#Log.sync_in_thread_pool-458"><span class="linenos">458</span></a>            <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Log.sync_in_thread_pool-459"><a href="#Log.sync_in_thread_pool-459"><span class="linenos">459</span></a>
</span><span id="Log.sync_in_thread_pool-460"><a href="#Log.sync_in_thread_pool-460"><span class="linenos">460</span></a>        <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">sync_db_coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">)</span>
</span><span id="Log.sync_in_thread_pool-461"><a href="#Log.sync_in_thread_pool-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Log.sync_in_thread_pool-462"><a href="#Log.sync_in_thread_pool-462"><span class="linenos">462</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="Log.sync_in_thread_pool-463"><a href="#Log.sync_in_thread_pool-463"><span class="linenos">463</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">periodic_sync_started</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.get_last_n_logs" class="classattr">
                                        <input id="Log.get_last_n_logs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_last_n_logs</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">number</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">NoneType</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span>:</span></span>

                <label class="view-source-button" for="Log.get_last_n_logs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.get_last_n_logs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.get_last_n_logs-465"><a href="#Log.get_last_n_logs-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">get_last_n_logs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">number</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]:</span>
</span><span id="Log.get_last_n_logs-466"><a href="#Log.get_last_n_logs-466"><span class="linenos">466</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log.get_last_n_logs-467"><a href="#Log.get_last_n_logs-467"><span class="linenos">467</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log.get_last_n_logs-468"><a href="#Log.get_last_n_logs-468"><span class="linenos">468</span></a>        
</span><span id="Log.get_last_n_logs-469"><a href="#Log.get_last_n_logs-469"><span class="linenos">469</span></a>        <span class="k">if</span> <span class="n">number</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Log.get_last_n_logs-470"><a href="#Log.get_last_n_logs-470"><span class="linenos">470</span></a>            <span class="n">number</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="Log.get_last_n_logs-471"><a href="#Log.get_last_n_logs-471"><span class="linenos">471</span></a>        <span class="k">elif</span> <span class="n">number</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="Log.get_last_n_logs-472"><a href="#Log.get_last_n_logs-472"><span class="linenos">472</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log.get_last_n_logs-473"><a href="#Log.get_last_n_logs-473"><span class="linenos">473</span></a>        
</span><span id="Log.get_last_n_logs-474"><a href="#Log.get_last_n_logs-474"><span class="linenos">474</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Log.get_last_n_logs-475"><a href="#Log.get_last_n_logs-475"><span class="linenos">475</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Log.get_last_n_logs-476"><a href="#Log.get_last_n_logs-476"><span class="linenos">476</span></a>            <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span><span class="o">.</span><span class="n">last</span><span class="p">()</span>
</span><span id="Log.get_last_n_logs-477"><a href="#Log.get_last_n_logs-477"><span class="linenos">477</span></a>            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span><span class="o">.</span><span class="n">iterprev</span><span class="p">():</span>
</span><span id="Log.get_last_n_logs-478"><a href="#Log.get_last_n_logs-478"><span class="linenos">478</span></a>                <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_counter_state_key</span><span class="p">:</span>
</span><span id="Log.get_last_n_logs-479"><a href="#Log.get_last_n_logs-479"><span class="linenos">479</span></a>                    <span class="k">continue</span>
</span><span id="Log.get_last_n_logs-480"><a href="#Log.get_last_n_logs-480"><span class="linenos">480</span></a>
</span><span id="Log.get_last_n_logs-481"><a href="#Log.get_last_n_logs-481"><span class="linenos">481</span></a>                <span class="k">if</span> <span class="n">number</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="Log.get_last_n_logs-482"><a href="#Log.get_last_n_logs-482"><span class="linenos">482</span></a>                    <span class="k">break</span>
</span><span id="Log.get_last_n_logs-483"><a href="#Log.get_last_n_logs-483"><span class="linenos">483</span></a>
</span><span id="Log.get_last_n_logs-484"><a href="#Log.get_last_n_logs-484"><span class="linenos">484</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>
</span><span id="Log.get_last_n_logs-485"><a href="#Log.get_last_n_logs-485"><span class="linenos">485</span></a>                <span class="n">number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="Log.get_last_n_logs-486"><a href="#Log.get_last_n_logs-486"><span class="linenos">486</span></a>        
</span><span id="Log.get_last_n_logs-487"><a href="#Log.get_last_n_logs-487"><span class="linenos">487</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">reverse</span><span class="p">()</span>
</span><span id="Log.get_last_n_logs-488"><a href="#Log.get_last_n_logs-488"><span class="linenos">488</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.inject_handler_to_logger" class="classattr">
                                        <input id="Log.inject_handler_to_logger-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">inject_handler_to_logger</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="Log.inject_handler_to_logger-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.inject_handler_to_logger"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.inject_handler_to_logger-490"><a href="#Log.inject_handler_to_logger-490"><span class="linenos">490</span></a>    <span class="k">def</span> <span class="nf">inject_handler_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Log.inject_handler_to_logger-491"><a href="#Log.inject_handler_to_logger-491"><span class="linenos">491</span></a>        <span class="k">if</span> <span class="n">logger_instance</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span>
</span><span id="Log.inject_handler_to_logger-492"><a href="#Log.inject_handler_to_logger-492"><span class="linenos">492</span></a>            <span class="n">logger_handler</span><span class="p">:</span> <span class="n">LoggingHandler</span> <span class="o">=</span> <span class="n">LoggingHandler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="Log.inject_handler_to_logger-493"><a href="#Log.inject_handler_to_logger-493"><span class="linenos">493</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">]</span> <span class="o">=</span> <span class="n">logger_handler</span>
</span><span id="Log.inject_handler_to_logger-494"><a href="#Log.inject_handler_to_logger-494"><span class="linenos">494</span></a>            <span class="n">logger_instance</span><span class="o">.</span><span class="n">addHandler</span><span class="p">(</span><span class="n">logger_handler</span><span class="p">)</span>
</span><span id="Log.inject_handler_to_logger-495"><a href="#Log.inject_handler_to_logger-495"><span class="linenos">495</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="Log.inject_handler_to_logger-496"><a href="#Log.inject_handler_to_logger-496"><span class="linenos">496</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log.inject_handler_to_logger-497"><a href="#Log.inject_handler_to_logger-497"><span class="linenos">497</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="Log.eject_handler_from_logger" class="classattr">
                                        <input id="Log.eject_handler_from_logger-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">eject_handler_from_logger</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="Log.eject_handler_from_logger-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Log.eject_handler_from_logger"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Log.eject_handler_from_logger-503"><a href="#Log.eject_handler_from_logger-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="nf">eject_handler_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Log.eject_handler_from_logger-504"><a href="#Log.eject_handler_from_logger-504"><span class="linenos">504</span></a>        <span class="k">if</span> <span class="n">logger_instance</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">:</span>
</span><span id="Log.eject_handler_from_logger-505"><a href="#Log.eject_handler_from_logger-505"><span class="linenos">505</span></a>            <span class="n">logger_instance</span><span class="o">.</span><span class="n">removeHandler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">])</span>
</span><span id="Log.eject_handler_from_logger-506"><a href="#Log.eject_handler_from_logger-506"><span class="linenos">506</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">logger_handlers</span><span class="p">[</span><span class="n">logger_instance</span><span class="p">]</span>
</span><span id="Log.eject_handler_from_logger-507"><a href="#Log.eject_handler_from_logger-507"><span class="linenos">507</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="Log.eject_handler_from_logger-508"><a href="#Log.eject_handler_from_logger-508"><span class="linenos">508</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Log.eject_handler_from_logger-509"><a href="#Log.eject_handler_from_logger-509"><span class="linenos">509</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="Log.StatsLevel" class="class">StatsLevel</dd>
                <dd id="Log.get_entity_stats" class="function">get_entity_stats</dd>

            </div>
            <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="Log.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="Log.iteration" class="function">iteration</dd>
                <dd id="Log.make_response" class="function">make_response</dd>
                <dd id="Log.register_response" class="function">register_response</dd>
                <dd id="Log.put_task" class="function">put_task</dd>
                <dd id="Log.resolve_request" class="function">resolve_request</dd>
                <dd id="Log.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="Log.in_forground_work" class="function">in_forground_work</dd>
                <dd id="Log.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="Log.is_low_latency" class="function">is_low_latency</dd>
                <dd id="Log.make_live" class="function">make_live</dd>
                <dd id="Log.make_dead" class="function">make_dead</dd>
                <dd id="Log.service_id_impl" class="function">service_id_impl</dd>
                <dd id="Log.service_id" class="function">service_id</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LogRequest">
                            <input id="LogRequest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LogRequest</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</span>):

                <label class="view-source-button" for="LogRequest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest-174"><a href="#LogRequest-174"><span class="linenos">174</span></a><span class="k">class</span> <span class="nc">LogRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="LogRequest-175"><a href="#LogRequest-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest-176"><a href="#LogRequest-176"><span class="linenos">176</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span><span id="LogRequest-177"><a href="#LogRequest-177"><span class="linenos">177</span></a>    
</span><span id="LogRequest-178"><a href="#LogRequest-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest-179"><a href="#LogRequest-179"><span class="linenos">179</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="LogRequest-180"><a href="#LogRequest-180"><span class="linenos">180</span></a>
</span><span id="LogRequest-181"><a href="#LogRequest-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">add_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest-182"><a href="#LogRequest-182"><span class="linenos">182</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="LogRequest-183"><a href="#LogRequest-183"><span class="linenos">183</span></a>
</span><span id="LogRequest-184"><a href="#LogRequest-184"><span class="linenos">184</span></a>    <span class="k">def</span> <span class="nf">remove_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest-185"><a href="#LogRequest-185"><span class="linenos">185</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span><span id="LogRequest-186"><a href="#LogRequest-186"><span class="linenos">186</span></a>    
</span><span id="LogRequest-187"><a href="#LogRequest-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest-188"><a href="#LogRequest-188"><span class="linenos">188</span></a>        <span class="k">return</span> <span class="n">LogEx</span><span class="p">[</span><span class="kc">None</span><span class="p">](</span><span class="n">default_info_gatherer</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">2</span><span class="p">)(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogRequest-189"><a href="#LogRequest-189"><span class="linenos">189</span></a>
</span><span id="LogRequest-190"><a href="#LogRequest-190"><span class="linenos">190</span></a>    <span class="k">def</span> <span class="nf">connect_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest-191"><a href="#LogRequest-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">)</span>
</span><span id="LogRequest-192"><a href="#LogRequest-192"><span class="linenos">192</span></a>
</span><span id="LogRequest-193"><a href="#LogRequest-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">disconnect_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest-194"><a href="#LogRequest-194"><span class="linenos">194</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="LogRequest.set_db_environment_path" class="classattr">
                                        <input id="LogRequest.set_db_environment_path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_db_environment_path</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LogRequest.set_db_environment_path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest.set_db_environment_path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest.set_db_environment_path-175"><a href="#LogRequest.set_db_environment_path-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest.set_db_environment_path-176"><a href="#LogRequest.set_db_environment_path-176"><span class="linenos">176</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogRequest.sync" class="classattr">
                                        <input id="LogRequest.sync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sync</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LogRequest.sync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest.sync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest.sync-178"><a href="#LogRequest.sync-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest.sync-179"><a href="#LogRequest.sync-179"><span class="linenos">179</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogRequest.add_iteration_handler" class="classattr">
                                        <input id="LogRequest.add_iteration_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_iteration_handler</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n"><a href="#Log">Log</a></span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">List</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LogRequest.add_iteration_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest.add_iteration_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest.add_iteration_handler-181"><a href="#LogRequest.add_iteration_handler-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">add_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest.add_iteration_handler-182"><a href="#LogRequest.add_iteration_handler-182"><span class="linenos">182</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogRequest.remove_iteration_handler" class="classattr">
                                        <input id="LogRequest.remove_iteration_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_iteration_handler</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">handler</span><span class="p">:</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n"><a href="#Log">Log</a></span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">List</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LogRequest.remove_iteration_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest.remove_iteration_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest.remove_iteration_handler-184"><a href="#LogRequest.remove_iteration_handler-184"><span class="linenos">184</span></a>    <span class="k">def</span> <span class="nf">remove_iteration_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="s1">&#39;Log&#39;</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]],</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest.remove_iteration_handler-185"><a href="#LogRequest.remove_iteration_handler-185"><span class="linenos">185</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogRequest.log" class="classattr">
                                        <input id="LogRequest.log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">log</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LogRequest.log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest.log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest.log-187"><a href="#LogRequest.log-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest.log-188"><a href="#LogRequest.log-188"><span class="linenos">188</span></a>        <span class="k">return</span> <span class="n">LogEx</span><span class="p">[</span><span class="kc">None</span><span class="p">](</span><span class="n">default_info_gatherer</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">2</span><span class="p">)(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogRequest.connect_to_logger" class="classattr">
                                        <input id="LogRequest.connect_to_logger-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">connect_to_logger</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LogRequest.connect_to_logger-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest.connect_to_logger"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest.connect_to_logger-190"><a href="#LogRequest.connect_to_logger-190"><span class="linenos">190</span></a>    <span class="k">def</span> <span class="nf">connect_to_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest.connect_to_logger-191"><a href="#LogRequest.connect_to_logger-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogRequest.disconnect_from_logger" class="classattr">
                                        <input id="LogRequest.disconnect_from_logger-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">disconnect_from_logger</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LogRequest.disconnect_from_logger-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogRequest.disconnect_from_logger"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogRequest.disconnect_from_logger-193"><a href="#LogRequest.disconnect_from_logger-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">disconnect_from_logger</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">:</span> <span class="n">logging</span><span class="o">.</span><span class="n">Logger</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LogRequest.disconnect_from_logger-194"><a href="#LogRequest.disconnect_from_logger-194"><span class="linenos">194</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">logger_instance</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogRequest.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<span class="default_value">&lt;class &#39;<a href="#Log">Log</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#LogRequest.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="LogRequest.default__request__type__" class="variable">default__request__type__</dd>
                <dd id="LogRequest.request_type" class="variable">request_type</dd>
                <dd id="LogRequest.args" class="variable">args</dd>
                <dd id="LogRequest.kwargs" class="variable">kwargs</dd>
                <dd id="LogRequest.provide_to_request_handler" class="variable">provide_to_request_handler</dd>
                <dd id="LogRequest.interface" class="function">interface</dd>
                <dd id="LogRequest.i" class="function">i</dd>
                <dd id="LogRequest.async_interface" class="function">async_interface</dd>
                <dd id="LogRequest.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="view_log">
                            <input id="view_log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">view_log</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">path_to_db_environment</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">file_to_redirect_output</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="view_log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#view_log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="view_log-604"><a href="#view_log-604"><span class="linenos">604</span></a><span class="k">def</span> <span class="nf">view_log</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">file_to_redirect_output</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="view_log-605"><a href="#view_log-605"><span class="linenos">605</span></a>    <span class="k">if</span> <span class="n">path_to_db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="view_log-606"><a href="#view_log-606"><span class="linenos">606</span></a>        <span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_relative_to_current_dir</span><span class="p">(</span><span class="s1">&#39;log.db&#39;</span><span class="p">)</span>
</span><span id="view_log-607"><a href="#view_log-607"><span class="linenos">607</span></a>
</span><span id="view_log-608"><a href="#view_log-608"><span class="linenos">608</span></a>    <span class="n">output_file</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="view_log-609"><a href="#view_log-609"><span class="linenos">609</span></a>    <span class="k">if</span> <span class="n">file_to_redirect_output</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="view_log-610"><a href="#view_log-610"><span class="linenos">610</span></a>        <span class="n">output_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_to_redirect_output</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span>
</span><span id="view_log-611"><a href="#view_log-611"><span class="linenos">611</span></a>
</span><span id="view_log-612"><a href="#view_log-612"><span class="linenos">612</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="view_log-613"><a href="#view_log-613"><span class="linenos">613</span></a>        <span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span> <span class="o">**</span> <span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="view_log-614"><a href="#view_log-614"><span class="linenos">614</span></a>        <span class="n">db</span> <span class="o">=</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;logs&#39;</span><span class="p">)</span>
</span><span id="view_log-615"><a href="#view_log-615"><span class="linenos">615</span></a>        <span class="c1"># serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="view_log-616"><a href="#view_log-616"><span class="linenos">616</span></a>        <span class="c1">#                               Tags.can_use_bytes,</span>
</span><span id="view_log-617"><a href="#view_log-617"><span class="linenos">617</span></a>        <span class="c1">#                               Tags.decode_str_as_str,</span>
</span><span id="view_log-618"><a href="#view_log-618"><span class="linenos">618</span></a>        <span class="c1">#                               Tags.decode_list_as_list,</span>
</span><span id="view_log-619"><a href="#view_log-619"><span class="linenos">619</span></a>        <span class="c1">#                               Tags.decode_bytes_as_bytes, </span>
</span><span id="view_log-620"><a href="#view_log-620"><span class="linenos">620</span></a>        <span class="c1">#                               Tags.superficial,</span>
</span><span id="view_log-621"><a href="#view_log-621"><span class="linenos">621</span></a>        <span class="c1">#                               Tags.current_platform,</span>
</span><span id="view_log-622"><a href="#view_log-622"><span class="linenos">622</span></a>        <span class="c1">#                               Tags.multi_platform),</span>
</span><span id="view_log-623"><a href="#view_log-623"><span class="linenos">623</span></a>        <span class="c1">#                              TestDataType.small,</span>
</span><span id="view_log-624"><a href="#view_log-624"><span class="linenos">624</span></a>        <span class="c1">#                              0.1)</span>
</span><span id="view_log-625"><a href="#view_log-625"><span class="linenos">625</span></a>        <span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="view_log-626"><a href="#view_log-626"><span class="linenos">626</span></a>        <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">()</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="view_log-627"><a href="#view_log-627"><span class="linenos">627</span></a>            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">db</span><span class="p">):</span>
</span><span id="view_log-628"><a href="#view_log-628"><span class="linenos">628</span></a>                <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">str</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">16</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">():</span>
</span><span id="view_log-629"><a href="#view_log-629"><span class="linenos">629</span></a>                    <span class="k">if</span> <span class="n">output_file</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="view_log-630"><a href="#view_log-630"><span class="linenos">630</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λλλ &lt;&lt;&lt; </span><span class="si">{</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1"> &gt;&gt;&gt;&#39;</span><span class="p">)</span>
</span><span id="view_log-631"><a href="#view_log-631"><span class="linenos">631</span></a>                        <span class="nb">print</span><span class="p">()</span>
</span><span id="view_log-632"><a href="#view_log-632"><span class="linenos">632</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="view_log-633"><a href="#view_log-633"><span class="linenos">633</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λλλ &lt;&lt;&lt; </span><span class="si">{</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1"> &gt;&gt;&gt;&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="view_log-634"><a href="#view_log-634"><span class="linenos">634</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="view_log-635"><a href="#view_log-635"><span class="linenos">635</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="view_log-636"><a href="#view_log-636"><span class="linenos">636</span></a>                    <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">info</span> <span class="o">=</span> <span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="view_log-637"><a href="#view_log-637"><span class="linenos">637</span></a>                    <span class="k">if</span> <span class="n">output_file</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="view_log-638"><a href="#view_log-638"><span class="linenos">638</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ &gt;&gt;&gt;</span><span class="se">\t</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="s2">&quot;~&quot;</span><span class="o">*</span><span class="mi">8</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="view_log-639"><a href="#view_log-639"><span class="linenos">639</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="view_log-640"><a href="#view_log-640"><span class="linenos">640</span></a>                        <span class="nb">print</span><span class="p">(</span><span class="n">info</span><span class="p">)</span>
</span><span id="view_log-641"><a href="#view_log-641"><span class="linenos">641</span></a>                        <span class="nb">print</span><span class="p">()</span>
</span><span id="view_log-642"><a href="#view_log-642"><span class="linenos">642</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="view_log-643"><a href="#view_log-643"><span class="linenos">643</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ &gt;&gt;&gt;</span><span class="se">\t</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="s2">&quot;~&quot;</span><span class="o">*</span><span class="mi">8</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="view_log-644"><a href="#view_log-644"><span class="linenos">644</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">args_kwargs_to_str</span><span class="p">(</span><span class="n">args</span><span class="p">,</span><span class="w"> </span><span class="n">kwargs</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="view_log-645"><a href="#view_log-645"><span class="linenos">645</span></a>                        <span class="n">output_file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>
</span><span id="view_log-646"><a href="#view_log-646"><span class="linenos">646</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="view_log-647"><a href="#view_log-647"><span class="linenos">647</span></a>        <span class="k">if</span> <span class="n">output_file</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="view_log-648"><a href="#view_log-648"><span class="linenos">648</span></a>            <span class="n">output_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="clear_log">
                            <input id="clear_log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">clear_log</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">path_to_db_environment</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="clear_log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#clear_log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="clear_log-651"><a href="#clear_log-651"><span class="linenos">651</span></a><span class="k">def</span> <span class="nf">clear_log</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="clear_log-652"><a href="#clear_log-652"><span class="linenos">652</span></a>    <span class="k">if</span> <span class="n">path_to_db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="clear_log-653"><a href="#clear_log-653"><span class="linenos">653</span></a>        <span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_relative_to_current_dir</span><span class="p">(</span><span class="s1">&#39;log.db&#39;</span><span class="p">)</span>
</span><span id="clear_log-654"><a href="#clear_log-654"><span class="linenos">654</span></a>    <span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span> <span class="o">**</span> <span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="clear_log-655"><a href="#clear_log-655"><span class="linenos">655</span></a>    <span class="n">db</span> <span class="o">=</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;logs&#39;</span><span class="p">)</span>
</span><span id="clear_log-656"><a href="#clear_log-656"><span class="linenos">656</span></a>    <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="clear_log-657"><a href="#clear_log-657"><span class="linenos">657</span></a>        <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="clear_log-658"><a href="#clear_log-658"><span class="linenos">658</span></a>            <span class="n">txn</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">db</span><span class="p">,</span> <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="clear_log-659"><a href="#clear_log-659"><span class="linenos">659</span></a>    <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">db</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="LogClient">
                            <input id="LogClient-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LogClient</span>:

                <label class="view-source-button" for="LogClient-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient-520"><a href="#LogClient-520"><span class="linenos">520</span></a><span class="k">class</span> <span class="nc">LogClient</span><span class="p">:</span>
</span><span id="LogClient-521"><a href="#LogClient-521"><span class="linenos">521</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LogClient-522"><a href="#LogClient-522"><span class="linenos">522</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">info_gatherer</span>
</span><span id="LogClient-523"><a href="#LogClient-523"><span class="linenos">523</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">:</span> <span class="n">LogEx</span> <span class="o">=</span> <span class="n">LogEx</span><span class="p">(</span><span class="n">default_info_gatherer</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="LogClient-524"><a href="#LogClient-524"><span class="linenos">524</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="LogClient-525"><a href="#LogClient-525"><span class="linenos">525</span></a>
</span><span id="LogClient-526"><a href="#LogClient-526"><span class="linenos">526</span></a>    <span class="k">def</span> <span class="nf">log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient-527"><a href="#LogClient-527"><span class="linenos">527</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient-528"><a href="#LogClient-528"><span class="linenos">528</span></a>            <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient-529"><a href="#LogClient-529"><span class="linenos">529</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient-530"><a href="#LogClient-530"><span class="linenos">530</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-531"><a href="#LogClient-531"><span class="linenos">531</span></a>        
</span><span id="LogClient-532"><a href="#LogClient-532"><span class="linenos">532</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="LogClient-533"><a href="#LogClient-533"><span class="linenos">533</span></a>
</span><span id="LogClient-534"><a href="#LogClient-534"><span class="linenos">534</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient-535"><a href="#LogClient-535"><span class="linenos">535</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient-536"><a href="#LogClient-536"><span class="linenos">536</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient-537"><a href="#LogClient-537"><span class="linenos">537</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient-538"><a href="#LogClient-538"><span class="linenos">538</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-539"><a href="#LogClient-539"><span class="linenos">539</span></a>        
</span><span id="LogClient-540"><a href="#LogClient-540"><span class="linenos">540</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="LogClient-541"><a href="#LogClient-541"><span class="linenos">541</span></a>
</span><span id="LogClient-542"><a href="#LogClient-542"><span class="linenos">542</span></a>    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient-543"><a href="#LogClient-543"><span class="linenos">543</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient-544"><a href="#LogClient-544"><span class="linenos">544</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient-545"><a href="#LogClient-545"><span class="linenos">545</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient-546"><a href="#LogClient-546"><span class="linenos">546</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-547"><a href="#LogClient-547"><span class="linenos">547</span></a>        
</span><span id="LogClient-548"><a href="#LogClient-548"><span class="linenos">548</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="LogClient-549"><a href="#LogClient-549"><span class="linenos">549</span></a>
</span><span id="LogClient-550"><a href="#LogClient-550"><span class="linenos">550</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient-551"><a href="#LogClient-551"><span class="linenos">551</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient-552"><a href="#LogClient-552"><span class="linenos">552</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient-553"><a href="#LogClient-553"><span class="linenos">553</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient-554"><a href="#LogClient-554"><span class="linenos">554</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-555"><a href="#LogClient-555"><span class="linenos">555</span></a>        
</span><span id="LogClient-556"><a href="#LogClient-556"><span class="linenos">556</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="LogClient-557"><a href="#LogClient-557"><span class="linenos">557</span></a>
</span><span id="LogClient-558"><a href="#LogClient-558"><span class="linenos">558</span></a>    <span class="k">def</span> <span class="nf">put_log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient-559"><a href="#LogClient-559"><span class="linenos">559</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient-560"><a href="#LogClient-560"><span class="linenos">560</span></a>            <span class="n">log_ex_request</span><span class="p">:</span> <span class="n">LogExtended</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-561"><a href="#LogClient-561"><span class="linenos">561</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log_ex</span><span class="p">(</span><span class="o">*</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-562"><a href="#LogClient-562"><span class="linenos">562</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient-563"><a href="#LogClient-563"><span class="linenos">563</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-564"><a href="#LogClient-564"><span class="linenos">564</span></a>        
</span><span id="LogClient-565"><a href="#LogClient-565"><span class="linenos">565</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="LogClient-566"><a href="#LogClient-566"><span class="linenos">566</span></a>
</span><span id="LogClient-567"><a href="#LogClient-567"><span class="linenos">567</span></a>    <span class="n">plog_fast</span> <span class="o">=</span> <span class="n">put_log_fast</span>
</span><span id="LogClient-568"><a href="#LogClient-568"><span class="linenos">568</span></a>
</span><span id="LogClient-569"><a href="#LogClient-569"><span class="linenos">569</span></a>    <span class="c1"># async def aput_log_fast(self, scheduler: CoroSchedulerType, *args, **kwargs):</span>
</span><span id="LogClient-570"><a href="#LogClient-570"><span class="linenos">570</span></a>    <span class="c1">#     if self.extended:</span>
</span><span id="LogClient-571"><a href="#LogClient-571"><span class="linenos">571</span></a>    <span class="c1">#         log_ex_request: LogExtended = self.log_extended_request(*args, **kwargs)</span>
</span><span id="LogClient-572"><a href="#LogClient-572"><span class="linenos">572</span></a>    <span class="c1">#         scheduler.get_service_instance_fast(Log).put_log_ex(*log_ex_request.args, **log_ex_request.kwargs)</span>
</span><span id="LogClient-573"><a href="#LogClient-573"><span class="linenos">573</span></a>    <span class="c1">#     else:</span>
</span><span id="LogClient-574"><a href="#LogClient-574"><span class="linenos">574</span></a>    <span class="c1">#         scheduler.get_service_instance_fast(Log).put_log(args, kwargs)</span>
</span><span id="LogClient-575"><a href="#LogClient-575"><span class="linenos">575</span></a>
</span><span id="LogClient-576"><a href="#LogClient-576"><span class="linenos">576</span></a>    <span class="c1"># aplog_fast = aput_log_fast</span>
</span><span id="LogClient-577"><a href="#LogClient-577"><span class="linenos">577</span></a>
</span><span id="LogClient-578"><a href="#LogClient-578"><span class="linenos">578</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient-579"><a href="#LogClient-579"><span class="linenos">579</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">put_log_fast</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient-580"><a href="#LogClient-580"><span class="linenos">580</span></a>
</span><span id="LogClient-581"><a href="#LogClient-581"><span class="linenos">581</span></a>    <span class="n">plog</span> <span class="o">=</span> <span class="n">put_log</span>
</span><span id="LogClient-582"><a href="#LogClient-582"><span class="linenos">582</span></a>
</span><span id="LogClient-583"><a href="#LogClient-583"><span class="linenos">583</span></a>    <span class="c1"># async def aput_log(self, *args, **kwargs):</span>
</span><span id="LogClient-584"><a href="#LogClient-584"><span class="linenos">584</span></a>    <span class="c1">#     self.put_log_fast(current_coro_scheduler(), *args, **kwargs)</span>
</span><span id="LogClient-585"><a href="#LogClient-585"><span class="linenos">585</span></a>
</span><span id="LogClient-586"><a href="#LogClient-586"><span class="linenos">586</span></a>    <span class="c1"># aplog = aput_log</span>
</span></pre></div>


    

                            <div id="LogClient.__init__" class="classattr">
                                        <input id="LogClient.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LogClient</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="LogClient.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.__init__-521"><a href="#LogClient.__init__-521"><span class="linenos">521</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LogClient.__init__-522"><a href="#LogClient.__init__-522"><span class="linenos">522</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">info_gatherer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">info_gatherer</span>
</span><span id="LogClient.__init__-523"><a href="#LogClient.__init__-523"><span class="linenos">523</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">:</span> <span class="n">LogEx</span> <span class="o">=</span> <span class="n">LogEx</span><span class="p">(</span><span class="n">default_info_gatherer</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="LogClient.__init__-524"><a href="#LogClient.__init__-524"><span class="linenos">524</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.info_gatherer" class="classattr">
                                <div class="attr variable">
            <span class="name">info_gatherer</span><span class="annotation">: Union[Callable, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#LogClient.info_gatherer"></a>
    
    

                            </div>
                            <div id="LogClient.log_extended_request" class="classattr">
                                <div class="attr variable">
            <span class="name">log_extended_request</span><span class="annotation">: <a href="#LogExtended">LogExtended</a></span>

        
    </div>
    <a class="headerlink" href="#LogClient.log_extended_request"></a>
    
    

                            </div>
                            <div id="LogClient.extended" class="classattr">
                                <div class="attr variable">
            <span class="name">extended</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#LogClient.extended"></a>
    
    

                            </div>
                            <div id="LogClient.log_fast" class="classattr">
                                        <input id="LogClient.log_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">log_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.log_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.log_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.log_fast-526"><a href="#LogClient.log_fast-526"><span class="linenos">526</span></a>    <span class="k">def</span> <span class="nf">log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.log_fast-527"><a href="#LogClient.log_fast-527"><span class="linenos">527</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient.log_fast-528"><a href="#LogClient.log_fast-528"><span class="linenos">528</span></a>            <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient.log_fast-529"><a href="#LogClient.log_fast-529"><span class="linenos">529</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient.log_fast-530"><a href="#LogClient.log_fast-530"><span class="linenos">530</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.log_fast-531"><a href="#LogClient.log_fast-531"><span class="linenos">531</span></a>        
</span><span id="LogClient.log_fast-532"><a href="#LogClient.log_fast-532"><span class="linenos">532</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.alog_fast" class="classattr">
                                        <input id="LogClient.alog_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">alog_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.alog_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.alog_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.alog_fast-534"><a href="#LogClient.alog_fast-534"><span class="linenos">534</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.alog_fast-535"><a href="#LogClient.alog_fast-535"><span class="linenos">535</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient.alog_fast-536"><a href="#LogClient.alog_fast-536"><span class="linenos">536</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient.alog_fast-537"><a href="#LogClient.alog_fast-537"><span class="linenos">537</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient.alog_fast-538"><a href="#LogClient.alog_fast-538"><span class="linenos">538</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.alog_fast-539"><a href="#LogClient.alog_fast-539"><span class="linenos">539</span></a>        
</span><span id="LogClient.alog_fast-540"><a href="#LogClient.alog_fast-540"><span class="linenos">540</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.log" class="classattr">
                                        <input id="LogClient.log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">log</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.log-542"><a href="#LogClient.log-542"><span class="linenos">542</span></a>    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.log-543"><a href="#LogClient.log-543"><span class="linenos">543</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient.log-544"><a href="#LogClient.log-544"><span class="linenos">544</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient.log-545"><a href="#LogClient.log-545"><span class="linenos">545</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient.log-546"><a href="#LogClient.log-546"><span class="linenos">546</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.log-547"><a href="#LogClient.log-547"><span class="linenos">547</span></a>        
</span><span id="LogClient.log-548"><a href="#LogClient.log-548"><span class="linenos">548</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.alog" class="classattr">
                                        <input id="LogClient.alog-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">alog</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.alog-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.alog"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.alog-550"><a href="#LogClient.alog-550"><span class="linenos">550</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.alog-551"><a href="#LogClient.alog-551"><span class="linenos">551</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient.alog-552"><a href="#LogClient.alog-552"><span class="linenos">552</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="LogClient.alog-553"><a href="#LogClient.alog-553"><span class="linenos">553</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient.alog-554"><a href="#LogClient.alog-554"><span class="linenos">554</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.alog-555"><a href="#LogClient.alog-555"><span class="linenos">555</span></a>        
</span><span id="LogClient.alog-556"><a href="#LogClient.alog-556"><span class="linenos">556</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.put_log_fast" class="classattr">
                                        <input id="LogClient.put_log_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_log_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.put_log_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.put_log_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.put_log_fast-558"><a href="#LogClient.put_log_fast-558"><span class="linenos">558</span></a>    <span class="k">def</span> <span class="nf">put_log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.put_log_fast-559"><a href="#LogClient.put_log_fast-559"><span class="linenos">559</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient.put_log_fast-560"><a href="#LogClient.put_log_fast-560"><span class="linenos">560</span></a>            <span class="n">log_ex_request</span><span class="p">:</span> <span class="n">LogExtended</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.put_log_fast-561"><a href="#LogClient.put_log_fast-561"><span class="linenos">561</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log_ex</span><span class="p">(</span><span class="o">*</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.put_log_fast-562"><a href="#LogClient.put_log_fast-562"><span class="linenos">562</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient.put_log_fast-563"><a href="#LogClient.put_log_fast-563"><span class="linenos">563</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.put_log_fast-564"><a href="#LogClient.put_log_fast-564"><span class="linenos">564</span></a>        
</span><span id="LogClient.put_log_fast-565"><a href="#LogClient.put_log_fast-565"><span class="linenos">565</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.plog_fast" class="classattr">
                                        <input id="LogClient.plog_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">plog_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.plog_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.plog_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.plog_fast-558"><a href="#LogClient.plog_fast-558"><span class="linenos">558</span></a>    <span class="k">def</span> <span class="nf">put_log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.plog_fast-559"><a href="#LogClient.plog_fast-559"><span class="linenos">559</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="LogClient.plog_fast-560"><a href="#LogClient.plog_fast-560"><span class="linenos">560</span></a>            <span class="n">log_ex_request</span><span class="p">:</span> <span class="n">LogExtended</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.plog_fast-561"><a href="#LogClient.plog_fast-561"><span class="linenos">561</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log_ex</span><span class="p">(</span><span class="o">*</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.plog_fast-562"><a href="#LogClient.plog_fast-562"><span class="linenos">562</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LogClient.plog_fast-563"><a href="#LogClient.plog_fast-563"><span class="linenos">563</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="LogClient.plog_fast-564"><a href="#LogClient.plog_fast-564"><span class="linenos">564</span></a>        
</span><span id="LogClient.plog_fast-565"><a href="#LogClient.plog_fast-565"><span class="linenos">565</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.put_log" class="classattr">
                                        <input id="LogClient.put_log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_log</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.put_log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.put_log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.put_log-578"><a href="#LogClient.put_log-578"><span class="linenos">578</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.put_log-579"><a href="#LogClient.put_log-579"><span class="linenos">579</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">put_log_fast</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LogClient.plog" class="classattr">
                                        <input id="LogClient.plog-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">plog</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LogClient.plog-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LogClient.plog"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LogClient.plog-578"><a href="#LogClient.plog-578"><span class="linenos">578</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="LogClient.plog-579"><a href="#LogClient.plog-579"><span class="linenos">579</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">put_log_fast</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="default_log_client">
                    <div class="attr variable">
            <span class="name">default_log_client</span><span class="annotation">: <a href="#LogClient">LogClient</a></span>        =
<span class="default_value">&lt;<a href="#LogClient">LogClient</a> object&gt;</span>

        
    </div>
    <a class="headerlink" href="#default_log_client"></a>
    
    

                </section>
                <section id="log_fast">
                            <input id="log_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">log_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="log_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#log_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="log_fast-526"><a href="#log_fast-526"><span class="linenos">526</span></a>    <span class="k">def</span> <span class="nf">log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="log_fast-527"><a href="#log_fast-527"><span class="linenos">527</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="log_fast-528"><a href="#log_fast-528"><span class="linenos">528</span></a>            <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="log_fast-529"><a href="#log_fast-529"><span class="linenos">529</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="log_fast-530"><a href="#log_fast-530"><span class="linenos">530</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="log_fast-531"><a href="#log_fast-531"><span class="linenos">531</span></a>        
</span><span id="log_fast-532"><a href="#log_fast-532"><span class="linenos">532</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="alog_fast">
                            <input id="alog_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">alog_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="alog_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#alog_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="alog_fast-534"><a href="#alog_fast-534"><span class="linenos">534</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="alog_fast-535"><a href="#alog_fast-535"><span class="linenos">535</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="alog_fast-536"><a href="#alog_fast-536"><span class="linenos">536</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="alog_fast-537"><a href="#alog_fast-537"><span class="linenos">537</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="alog_fast-538"><a href="#alog_fast-538"><span class="linenos">538</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="alog_fast-539"><a href="#alog_fast-539"><span class="linenos">539</span></a>        
</span><span id="alog_fast-540"><a href="#alog_fast-540"><span class="linenos">540</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="log">
                            <input id="log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">log</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="log-542"><a href="#log-542"><span class="linenos">542</span></a>    <span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="log-543"><a href="#log-543"><span class="linenos">543</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="log-544"><a href="#log-544"><span class="linenos">544</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="log-545"><a href="#log-545"><span class="linenos">545</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="log-546"><a href="#log-546"><span class="linenos">546</span></a>            <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="log-547"><a href="#log-547"><span class="linenos">547</span></a>        
</span><span id="log-548"><a href="#log-548"><span class="linenos">548</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="alog">
                            <input id="alog-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">alog</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="alog-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#alog"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="alog-550"><a href="#alog-550"><span class="linenos">550</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">alog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="alog-551"><a href="#alog-551"><span class="linenos">551</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="alog-552"><a href="#alog-552"><span class="linenos">552</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="alog-553"><a href="#alog-553"><span class="linenos">553</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="alog-554"><a href="#alog-554"><span class="linenos">554</span></a>            <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">Log</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="alog-555"><a href="#alog-555"><span class="linenos">555</span></a>        
</span><span id="alog-556"><a href="#alog-556"><span class="linenos">556</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="put_log_fast">
                            <input id="put_log_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_log_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="put_log_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#put_log_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="put_log_fast-558"><a href="#put_log_fast-558"><span class="linenos">558</span></a>    <span class="k">def</span> <span class="nf">put_log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="put_log_fast-559"><a href="#put_log_fast-559"><span class="linenos">559</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="put_log_fast-560"><a href="#put_log_fast-560"><span class="linenos">560</span></a>            <span class="n">log_ex_request</span><span class="p">:</span> <span class="n">LogExtended</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="put_log_fast-561"><a href="#put_log_fast-561"><span class="linenos">561</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log_ex</span><span class="p">(</span><span class="o">*</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="put_log_fast-562"><a href="#put_log_fast-562"><span class="linenos">562</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="put_log_fast-563"><a href="#put_log_fast-563"><span class="linenos">563</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="put_log_fast-564"><a href="#put_log_fast-564"><span class="linenos">564</span></a>        
</span><span id="put_log_fast-565"><a href="#put_log_fast-565"><span class="linenos">565</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="plog_fast">
                            <input id="plog_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">plog_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="plog_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#plog_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="plog_fast-558"><a href="#plog_fast-558"><span class="linenos">558</span></a>    <span class="k">def</span> <span class="nf">put_log_fast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="plog_fast-559"><a href="#plog_fast-559"><span class="linenos">559</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">extended</span><span class="p">:</span>
</span><span id="plog_fast-560"><a href="#plog_fast-560"><span class="linenos">560</span></a>            <span class="n">log_ex_request</span><span class="p">:</span> <span class="n">LogExtended</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">log_extended_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="plog_fast-561"><a href="#plog_fast-561"><span class="linenos">561</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log_ex</span><span class="p">(</span><span class="o">*</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">log_ex_request</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="plog_fast-562"><a href="#plog_fast-562"><span class="linenos">562</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="plog_fast-563"><a href="#plog_fast-563"><span class="linenos">563</span></a>            <span class="n">scheduler</span><span class="o">.</span><span class="n">get_service_instance_fast</span><span class="p">(</span><span class="n">Log</span><span class="p">)</span><span class="o">.</span><span class="n">put_log</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="plog_fast-564"><a href="#plog_fast-564"><span class="linenos">564</span></a>        
</span><span id="plog_fast-565"><a href="#plog_fast-565"><span class="linenos">565</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">args</span> <span class="k">else</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="put_log">
                            <input id="put_log-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_log</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="put_log-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#put_log"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="put_log-578"><a href="#put_log-578"><span class="linenos">578</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="put_log-579"><a href="#put_log-579"><span class="linenos">579</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">put_log_fast</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="plog">
                            <input id="plog-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">plog</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="plog-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#plog"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="plog-578"><a href="#plog-578"><span class="linenos">578</span></a>    <span class="k">def</span> <span class="nf">put_log</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="plog-579"><a href="#plog-579"><span class="linenos">579</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">put_log_fast</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>