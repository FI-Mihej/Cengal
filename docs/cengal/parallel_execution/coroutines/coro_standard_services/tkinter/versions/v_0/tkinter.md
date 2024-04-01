---
title: tkinter
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.tkinter<wbr>.versions<wbr>.v_0<wbr>.tkinter    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-tkinter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-tkinter-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect.versions.v_0.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield.versions.v_0.loop_yield</span> <span class="kn">import</span> <span class="n">CoroPriority</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.simple_yield</span> <span class="kn">import</span> <span class="n">Yield</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.await_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Set</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.repeat_for_a_time</span> <span class="kn">import</span> <span class="n">Tracer</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions.v_1</span> <span class="kn">import</span> <span class="n">ValueExistence</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">from</span> <span class="nn">async_generator</span> <span class="kn">import</span> <span class="n">asynccontextmanager</span><span class="p">,</span> <span class="n">async_generator</span><span class="p">,</span> <span class="n">yield_</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="kn">from</span> <span class="nn">tkinter</span> <span class="kn">import</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">TclError</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="kn">import</span> <span class="nn">inspect</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="kn">from</span> <span class="nn">inspect</span> <span class="kn">import</span> <span class="n">isfunction</span><span class="p">,</span> <span class="n">ismethod</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="kn">from</span> <span class="nn">copy</span> <span class="kn">import</span> <span class="n">copy</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.sleep_tools</span> <span class="kn">import</span> <span class="n">get_usable_min_sleep_interval</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="n">TkObjId</span> <span class="o">=</span> <span class="nb">int</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="k">class</span> <span class="nc">TkinterServiceRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="nf">create</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TkObjId</span><span class="p">:</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TkObjId</span><span class="p">:</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">)</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tk</span><span class="p">:</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">)</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="nf">destroy_and_wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">)</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="nf">wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="k">def</span> <span class="nf">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CoroID</span><span class="p">:</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="k">def</span> <span class="nf">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    <span class="k">def</span> <span class="nf">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">period</span><span class="p">)</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="k">class</span> <span class="nc">TkObjDestroyedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="k">pass</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="k">class</span> <span class="nc">TkObjWrapper</span><span class="p">:</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="n">tk_obj_id</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="n">tk_obj</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">destroy_on_finish</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_service</span><span class="p">:</span> <span class="n">TkinterService</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">)</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="nd">@property</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">tk</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>            <span class="k">raise</span> <span class="n">TkObjDestroyedError</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="nd">@property</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">tk_id</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>            <span class="k">raise</span> <span class="n">TkObjDestroyedError</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">destroy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">))</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">adestroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">destroy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">))</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>    
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    <span class="k">def</span> <span class="nf">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">))</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aregister_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">))</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="nd">@property</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service</span><span class="o">.</span><span class="n">_get_inline</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>    
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">adestroy</span><span class="p">()</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">period</span><span class="p">))</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aset_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">period</span><span class="p">))</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a><span class="k">class</span> <span class="nc">TkinterContextManager</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">tk_obj_or_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tk</span><span class="p">,</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">interface</span> <span class="ow">or</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tk</span><span class="p">,</span> <span class="n">TkObjId</span><span class="p">]]</span> <span class="o">=</span> <span class="n">tk_obj_or_id</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">:</span> <span class="n">Tk</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="p">:</span> <span class="n">TkObjWrapper</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">Tk</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">))</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">):</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="nb">issubclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s1">&#39;Given class is not a subclass of Tk&#39;</span><span class="p">)</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span> <span class="o">=</span> <span class="n">TkObjWrapper</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span><span class="p">)</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">Tk</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">))</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">):</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="nb">issubclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s1">&#39;Given class is not a subclass of Tk&#39;</span><span class="p">)</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>            
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span> <span class="o">=</span> <span class="n">TkObjWrapper</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span><span class="p">)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a><span class="n">tcm</span> <span class="o">=</span> <span class="n">TkinterContextManager</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a><span class="k">class</span> <span class="nc">TkObjNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>    <span class="k">pass</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a><span class="k">class</span> <span class="nc">TkinterService</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_create</span><span class="p">,</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put</span><span class="p">,</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_destroy</span><span class="p">,</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_destroy_and_wait_for_destroyed</span><span class="p">,</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_destroyed</span><span class="p">,</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put_coro</span><span class="p">,</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_coro</span><span class="p">,</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_update_period</span><span class="p">,</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="p">}</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">standard_ui_update_interval</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="mi">60</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">get_usable_min_sleep_interval</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">standard_ui_update_interval</span><span class="p">)</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Tk</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_after_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>    
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>    <span class="k">def</span> <span class="nf">start_tk_updater</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span><span class="p">:</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="n">tk_updater_coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">tk_updater</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="n">tk_updater_coro</span><span class="o">.</span><span class="n">is_background_coro</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="s1">&#39;tk_counter&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="p">}</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TkinterServiceRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="c1"># closed</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="n">new_closed_bak</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">new_closed_bak</span><span class="p">)()</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span> <span class="ow">in</span> <span class="n">new_closed_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">just_mark_as_destroyed</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>        
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="c1"># waiting_for_destroyed</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="n">new_destroyed_bak</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">)()</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span> <span class="ow">in</span> <span class="n">new_destroyed_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>                <span class="k">continue</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>            
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>            <span class="n">tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>            
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>            <span class="c1"># if tk_obj_id in self.tk_after_ids:</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>            <span class="c1">#     after_ids = self.tk_after_ids[tk_obj_id]</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>            <span class="c1">#     for after_id in after_ids:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>            <span class="c1">#         tk_obj.after_cancel(after_id)</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>                
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>            <span class="c1">#     del self.tk_after_ids[tk_obj_id]</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>            <span class="c1"># cancel_all_after(tk_obj)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>            
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                <span class="n">tk_obj</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>            
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>                <span class="k">for</span> <span class="n">waiter_coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]:</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">waiter_coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>                
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>            
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">:</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>                <span class="n">coros_tks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]]</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>                <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="n">coros_tks</span><span class="p">:</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>                    <span class="n">coros_tks</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>                <span class="n">tk_users</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>                <span class="k">for</span> <span class="n">tk_user_coro_id</span> <span class="ow">in</span> <span class="n">tk_users</span><span class="p">:</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>                    <span class="c1"># TODO: switch to an appropriate service</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">kill_coro_by_id</span><span class="p">(</span><span class="n">tk_user_coro_id</span><span class="p">)</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>            
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>        
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>        <span class="c1"># compute min update period</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="c1"># general</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">):</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">)</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>    
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">_on_create</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="n">tk</span> <span class="o">=</span> <span class="n">tk_class</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>        <span class="n">tk_id</span><span class="p">:</span> <span class="n">TkObjId</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>        <span class="n">on_destroy</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_create_on_destroyed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">)</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Destroy&gt;&quot;</span><span class="p">,</span> <span class="n">on_destroy</span><span class="p">,</span> <span class="s1">&#39;+&#39;</span><span class="p">)</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>        <span class="n">old_on_close</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">isfunction</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ismethod</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">)):</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            <span class="n">old_on_close</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="n">on_create_on_closed</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_create_on_closed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">,</span> <span class="n">old_on_close</span><span class="p">)</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="n">on_create_on_closed</span><span class="p">)</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">tk</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="n">coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">:</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_created_coro_del_handler</span><span class="p">)</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">coro_id</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="c1"># after_setup(tk, 1)</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="n">after_idle_setup</span><span class="p">(</span><span class="n">tk</span><span class="p">)</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_tk_updater</span><span class="p">()</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>    
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="nf">_on_put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="n">tk</span><span class="p">:</span> <span class="n">Tk</span> <span class="o">=</span> <span class="n">tk_obj</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="n">tk_id</span><span class="p">:</span> <span class="n">TkObjId</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="n">on_destroy</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_put_on_destroyed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">)</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Destroy&gt;&quot;</span><span class="p">,</span> <span class="n">on_destroy</span><span class="p">,</span> <span class="s1">&#39;+&#39;</span><span class="p">)</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="n">old_on_close</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">isfunction</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ismethod</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">)):</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>            <span class="n">old_on_close</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>        <span class="n">on_put_on_closed</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_put_on_closed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">,</span> <span class="n">old_on_close</span><span class="p">)</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="n">on_put_on_closed</span><span class="p">)</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">tk</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>        <span class="n">coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">:</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>            <span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_put_coro_del_handler</span><span class="p">)</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>        
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">coro_id</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="c1"># after_setup(tk, 1)</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>        <span class="n">after_idle_setup</span><span class="p">(</span><span class="n">tk</span><span class="p">)</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_tk_updater</span><span class="p">()</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>    
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">],</span> <span class="kc">None</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">TkObjNotFoundError</span><span class="p">()</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>    
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>    <span class="k">def</span> <span class="nf">_get_inline</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tk</span><span class="p">]:</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>    
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>    <span class="k">def</span> <span class="nf">_on_destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">just_mark_as_destroyed</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>    
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>    <span class="k">def</span> <span class="nf">_on_destroy_and_wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">just_mark_as_destroyed</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_destroyed</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>    
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>    <span class="k">def</span> <span class="nf">_on_wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>        
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>    
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>    <span class="k">def</span> <span class="nf">_on_put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>            <span class="c1"># TODO: switch to an appropriate service</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>            <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_register_coro_impl</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>    
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>    <span class="k">def</span> <span class="nf">_on_register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_register_coro_impl</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>    
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>    <span class="k">def</span> <span class="nf">_register_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>        
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>    <span class="k">def</span> <span class="nf">_on_set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">period</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>        
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">_on_created_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>        
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>    <span class="k">def</span> <span class="nf">_on_put_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>        
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>    
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>    <span class="k">def</span> <span class="nf">_on_create_on_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>        <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">widget</span> <span class="ow">is</span> <span class="n">tk_obj</span><span class="p">:</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>        
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>    
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>    <span class="k">def</span> <span class="nf">_on_put_on_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">widget</span> <span class="ow">is</span> <span class="n">tk_obj</span><span class="p">:</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>        
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>    
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>    <span class="k">def</span> <span class="nf">_on_create_on_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">previous_on_close</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]):</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>        <span class="k">if</span> <span class="n">previous_on_close</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>            <span class="n">previous_on_close</span><span class="p">()</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>        
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>    
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>    <span class="k">def</span> <span class="nf">_on_put_on_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">previous_on_close</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]):</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>        <span class="k">if</span> <span class="n">previous_on_close</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>            <span class="n">previous_on_close</span><span class="p">()</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>        
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a><span class="c1"># def tk_updater(i: Interface, tkinter_service: TkinterService):</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a><span class="c1">#     from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a><span class="c1">#     while tkinter_service.tk_by_id:</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a><span class="c1">#         tk_by_id_bak = copy(tkinter_service.tk_by_id)</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a><span class="c1">#         for tk_id, tk_obj in tk_by_id_bak.items():</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a><span class="c1">#             if tk_id not in tkinter_service.destroyed:</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a><span class="c1">#                 tk_obj.update()</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>        
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a><span class="c1">#         i(Sleep, tkinter_service.update_period)</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>    
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a><span class="c1">#     tkinter_service.updater_running = False</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>    
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a><span class="c1"># def tk_updater(i: Interface, tkinter_service: TkinterService):</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a><span class="c1">#     &quot;&quot;&quot;</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a><span class="c1">#     https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a><span class="c1">#     https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a><span class="c1">#     Args:</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a><span class="c1">#         i (Interface): [description]</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a><span class="c1">#         tkinter_service (TkinterService): [description]</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a><span class="c1">#     &quot;&quot;&quot;</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a><span class="c1">#     from _tkinter import ALL_EVENTS as _tkinter__ALL_EVENTS, DONT_WAIT as _tkinter__DONT_WAIT</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a><span class="c1">#     from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a><span class="c1">#     from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import get_loop_yield</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a><span class="c1">#     ly = get_loop_yield(CoroPriority.low)</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a><span class="c1">#     while tkinter_service.tk_by_id:</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a><span class="c1">#         tk_by_id_bak = copy(tkinter_service.tk_by_id)</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a><span class="c1">#         for tk_id, tk_obj in tk_by_id_bak.items():</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a><span class="c1">#             ly()</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a><span class="c1">#             if tk_id not in tkinter_service.destroyed:</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a><span class="c1">#                 while tk_obj.dooneevent(_tkinter__ALL_EVENTS | _tkinter__DONT_WAIT):</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a><span class="c1">#                     ly()</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>        
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a><span class="c1">#         i(Sleep, tkinter_service.update_period)</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>    
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a><span class="c1">#     tkinter_service.updater_running = False</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>    
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a><span class="c1"># def tk_updater(i: Interface, tkinter_service: TkinterService):</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a><span class="c1">#     &quot;&quot;&quot;</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a><span class="c1">#     https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a><span class="c1">#     https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a><span class="c1">#     Args:</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a><span class="c1">#         i (Interface): [description]</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a><span class="c1">#         tkinter_service (TkinterService): [description]</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a><span class="c1">#     &quot;&quot;&quot;</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a><span class="c1">#     from _tkinter import ALL_EVENTS as _tkinter__ALL_EVENTS, DONT_WAIT as _tkinter__DONT_WAIT</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a><span class="c1">#     from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a><span class="c1">#     from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import get_loop_yield</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a><span class="c1">#     ly = get_loop_yield(CoroPriority.low)</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a><span class="c1">#     while tkinter_service.tk_by_id:</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a><span class="c1">#         ly()</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a><span class="c1">#         tk_by_id_bak = copy(tkinter_service.tk_by_id)</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a><span class="c1">#         tk_objects_with_events = set()</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a><span class="c1">#         for tk_id, tk_obj in tk_by_id_bak.items():</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a><span class="c1">#             if tk_id not in tkinter_service.destroyed:</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a><span class="c1">#                 tk_objects_with_events.add(tk_obj)</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>        
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a><span class="c1">#         while tk_objects_with_events:</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a><span class="c1">#             new_tk_objects_with_events = set()</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a><span class="c1">#             for tk_obj in tk_objects_with_events:</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a><span class="c1">#                 ly()</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a><span class="c1">#                 if tk_obj.dooneevent(_tkinter__ALL_EVENTS | _tkinter__DONT_WAIT):</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a><span class="c1">#                     new_tk_objects_with_events.add(tk_obj)</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>            
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a><span class="c1">#             tk_objects_with_events = new_tk_objects_with_events</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>        
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a><span class="c1">#         i(Sleep, tkinter_service.update_period)</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>    
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a><span class="c1">#     tkinter_service.updater_running = False</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a><span class="n">TkinterServiceRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">TkinterService</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a><span class="c1"># TODO: currently it uses Yield if delay is bigger that a magic number `0.001` seconds. Maybe make it some how use TkinterService.update_periods or somethin like it instead?</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a><span class="k">def</span> <span class="nf">tk_updater</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">tkinter_service</span><span class="p">:</span> <span class="n">TkinterService</span><span class="p">):</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a><span class="sd">    https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a><span class="sd">    https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a><span class="sd">    Args:</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a><span class="sd">        i (Interface): [description]</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a><span class="sd">        tkinter_service (TkinterService): [description]</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>    <span class="kn">from</span> <span class="nn">_tkinter</span> <span class="kn">import</span> <span class="n">ALL_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__ALL_EVENTS</span><span class="p">,</span> <span class="n">WINDOW_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__WINDOW_EVENTS</span><span class="p">,</span> <span class="n">FILE_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__FILE_EVENTS</span><span class="p">,</span> <span class="n">TIMER_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__TIMER_EVENTS</span><span class="p">,</span> <span class="n">IDLE_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__IDLE_EVENTS</span><span class="p">,</span> <span class="n">DONT_WAIT</span> <span class="k">as</span> <span class="n">_tkinter__DONT_WAIT</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.sleep</span> <span class="kn">import</span> <span class="n">Sleep</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">get_loop_yield</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">get_loop_yield</span><span class="p">(</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">)</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>    <span class="k">while</span> <span class="n">tkinter_service</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>        <span class="n">ly</span><span class="p">()</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>        <span class="n">tk_by_id_bak</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="n">tkinter_service</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">)</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>        <span class="n">desired_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tk_by_id_bak</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>        <span class="n">tk_ids_without_events</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>        
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>        <span class="k">while</span> <span class="nb">len</span><span class="p">(</span><span class="n">tk_ids_without_events</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">desired_length</span><span class="p">:</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>            <span class="k">for</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk_obj</span> <span class="ow">in</span> <span class="n">tk_by_id_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>                <span class="k">if</span> <span class="n">tk_id</span> <span class="ow">in</span> <span class="n">tk_ids_without_events</span><span class="p">:</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>                    <span class="k">continue</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>                
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>                <span class="k">if</span> <span class="n">tk_id</span> <span class="ow">in</span> <span class="n">tkinter_service</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>                    <span class="n">tk_ids_without_events</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>                    <span class="k">continue</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>                
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>                <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>                <span class="n">has_window_events</span> <span class="o">=</span> <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__WINDOW_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>                <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>                    <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>                <span class="c1"># ly()</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>                
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>                <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>                <span class="n">has_file_events</span> <span class="o">=</span> <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__FILE_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>                <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>                    <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>                <span class="c1"># ly()</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>                
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>                <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>                <span class="n">has_timer_events</span> <span class="o">=</span> <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__TIMER_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>                <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>                    <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>                <span class="c1"># ly()</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>                
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>                <span class="n">has_events</span> <span class="o">=</span> <span class="n">has_window_events</span> <span class="ow">or</span> <span class="n">has_file_events</span> <span class="ow">or</span> <span class="n">has_timer_events</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>                
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">has_events</span><span class="p">:</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>                    <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>                    <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__IDLE_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>                    <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>                    <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>                        <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>                    <span class="c1"># ly()</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>                    <span class="n">tk_ids_without_events</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="n">tkinter_service</span><span class="o">.</span><span class="n">update_period</span><span class="p">)</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>    
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>    <span class="n">tkinter_service</span><span class="o">.</span><span class="n">updater_running</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a><span class="k">def</span> <span class="nf">after_func</span><span class="p">(</span><span class="n">root</span><span class="p">):</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.simple_yield</span> <span class="kn">import</span> <span class="n">Yield</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="n">current_interface</span><span class="p">,</span> <span class="n">OutsideCoroSchedulerContext</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>        <span class="n">i</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>        <span class="k">if</span> <span class="n">i</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>    <span class="k">except</span> <span class="n">OutsideCoroSchedulerContext</span><span class="p">:</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>        <span class="k">pass</span>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a>    
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>    <span class="c1"># after_setup(root, 1)</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>    <span class="n">after_idle_setup</span><span class="p">(</span><span class="n">root</span><span class="p">)</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a><span class="k">def</span> <span class="nf">after_setup</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">update_period</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>        <span class="n">handler</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">after</span><span class="p">(</span><span class="n">update_period</span><span class="p">,</span> <span class="n">after_func</span><span class="p">,</span> <span class="n">root</span><span class="p">)</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>    <span class="k">except</span> <span class="n">TclError</span><span class="p">:</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>    <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a><span class="k">def</span> <span class="nf">after_idle_setup</span><span class="p">(</span><span class="n">root</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>        <span class="n">handler</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">after_idle</span><span class="p">(</span><span class="n">after_setup</span><span class="p">,</span> <span class="n">root</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>    <span class="k">except</span> <span class="n">TclError</span><span class="p">:</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>    <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


            </section>
                <section id="TkObjId">
                    <div class="attr variable">
            <span class="name">TkObjId</span>        =
<span class="default_value">&lt;class &#39;int&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#TkObjId"></a>
    
    

                </section>
                <section id="TkinterServiceRequest">
                            <input id="TkinterServiceRequest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TkinterServiceRequest</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</span>):

                <label class="view-source-button" for="TkinterServiceRequest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest-61"><a href="#TkinterServiceRequest-61"><span class="linenos">61</span></a><span class="k">class</span> <span class="nc">TkinterServiceRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="TkinterServiceRequest-62"><a href="#TkinterServiceRequest-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="nf">create</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TkObjId</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-63"><a href="#TkinterServiceRequest-63"><span class="linenos">63</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-64"><a href="#TkinterServiceRequest-64"><span class="linenos">64</span></a>
</span><span id="TkinterServiceRequest-65"><a href="#TkinterServiceRequest-65"><span class="linenos">65</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TkObjId</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-66"><a href="#TkinterServiceRequest-66"><span class="linenos">66</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-67"><a href="#TkinterServiceRequest-67"><span class="linenos">67</span></a>
</span><span id="TkinterServiceRequest-68"><a href="#TkinterServiceRequest-68"><span class="linenos">68</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tk</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-69"><a href="#TkinterServiceRequest-69"><span class="linenos">69</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-70"><a href="#TkinterServiceRequest-70"><span class="linenos">70</span></a>
</span><span id="TkinterServiceRequest-71"><a href="#TkinterServiceRequest-71"><span class="linenos">71</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-72"><a href="#TkinterServiceRequest-72"><span class="linenos">72</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-73"><a href="#TkinterServiceRequest-73"><span class="linenos">73</span></a>    
</span><span id="TkinterServiceRequest-74"><a href="#TkinterServiceRequest-74"><span class="linenos">74</span></a>    <span class="k">def</span> <span class="nf">destroy_and_wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-75"><a href="#TkinterServiceRequest-75"><span class="linenos">75</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-76"><a href="#TkinterServiceRequest-76"><span class="linenos">76</span></a>    
</span><span id="TkinterServiceRequest-77"><a href="#TkinterServiceRequest-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-78"><a href="#TkinterServiceRequest-78"><span class="linenos">78</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-79"><a href="#TkinterServiceRequest-79"><span class="linenos">79</span></a>    
</span><span id="TkinterServiceRequest-80"><a href="#TkinterServiceRequest-80"><span class="linenos">80</span></a>    <span class="k">def</span> <span class="nf">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CoroID</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-81"><a href="#TkinterServiceRequest-81"><span class="linenos">81</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-82"><a href="#TkinterServiceRequest-82"><span class="linenos">82</span></a>    
</span><span id="TkinterServiceRequest-83"><a href="#TkinterServiceRequest-83"><span class="linenos">83</span></a>    <span class="k">def</span> <span class="nf">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-84"><a href="#TkinterServiceRequest-84"><span class="linenos">84</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="TkinterServiceRequest-85"><a href="#TkinterServiceRequest-85"><span class="linenos">85</span></a>    
</span><span id="TkinterServiceRequest-86"><a href="#TkinterServiceRequest-86"><span class="linenos">86</span></a>    <span class="k">def</span> <span class="nf">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest-87"><a href="#TkinterServiceRequest-87"><span class="linenos">87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">period</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="TkinterServiceRequest.create" class="classattr">
                                        <input id="TkinterServiceRequest.create-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">tkinter</span><span class="o">.</span><span class="n">Tk</span><span class="p">]</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.create-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.create"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.create-62"><a href="#TkinterServiceRequest.create-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="nf">create</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TkObjId</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.create-63"><a href="#TkinterServiceRequest.create-63"><span class="linenos">63</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.put" class="classattr">
                                        <input id="TkinterServiceRequest.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_obj</span><span class="p">:</span> <span class="n">tkinter</span><span class="o">.</span><span class="n">Tk</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.put-65"><a href="#TkinterServiceRequest.put-65"><span class="linenos">65</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TkObjId</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.put-66"><a href="#TkinterServiceRequest.put-66"><span class="linenos">66</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.get" class="classattr">
                                        <input id="TkinterServiceRequest.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_obj_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n">tkinter</span><span class="o">.</span><span class="n">Tk</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.get-68"><a href="#TkinterServiceRequest.get-68"><span class="linenos">68</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tk</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.get-69"><a href="#TkinterServiceRequest.get-69"><span class="linenos">69</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.destroy" class="classattr">
                                        <input id="TkinterServiceRequest.destroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_obj_id</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.destroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.destroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.destroy-71"><a href="#TkinterServiceRequest.destroy-71"><span class="linenos">71</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.destroy-72"><a href="#TkinterServiceRequest.destroy-72"><span class="linenos">72</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.destroy_and_wait_for_destroyed" class="classattr">
                                        <input id="TkinterServiceRequest.destroy_and_wait_for_destroyed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy_and_wait_for_destroyed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_obj_id</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.destroy_and_wait_for_destroyed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.destroy_and_wait_for_destroyed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.destroy_and_wait_for_destroyed-74"><a href="#TkinterServiceRequest.destroy_and_wait_for_destroyed-74"><span class="linenos">74</span></a>    <span class="k">def</span> <span class="nf">destroy_and_wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.destroy_and_wait_for_destroyed-75"><a href="#TkinterServiceRequest.destroy_and_wait_for_destroyed-75"><span class="linenos">75</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.wait_for_destroyed" class="classattr">
                                        <input id="TkinterServiceRequest.wait_for_destroyed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wait_for_destroyed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_obj_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.wait_for_destroyed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.wait_for_destroyed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.wait_for_destroyed-77"><a href="#TkinterServiceRequest.wait_for_destroyed-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.wait_for_destroyed-78"><a href="#TkinterServiceRequest.wait_for_destroyed-78"><span class="linenos">78</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.put_coro" class="classattr">
                                        <input id="TkinterServiceRequest.put_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_coro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">tk_obj_id</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ExplicitWorker</span><span class="p">,</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.put_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.put_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.put_coro-80"><a href="#TkinterServiceRequest.put_coro-80"><span class="linenos">80</span></a>    <span class="k">def</span> <span class="nf">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CoroID</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.put_coro-81"><a href="#TkinterServiceRequest.put_coro-81"><span class="linenos">81</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.register_coro" class="classattr">
                                        <input id="TkinterServiceRequest.register_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_obj_id</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.register_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.register_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.register_coro-83"><a href="#TkinterServiceRequest.register_coro-83"><span class="linenos">83</span></a>    <span class="k">def</span> <span class="nf">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.register_coro-84"><a href="#TkinterServiceRequest.register_coro-84"><span class="linenos">84</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.set_update_period" class="classattr">
                                        <input id="TkinterServiceRequest.set_update_period-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_update_period</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tk_obj_id</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">period</span><span class="p">:</span> <span class="nb">float</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TkinterServiceRequest.set_update_period-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterServiceRequest.set_update_period"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterServiceRequest.set_update_period-86"><a href="#TkinterServiceRequest.set_update_period-86"><span class="linenos">86</span></a>    <span class="k">def</span> <span class="nf">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterServiceRequest.set_update_period-87"><a href="#TkinterServiceRequest.set_update_period-87"><span class="linenos">87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">period</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterServiceRequest.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<input id="TkinterServiceRequest.default_service_type-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="TkinterServiceRequest.default_service_type-view-value"></label><span class="default_value">&lt;class &#39;<a href="#TkinterService">TkinterService</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#TkinterServiceRequest.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="TkinterServiceRequest.default__request__type__" class="variable">default__request__type__</dd>
                <dd id="TkinterServiceRequest.request_type" class="variable">request_type</dd>
                <dd id="TkinterServiceRequest.args" class="variable">args</dd>
                <dd id="TkinterServiceRequest.kwargs" class="variable">kwargs</dd>
                <dd id="TkinterServiceRequest.provide_to_request_handler" class="variable">provide_to_request_handler</dd>
                <dd id="TkinterServiceRequest.interface" class="function">interface</dd>
                <dd id="TkinterServiceRequest.i" class="function">i</dd>
                <dd id="TkinterServiceRequest.async_interface" class="function">async_interface</dd>
                <dd id="TkinterServiceRequest.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TkObjDestroyedError">
                            <input id="TkObjDestroyedError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TkObjDestroyedError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="TkObjDestroyedError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjDestroyedError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjDestroyedError-90"><a href="#TkObjDestroyedError-90"><span class="linenos">90</span></a><span class="k">class</span> <span class="nc">TkObjDestroyedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="TkObjDestroyedError-91"><a href="#TkObjDestroyedError-91"><span class="linenos">91</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="TkObjDestroyedError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="TkObjDestroyedError.with_traceback" class="function">with_traceback</dd>
                <dd id="TkObjDestroyedError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TkObjWrapper">
                            <input id="TkObjWrapper-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TkObjWrapper</span>:

                <label class="view-source-button" for="TkObjWrapper-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper-94"><a href="#TkObjWrapper-94"><span class="linenos"> 94</span></a><span class="k">class</span> <span class="nc">TkObjWrapper</span><span class="p">:</span>
</span><span id="TkObjWrapper-95"><a href="#TkObjWrapper-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkObjWrapper-96"><a href="#TkObjWrapper-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="TkObjWrapper-97"><a href="#TkObjWrapper-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="n">tk_obj_id</span>
</span><span id="TkObjWrapper-98"><a href="#TkObjWrapper-98"><span class="linenos"> 98</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="n">tk_obj</span>
</span><span id="TkObjWrapper-99"><a href="#TkObjWrapper-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TkObjWrapper-100"><a href="#TkObjWrapper-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">destroy_on_finish</span>
</span><span id="TkObjWrapper-101"><a href="#TkObjWrapper-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_service</span><span class="p">:</span> <span class="n">TkinterService</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">)</span>
</span><span id="TkObjWrapper-102"><a href="#TkObjWrapper-102"><span class="linenos">102</span></a>    
</span><span id="TkObjWrapper-103"><a href="#TkObjWrapper-103"><span class="linenos">103</span></a>    <span class="nd">@property</span>
</span><span id="TkObjWrapper-104"><a href="#TkObjWrapper-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">tk</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper-105"><a href="#TkObjWrapper-105"><span class="linenos">105</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper-106"><a href="#TkObjWrapper-106"><span class="linenos">106</span></a>            <span class="k">raise</span> <span class="n">TkObjDestroyedError</span>
</span><span id="TkObjWrapper-107"><a href="#TkObjWrapper-107"><span class="linenos">107</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkObjWrapper-108"><a href="#TkObjWrapper-108"><span class="linenos">108</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span>
</span><span id="TkObjWrapper-109"><a href="#TkObjWrapper-109"><span class="linenos">109</span></a>    
</span><span id="TkObjWrapper-110"><a href="#TkObjWrapper-110"><span class="linenos">110</span></a>    <span class="nd">@property</span>
</span><span id="TkObjWrapper-111"><a href="#TkObjWrapper-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">tk_id</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper-112"><a href="#TkObjWrapper-112"><span class="linenos">112</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper-113"><a href="#TkObjWrapper-113"><span class="linenos">113</span></a>            <span class="k">raise</span> <span class="n">TkObjDestroyedError</span>
</span><span id="TkObjWrapper-114"><a href="#TkObjWrapper-114"><span class="linenos">114</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkObjWrapper-115"><a href="#TkObjWrapper-115"><span class="linenos">115</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span>
</span><span id="TkObjWrapper-116"><a href="#TkObjWrapper-116"><span class="linenos">116</span></a>    
</span><span id="TkObjWrapper-117"><a href="#TkObjWrapper-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="TkObjWrapper-118"><a href="#TkObjWrapper-118"><span class="linenos">118</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper-119"><a href="#TkObjWrapper-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkObjWrapper-120"><a href="#TkObjWrapper-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">destroy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">))</span>
</span><span id="TkObjWrapper-121"><a href="#TkObjWrapper-121"><span class="linenos">121</span></a>    
</span><span id="TkObjWrapper-122"><a href="#TkObjWrapper-122"><span class="linenos">122</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">adestroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="TkObjWrapper-123"><a href="#TkObjWrapper-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper-124"><a href="#TkObjWrapper-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkObjWrapper-125"><a href="#TkObjWrapper-125"><span class="linenos">125</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">destroy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">))</span>
</span><span id="TkObjWrapper-126"><a href="#TkObjWrapper-126"><span class="linenos">126</span></a>    
</span><span id="TkObjWrapper-127"><a href="#TkObjWrapper-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TkObjWrapper-128"><a href="#TkObjWrapper-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="TkObjWrapper-129"><a href="#TkObjWrapper-129"><span class="linenos">129</span></a>    
</span><span id="TkObjWrapper-130"><a href="#TkObjWrapper-130"><span class="linenos">130</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TkObjWrapper-131"><a href="#TkObjWrapper-131"><span class="linenos">131</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="TkObjWrapper-132"><a href="#TkObjWrapper-132"><span class="linenos">132</span></a>    
</span><span id="TkObjWrapper-133"><a href="#TkObjWrapper-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="TkObjWrapper-134"><a href="#TkObjWrapper-134"><span class="linenos">134</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">))</span>
</span><span id="TkObjWrapper-135"><a href="#TkObjWrapper-135"><span class="linenos">135</span></a>    
</span><span id="TkObjWrapper-136"><a href="#TkObjWrapper-136"><span class="linenos">136</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aregister_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="TkObjWrapper-137"><a href="#TkObjWrapper-137"><span class="linenos">137</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">))</span>
</span><span id="TkObjWrapper-138"><a href="#TkObjWrapper-138"><span class="linenos">138</span></a>    
</span><span id="TkObjWrapper-139"><a href="#TkObjWrapper-139"><span class="linenos">139</span></a>    <span class="nd">@property</span>
</span><span id="TkObjWrapper-140"><a href="#TkObjWrapper-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper-141"><a href="#TkObjWrapper-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service</span><span class="o">.</span><span class="n">_get_inline</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="TkObjWrapper-142"><a href="#TkObjWrapper-142"><span class="linenos">142</span></a>    
</span><span id="TkObjWrapper-143"><a href="#TkObjWrapper-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TkObjWrapper-144"><a href="#TkObjWrapper-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk</span>
</span><span id="TkObjWrapper-145"><a href="#TkObjWrapper-145"><span class="linenos">145</span></a>    
</span><span id="TkObjWrapper-146"><a href="#TkObjWrapper-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper-147"><a href="#TkObjWrapper-147"><span class="linenos">147</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span>
</span><span id="TkObjWrapper-148"><a href="#TkObjWrapper-148"><span class="linenos">148</span></a>    
</span><span id="TkObjWrapper-149"><a href="#TkObjWrapper-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="TkObjWrapper-150"><a href="#TkObjWrapper-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span><span id="TkObjWrapper-151"><a href="#TkObjWrapper-151"><span class="linenos">151</span></a>
</span><span id="TkObjWrapper-152"><a href="#TkObjWrapper-152"><span class="linenos">152</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper-153"><a href="#TkObjWrapper-153"><span class="linenos">153</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span>
</span><span id="TkObjWrapper-154"><a href="#TkObjWrapper-154"><span class="linenos">154</span></a>
</span><span id="TkObjWrapper-155"><a href="#TkObjWrapper-155"><span class="linenos">155</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="TkObjWrapper-156"><a href="#TkObjWrapper-156"><span class="linenos">156</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">adestroy</span><span class="p">()</span>
</span><span id="TkObjWrapper-157"><a href="#TkObjWrapper-157"><span class="linenos">157</span></a>    
</span><span id="TkObjWrapper-158"><a href="#TkObjWrapper-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="TkObjWrapper-159"><a href="#TkObjWrapper-159"><span class="linenos">159</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">period</span><span class="p">))</span>
</span><span id="TkObjWrapper-160"><a href="#TkObjWrapper-160"><span class="linenos">160</span></a>    
</span><span id="TkObjWrapper-161"><a href="#TkObjWrapper-161"><span class="linenos">161</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aset_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="TkObjWrapper-162"><a href="#TkObjWrapper-162"><span class="linenos">162</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">period</span><span class="p">))</span>
</span></pre></div>


    

                            <div id="TkObjWrapper.__init__" class="classattr">
                                        <input id="TkObjWrapper.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TkObjWrapper</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">interface</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="n">tk_obj_id</span>,</span><span class="param">	<span class="n">tk_obj</span>,</span><span class="param">	<span class="n">destroy_on_finish</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span>)</span>

                <label class="view-source-button" for="TkObjWrapper.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.__init__-95"><a href="#TkObjWrapper.__init__-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkObjWrapper.__init__-96"><a href="#TkObjWrapper.__init__-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="TkObjWrapper.__init__-97"><a href="#TkObjWrapper.__init__-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="n">tk_obj_id</span>
</span><span id="TkObjWrapper.__init__-98"><a href="#TkObjWrapper.__init__-98"><span class="linenos"> 98</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="n">tk_obj</span>
</span><span id="TkObjWrapper.__init__-99"><a href="#TkObjWrapper.__init__-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TkObjWrapper.__init__-100"><a href="#TkObjWrapper.__init__-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">destroy_on_finish</span>
</span><span id="TkObjWrapper.__init__-101"><a href="#TkObjWrapper.__init__-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_service</span><span class="p">:</span> <span class="n">TkinterService</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.tk" class="classattr">
                                        <input id="TkObjWrapper.tk-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">tk</span>

                <label class="view-source-button" for="TkObjWrapper.tk-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.tk"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.tk-103"><a href="#TkObjWrapper.tk-103"><span class="linenos">103</span></a>    <span class="nd">@property</span>
</span><span id="TkObjWrapper.tk-104"><a href="#TkObjWrapper.tk-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">tk</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper.tk-105"><a href="#TkObjWrapper.tk-105"><span class="linenos">105</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper.tk-106"><a href="#TkObjWrapper.tk-106"><span class="linenos">106</span></a>            <span class="k">raise</span> <span class="n">TkObjDestroyedError</span>
</span><span id="TkObjWrapper.tk-107"><a href="#TkObjWrapper.tk-107"><span class="linenos">107</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkObjWrapper.tk-108"><a href="#TkObjWrapper.tk-108"><span class="linenos">108</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.tk_id" class="classattr">
                                        <input id="TkObjWrapper.tk_id-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">tk_id</span>

                <label class="view-source-button" for="TkObjWrapper.tk_id-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.tk_id"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.tk_id-110"><a href="#TkObjWrapper.tk_id-110"><span class="linenos">110</span></a>    <span class="nd">@property</span>
</span><span id="TkObjWrapper.tk_id-111"><a href="#TkObjWrapper.tk_id-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">tk_id</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper.tk_id-112"><a href="#TkObjWrapper.tk_id-112"><span class="linenos">112</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper.tk_id-113"><a href="#TkObjWrapper.tk_id-113"><span class="linenos">113</span></a>            <span class="k">raise</span> <span class="n">TkObjDestroyedError</span>
</span><span id="TkObjWrapper.tk_id-114"><a href="#TkObjWrapper.tk_id-114"><span class="linenos">114</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkObjWrapper.tk_id-115"><a href="#TkObjWrapper.tk_id-115"><span class="linenos">115</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.destroy" class="classattr">
                                        <input id="TkObjWrapper.destroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.destroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.destroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.destroy-117"><a href="#TkObjWrapper.destroy-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="TkObjWrapper.destroy-118"><a href="#TkObjWrapper.destroy-118"><span class="linenos">118</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper.destroy-119"><a href="#TkObjWrapper.destroy-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkObjWrapper.destroy-120"><a href="#TkObjWrapper.destroy-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">destroy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.adestroy" class="classattr">
                                        <input id="TkObjWrapper.adestroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">adestroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.adestroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.adestroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.adestroy-122"><a href="#TkObjWrapper.adestroy-122"><span class="linenos">122</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">adestroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="TkObjWrapper.adestroy-123"><a href="#TkObjWrapper.adestroy-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span><span class="p">:</span>
</span><span id="TkObjWrapper.adestroy-124"><a href="#TkObjWrapper.adestroy-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkObjWrapper.adestroy-125"><a href="#TkObjWrapper.adestroy-125"><span class="linenos">125</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">destroy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.put_coro" class="classattr">
                                        <input id="TkObjWrapper.put_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_coro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ExplicitWorker</span><span class="p">,</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.put_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.put_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.put_coro-127"><a href="#TkObjWrapper.put_coro-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TkObjWrapper.put_coro-128"><a href="#TkObjWrapper.put_coro-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.aput_coro" class="classattr">
                                        <input id="TkObjWrapper.aput_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aput_coro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ExplicitWorker</span><span class="p">,</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.aput_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.aput_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.aput_coro-130"><a href="#TkObjWrapper.aput_coro-130"><span class="linenos">130</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TkObjWrapper.aput_coro-131"><a href="#TkObjWrapper.aput_coro-131"><span class="linenos">131</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.register_coro" class="classattr">
                                        <input id="TkObjWrapper.register_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.register_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.register_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.register_coro-133"><a href="#TkObjWrapper.register_coro-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="TkObjWrapper.register_coro-134"><a href="#TkObjWrapper.register_coro-134"><span class="linenos">134</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.aregister_coro" class="classattr">
                                        <input id="TkObjWrapper.aregister_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aregister_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.aregister_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.aregister_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.aregister_coro-136"><a href="#TkObjWrapper.aregister_coro-136"><span class="linenos">136</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aregister_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="TkObjWrapper.aregister_coro-137"><a href="#TkObjWrapper.aregister_coro-137"><span class="linenos">137</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.destroyed" class="classattr">
                                        <input id="TkObjWrapper.destroyed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">destroyed</span>

                <label class="view-source-button" for="TkObjWrapper.destroyed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.destroyed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.destroyed-139"><a href="#TkObjWrapper.destroyed-139"><span class="linenos">139</span></a>    <span class="nd">@property</span>
</span><span id="TkObjWrapper.destroyed-140"><a href="#TkObjWrapper.destroyed-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkObjWrapper.destroyed-141"><a href="#TkObjWrapper.destroyed-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroyed</span> <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_service</span><span class="o">.</span><span class="n">_get_inline</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.set_update_period" class="classattr">
                                        <input id="TkObjWrapper.set_update_period-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_update_period</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">period</span><span class="p">:</span> <span class="nb">float</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.set_update_period-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.set_update_period"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.set_update_period-158"><a href="#TkObjWrapper.set_update_period-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="TkObjWrapper.set_update_period-159"><a href="#TkObjWrapper.set_update_period-159"><span class="linenos">159</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">period</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TkObjWrapper.aset_update_period" class="classattr">
                                        <input id="TkObjWrapper.aset_update_period-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aset_update_period</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">period</span><span class="p">:</span> <span class="nb">float</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkObjWrapper.aset_update_period-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjWrapper.aset_update_period"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjWrapper.aset_update_period-161"><a href="#TkObjWrapper.aset_update_period-161"><span class="linenos">161</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aset_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="TkObjWrapper.aset_update_period-162"><a href="#TkObjWrapper.aset_update_period-162"><span class="linenos">162</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tk_id</span><span class="p">,</span> <span class="n">period</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="TkinterContextManager">
                            <input id="TkinterContextManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TkinterContextManager</span>:

                <label class="view-source-button" for="TkinterContextManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterContextManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterContextManager-165"><a href="#TkinterContextManager-165"><span class="linenos">165</span></a><span class="k">class</span> <span class="nc">TkinterContextManager</span><span class="p">:</span>
</span><span id="TkinterContextManager-166"><a href="#TkinterContextManager-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">tk_obj_or_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tk</span><span class="p">,</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TkinterContextManager-167"><a href="#TkinterContextManager-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">interface</span> <span class="ow">or</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TkinterContextManager-168"><a href="#TkinterContextManager-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tk</span><span class="p">,</span> <span class="n">TkObjId</span><span class="p">]]</span> <span class="o">=</span> <span class="n">tk_obj_or_id</span>
</span><span id="TkinterContextManager-169"><a href="#TkinterContextManager-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="TkinterContextManager-170"><a href="#TkinterContextManager-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="TkinterContextManager-171"><a href="#TkinterContextManager-171"><span class="linenos">171</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">:</span> <span class="n">Tk</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterContextManager-172"><a href="#TkinterContextManager-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterContextManager-173"><a href="#TkinterContextManager-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="p">:</span> <span class="n">TkObjWrapper</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterContextManager-174"><a href="#TkinterContextManager-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TkinterContextManager-175"><a href="#TkinterContextManager-175"><span class="linenos">175</span></a>    
</span><span id="TkinterContextManager-176"><a href="#TkinterContextManager-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkinterContextManager-177"><a href="#TkinterContextManager-177"><span class="linenos">177</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterContextManager-178"><a href="#TkinterContextManager-178"><span class="linenos">178</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterContextManager-179"><a href="#TkinterContextManager-179"><span class="linenos">179</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">Tk</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="TkinterContextManager-180"><a href="#TkinterContextManager-180"><span class="linenos">180</span></a>        
</span><span id="TkinterContextManager-181"><a href="#TkinterContextManager-181"><span class="linenos">181</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="TkinterContextManager-182"><a href="#TkinterContextManager-182"><span class="linenos">182</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="TkinterContextManager-183"><a href="#TkinterContextManager-183"><span class="linenos">183</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">))</span>
</span><span id="TkinterContextManager-184"><a href="#TkinterContextManager-184"><span class="linenos">184</span></a>        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">):</span>
</span><span id="TkinterContextManager-185"><a href="#TkinterContextManager-185"><span class="linenos">185</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterContextManager-186"><a href="#TkinterContextManager-186"><span class="linenos">186</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="nb">issubclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="TkinterContextManager-187"><a href="#TkinterContextManager-187"><span class="linenos">187</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s1">&#39;Given class is not a subclass of Tk&#39;</span><span class="p">)</span>
</span><span id="TkinterContextManager-188"><a href="#TkinterContextManager-188"><span class="linenos">188</span></a>            
</span><span id="TkinterContextManager-189"><a href="#TkinterContextManager-189"><span class="linenos">189</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="TkinterContextManager-190"><a href="#TkinterContextManager-190"><span class="linenos">190</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="TkinterContextManager-191"><a href="#TkinterContextManager-191"><span class="linenos">191</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkinterContextManager-192"><a href="#TkinterContextManager-192"><span class="linenos">192</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="TkinterContextManager-193"><a href="#TkinterContextManager-193"><span class="linenos">193</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="TkinterContextManager-194"><a href="#TkinterContextManager-194"><span class="linenos">194</span></a>        
</span><span id="TkinterContextManager-195"><a href="#TkinterContextManager-195"><span class="linenos">195</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span> <span class="o">=</span> <span class="n">TkObjWrapper</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span><span class="p">)</span>
</span><span id="TkinterContextManager-196"><a href="#TkinterContextManager-196"><span class="linenos">196</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span>
</span><span id="TkinterContextManager-197"><a href="#TkinterContextManager-197"><span class="linenos">197</span></a>    
</span><span id="TkinterContextManager-198"><a href="#TkinterContextManager-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="TkinterContextManager-199"><a href="#TkinterContextManager-199"><span class="linenos">199</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterContextManager-200"><a href="#TkinterContextManager-200"><span class="linenos">200</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="TkinterContextManager-201"><a href="#TkinterContextManager-201"><span class="linenos">201</span></a>
</span><span id="TkinterContextManager-202"><a href="#TkinterContextManager-202"><span class="linenos">202</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkinterContextManager-203"><a href="#TkinterContextManager-203"><span class="linenos">203</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterContextManager-204"><a href="#TkinterContextManager-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterContextManager-205"><a href="#TkinterContextManager-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">Tk</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="TkinterContextManager-206"><a href="#TkinterContextManager-206"><span class="linenos">206</span></a>        
</span><span id="TkinterContextManager-207"><a href="#TkinterContextManager-207"><span class="linenos">207</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="TkinterContextManager-208"><a href="#TkinterContextManager-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="TkinterContextManager-209"><a href="#TkinterContextManager-209"><span class="linenos">209</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">))</span>
</span><span id="TkinterContextManager-210"><a href="#TkinterContextManager-210"><span class="linenos">210</span></a>        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">):</span>
</span><span id="TkinterContextManager-211"><a href="#TkinterContextManager-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterContextManager-212"><a href="#TkinterContextManager-212"><span class="linenos">212</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="nb">issubclass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="n">Tk</span><span class="p">):</span>
</span><span id="TkinterContextManager-213"><a href="#TkinterContextManager-213"><span class="linenos">213</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s1">&#39;Given class is not a subclass of Tk&#39;</span><span class="p">)</span>
</span><span id="TkinterContextManager-214"><a href="#TkinterContextManager-214"><span class="linenos">214</span></a>            
</span><span id="TkinterContextManager-215"><a href="#TkinterContextManager-215"><span class="linenos">215</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">))</span>
</span><span id="TkinterContextManager-216"><a href="#TkinterContextManager-216"><span class="linenos">216</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="TkinterContextManager-217"><a href="#TkinterContextManager-217"><span class="linenos">217</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkinterContextManager-218"><a href="#TkinterContextManager-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span>
</span><span id="TkinterContextManager-219"><a href="#TkinterContextManager-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span><span id="TkinterContextManager-220"><a href="#TkinterContextManager-220"><span class="linenos">220</span></a>        
</span><span id="TkinterContextManager-221"><a href="#TkinterContextManager-221"><span class="linenos">221</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span> <span class="o">=</span> <span class="n">TkObjWrapper</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span><span class="p">)</span>
</span><span id="TkinterContextManager-222"><a href="#TkinterContextManager-222"><span class="linenos">222</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span>
</span><span id="TkinterContextManager-223"><a href="#TkinterContextManager-223"><span class="linenos">223</span></a>
</span><span id="TkinterContextManager-224"><a href="#TkinterContextManager-224"><span class="linenos">224</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="TkinterContextManager-225"><a href="#TkinterContextManager-225"><span class="linenos">225</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterContextManager-226"><a href="#TkinterContextManager-226"><span class="linenos">226</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="n">TkinterServiceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">))</span>
</span></pre></div>


    

                            <div id="TkinterContextManager.__init__" class="classattr">
                                        <input id="TkinterContextManager.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TkinterContextManager</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">interface</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">tk_obj_or_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">tkinter</span><span class="o">.</span><span class="n">Tk</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="n">Type</span><span class="p">[</span><span class="n">tkinter</span><span class="o">.</span><span class="n">Tk</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="TkinterContextManager.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterContextManager.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterContextManager.__init__-166"><a href="#TkinterContextManager.__init__-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Interface</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">tk_obj_or_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tk</span><span class="p">,</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TkinterContextManager.__init__-167"><a href="#TkinterContextManager.__init__-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">interface</span> <span class="ow">or</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TkinterContextManager.__init__-168"><a href="#TkinterContextManager.__init__-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_or_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tk</span><span class="p">,</span> <span class="n">TkObjId</span><span class="p">]]</span> <span class="o">=</span> <span class="n">tk_obj_or_id</span>
</span><span id="TkinterContextManager.__init__-169"><a href="#TkinterContextManager.__init__-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="TkinterContextManager.__init__-170"><a href="#TkinterContextManager.__init__-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="TkinterContextManager.__init__-171"><a href="#TkinterContextManager.__init__-171"><span class="linenos">171</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj</span><span class="p">:</span> <span class="n">Tk</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterContextManager.__init__-172"><a href="#TkinterContextManager.__init__-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_obj_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterContextManager.__init__-173"><a href="#TkinterContextManager.__init__-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tk_wrapper</span><span class="p">:</span> <span class="n">TkObjWrapper</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterContextManager.__init__-174"><a href="#TkinterContextManager.__init__-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_destroy_on_finish</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="tcm">
                    <div class="attr variable">
            <span class="name">tcm</span>        =
<input id="tcm-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="tcm-view-value"></label><span class="default_value">&lt;class &#39;<a href="#TkinterContextManager">TkinterContextManager</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#tcm"></a>
    
    

                </section>
                <section id="TkObjNotFoundError">
                            <input id="TkObjNotFoundError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TkObjNotFoundError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="TkObjNotFoundError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkObjNotFoundError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkObjNotFoundError-232"><a href="#TkObjNotFoundError-232"><span class="linenos">232</span></a><span class="k">class</span> <span class="nc">TkObjNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="TkObjNotFoundError-233"><a href="#TkObjNotFoundError-233"><span class="linenos">233</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="TkObjNotFoundError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="TkObjNotFoundError.with_traceback" class="function">with_traceback</dd>
                <dd id="TkObjNotFoundError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TkinterService">
                            <input id="TkinterService-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TkinterService</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</span>, <span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="TkinterService-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterService"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterService-236"><a href="#TkinterService-236"><span class="linenos">236</span></a><span class="k">class</span> <span class="nc">TkinterService</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="TkinterService-237"><a href="#TkinterService-237"><span class="linenos">237</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="TkinterService-238"><a href="#TkinterService-238"><span class="linenos">238</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TkinterService-239"><a href="#TkinterService-239"><span class="linenos">239</span></a>
</span><span id="TkinterService-240"><a href="#TkinterService-240"><span class="linenos">240</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="TkinterService-241"><a href="#TkinterService-241"><span class="linenos">241</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_create</span><span class="p">,</span>
</span><span id="TkinterService-242"><a href="#TkinterService-242"><span class="linenos">242</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put</span><span class="p">,</span>
</span><span id="TkinterService-243"><a href="#TkinterService-243"><span class="linenos">243</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="TkinterService-244"><a href="#TkinterService-244"><span class="linenos">244</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_destroy</span><span class="p">,</span>
</span><span id="TkinterService-245"><a href="#TkinterService-245"><span class="linenos">245</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_destroy_and_wait_for_destroyed</span><span class="p">,</span>
</span><span id="TkinterService-246"><a href="#TkinterService-246"><span class="linenos">246</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_destroyed</span><span class="p">,</span>
</span><span id="TkinterService-247"><a href="#TkinterService-247"><span class="linenos">247</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put_coro</span><span class="p">,</span>
</span><span id="TkinterService-248"><a href="#TkinterService-248"><span class="linenos">248</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_coro</span><span class="p">,</span>
</span><span id="TkinterService-249"><a href="#TkinterService-249"><span class="linenos">249</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_update_period</span><span class="p">,</span>
</span><span id="TkinterService-250"><a href="#TkinterService-250"><span class="linenos">250</span></a>        <span class="p">}</span>
</span><span id="TkinterService-251"><a href="#TkinterService-251"><span class="linenos">251</span></a>        
</span><span id="TkinterService-252"><a href="#TkinterService-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">standard_ui_update_interval</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="mi">60</span>
</span><span id="TkinterService-253"><a href="#TkinterService-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">get_usable_min_sleep_interval</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">standard_ui_update_interval</span><span class="p">)</span>
</span><span id="TkinterService-254"><a href="#TkinterService-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span>
</span><span id="TkinterService-255"><a href="#TkinterService-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-256"><a href="#TkinterService-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="TkinterService-257"><a href="#TkinterService-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Tk</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-258"><a href="#TkinterService-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-259"><a href="#TkinterService-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-260"><a href="#TkinterService-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-261"><a href="#TkinterService-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-262"><a href="#TkinterService-262"><span class="linenos">262</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TkinterService-263"><a href="#TkinterService-263"><span class="linenos">263</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-264"><a href="#TkinterService-264"><span class="linenos">264</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-265"><a href="#TkinterService-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_after_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService-266"><a href="#TkinterService-266"><span class="linenos">266</span></a>        
</span><span id="TkinterService-267"><a href="#TkinterService-267"><span class="linenos">267</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TkinterService-268"><a href="#TkinterService-268"><span class="linenos">268</span></a>    
</span><span id="TkinterService-269"><a href="#TkinterService-269"><span class="linenos">269</span></a>    <span class="k">def</span> <span class="nf">start_tk_updater</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkinterService-270"><a href="#TkinterService-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span><span class="p">:</span>
</span><span id="TkinterService-271"><a href="#TkinterService-271"><span class="linenos">271</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterService-272"><a href="#TkinterService-272"><span class="linenos">272</span></a>            <span class="n">tk_updater_coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">tk_updater</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="TkinterService-273"><a href="#TkinterService-273"><span class="linenos">273</span></a>            <span class="n">tk_updater_coro</span><span class="o">.</span><span class="n">is_background_coro</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterService-274"><a href="#TkinterService-274"><span class="linenos">274</span></a>
</span><span id="TkinterService-275"><a href="#TkinterService-275"><span class="linenos">275</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="TkinterService-276"><a href="#TkinterService-276"><span class="linenos">276</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="TkinterService-277"><a href="#TkinterService-277"><span class="linenos">277</span></a>            <span class="s1">&#39;tk_counter&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="TkinterService-278"><a href="#TkinterService-278"><span class="linenos">278</span></a>        <span class="p">}</span>
</span><span id="TkinterService-279"><a href="#TkinterService-279"><span class="linenos">279</span></a>
</span><span id="TkinterService-280"><a href="#TkinterService-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TkinterServiceRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="TkinterService-281"><a href="#TkinterService-281"><span class="linenos">281</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService-282"><a href="#TkinterService-282"><span class="linenos">282</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterService-283"><a href="#TkinterService-283"><span class="linenos">283</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="TkinterService-284"><a href="#TkinterService-284"><span class="linenos">284</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TkinterService-285"><a href="#TkinterService-285"><span class="linenos">285</span></a>
</span><span id="TkinterService-286"><a href="#TkinterService-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkinterService-287"><a href="#TkinterService-287"><span class="linenos">287</span></a>        <span class="c1"># closed</span>
</span><span id="TkinterService-288"><a href="#TkinterService-288"><span class="linenos">288</span></a>        <span class="n">new_closed_bak</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span>
</span><span id="TkinterService-289"><a href="#TkinterService-289"><span class="linenos">289</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">new_closed_bak</span><span class="p">)()</span>
</span><span id="TkinterService-290"><a href="#TkinterService-290"><span class="linenos">290</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span> <span class="ow">in</span> <span class="n">new_closed_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TkinterService-291"><a href="#TkinterService-291"><span class="linenos">291</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">just_mark_as_destroyed</span>
</span><span id="TkinterService-292"><a href="#TkinterService-292"><span class="linenos">292</span></a>        
</span><span id="TkinterService-293"><a href="#TkinterService-293"><span class="linenos">293</span></a>        <span class="c1"># waiting_for_destroyed</span>
</span><span id="TkinterService-294"><a href="#TkinterService-294"><span class="linenos">294</span></a>        <span class="n">new_destroyed_bak</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span>
</span><span id="TkinterService-295"><a href="#TkinterService-295"><span class="linenos">295</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">)()</span>
</span><span id="TkinterService-296"><a href="#TkinterService-296"><span class="linenos">296</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span> <span class="ow">in</span> <span class="n">new_destroyed_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TkinterService-297"><a href="#TkinterService-297"><span class="linenos">297</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterService-298"><a href="#TkinterService-298"><span class="linenos">298</span></a>                <span class="k">continue</span>
</span><span id="TkinterService-299"><a href="#TkinterService-299"><span class="linenos">299</span></a>                
</span><span id="TkinterService-300"><a href="#TkinterService-300"><span class="linenos">300</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="TkinterService-301"><a href="#TkinterService-301"><span class="linenos">301</span></a>            
</span><span id="TkinterService-302"><a href="#TkinterService-302"><span class="linenos">302</span></a>            <span class="n">tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService-303"><a href="#TkinterService-303"><span class="linenos">303</span></a>            
</span><span id="TkinterService-304"><a href="#TkinterService-304"><span class="linenos">304</span></a>            <span class="c1"># if tk_obj_id in self.tk_after_ids:</span>
</span><span id="TkinterService-305"><a href="#TkinterService-305"><span class="linenos">305</span></a>            <span class="c1">#     after_ids = self.tk_after_ids[tk_obj_id]</span>
</span><span id="TkinterService-306"><a href="#TkinterService-306"><span class="linenos">306</span></a>            <span class="c1">#     for after_id in after_ids:</span>
</span><span id="TkinterService-307"><a href="#TkinterService-307"><span class="linenos">307</span></a>            <span class="c1">#         tk_obj.after_cancel(after_id)</span>
</span><span id="TkinterService-308"><a href="#TkinterService-308"><span class="linenos">308</span></a>                
</span><span id="TkinterService-309"><a href="#TkinterService-309"><span class="linenos">309</span></a>            <span class="c1">#     del self.tk_after_ids[tk_obj_id]</span>
</span><span id="TkinterService-310"><a href="#TkinterService-310"><span class="linenos">310</span></a>
</span><span id="TkinterService-311"><a href="#TkinterService-311"><span class="linenos">311</span></a>            <span class="c1"># cancel_all_after(tk_obj)</span>
</span><span id="TkinterService-312"><a href="#TkinterService-312"><span class="linenos">312</span></a>            
</span><span id="TkinterService-313"><a href="#TkinterService-313"><span class="linenos">313</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span>
</span><span id="TkinterService-314"><a href="#TkinterService-314"><span class="linenos">314</span></a>                <span class="n">tk_obj</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span><span id="TkinterService-315"><a href="#TkinterService-315"><span class="linenos">315</span></a>            
</span><span id="TkinterService-316"><a href="#TkinterService-316"><span class="linenos">316</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span>
</span><span id="TkinterService-317"><a href="#TkinterService-317"><span class="linenos">317</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService-318"><a href="#TkinterService-318"><span class="linenos">318</span></a>
</span><span id="TkinterService-319"><a href="#TkinterService-319"><span class="linenos">319</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span>
</span><span id="TkinterService-320"><a href="#TkinterService-320"><span class="linenos">320</span></a>                <span class="k">for</span> <span class="n">waiter_coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]:</span>
</span><span id="TkinterService-321"><a href="#TkinterService-321"><span class="linenos">321</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">waiter_coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TkinterService-322"><a href="#TkinterService-322"><span class="linenos">322</span></a>                
</span><span id="TkinterService-323"><a href="#TkinterService-323"><span class="linenos">323</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService-324"><a href="#TkinterService-324"><span class="linenos">324</span></a>            
</span><span id="TkinterService-325"><a href="#TkinterService-325"><span class="linenos">325</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">:</span>
</span><span id="TkinterService-326"><a href="#TkinterService-326"><span class="linenos">326</span></a>                <span class="n">coros_tks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]]</span>
</span><span id="TkinterService-327"><a href="#TkinterService-327"><span class="linenos">327</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService-328"><a href="#TkinterService-328"><span class="linenos">328</span></a>                <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="n">coros_tks</span><span class="p">:</span>
</span><span id="TkinterService-329"><a href="#TkinterService-329"><span class="linenos">329</span></a>                    <span class="n">coros_tks</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="TkinterService-330"><a href="#TkinterService-330"><span class="linenos">330</span></a>
</span><span id="TkinterService-331"><a href="#TkinterService-331"><span class="linenos">331</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span>
</span><span id="TkinterService-332"><a href="#TkinterService-332"><span class="linenos">332</span></a>                <span class="n">tk_users</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService-333"><a href="#TkinterService-333"><span class="linenos">333</span></a>                <span class="k">for</span> <span class="n">tk_user_coro_id</span> <span class="ow">in</span> <span class="n">tk_users</span><span class="p">:</span>
</span><span id="TkinterService-334"><a href="#TkinterService-334"><span class="linenos">334</span></a>                    <span class="c1"># TODO: switch to an appropriate service</span>
</span><span id="TkinterService-335"><a href="#TkinterService-335"><span class="linenos">335</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">kill_coro_by_id</span><span class="p">(</span><span class="n">tk_user_coro_id</span><span class="p">)</span>
</span><span id="TkinterService-336"><a href="#TkinterService-336"><span class="linenos">336</span></a>            
</span><span id="TkinterService-337"><a href="#TkinterService-337"><span class="linenos">337</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span>
</span><span id="TkinterService-338"><a href="#TkinterService-338"><span class="linenos">338</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService-339"><a href="#TkinterService-339"><span class="linenos">339</span></a>        
</span><span id="TkinterService-340"><a href="#TkinterService-340"><span class="linenos">340</span></a>        <span class="c1"># compute min update period</span>
</span><span id="TkinterService-341"><a href="#TkinterService-341"><span class="linenos">341</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span>
</span><span id="TkinterService-342"><a href="#TkinterService-342"><span class="linenos">342</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
</span><span id="TkinterService-343"><a href="#TkinterService-343"><span class="linenos">343</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkinterService-344"><a href="#TkinterService-344"><span class="linenos">344</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span>
</span><span id="TkinterService-345"><a href="#TkinterService-345"><span class="linenos">345</span></a>        
</span><span id="TkinterService-346"><a href="#TkinterService-346"><span class="linenos">346</span></a>        <span class="c1"># general</span>
</span><span id="TkinterService-347"><a href="#TkinterService-347"><span class="linenos">347</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">):</span>
</span><span id="TkinterService-348"><a href="#TkinterService-348"><span class="linenos">348</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="TkinterService-349"><a href="#TkinterService-349"><span class="linenos">349</span></a>
</span><span id="TkinterService-350"><a href="#TkinterService-350"><span class="linenos">350</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TkinterService-351"><a href="#TkinterService-351"><span class="linenos">351</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">)</span>
</span><span id="TkinterService-352"><a href="#TkinterService-352"><span class="linenos">352</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="TkinterService-353"><a href="#TkinterService-353"><span class="linenos">353</span></a>    
</span><span id="TkinterService-354"><a href="#TkinterService-354"><span class="linenos">354</span></a>    <span class="k">def</span> <span class="nf">_on_create</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Tk</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService-355"><a href="#TkinterService-355"><span class="linenos">355</span></a>        <span class="n">tk</span> <span class="o">=</span> <span class="n">tk_class</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TkinterService-356"><a href="#TkinterService-356"><span class="linenos">356</span></a>        <span class="n">tk_id</span><span class="p">:</span> <span class="n">TkObjId</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="TkinterService-357"><a href="#TkinterService-357"><span class="linenos">357</span></a>        <span class="n">on_destroy</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_create_on_destroyed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">)</span>
</span><span id="TkinterService-358"><a href="#TkinterService-358"><span class="linenos">358</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Destroy&gt;&quot;</span><span class="p">,</span> <span class="n">on_destroy</span><span class="p">,</span> <span class="s1">&#39;+&#39;</span><span class="p">)</span>
</span><span id="TkinterService-359"><a href="#TkinterService-359"><span class="linenos">359</span></a>        <span class="n">old_on_close</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TkinterService-360"><a href="#TkinterService-360"><span class="linenos">360</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">isfunction</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ismethod</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">)):</span>
</span><span id="TkinterService-361"><a href="#TkinterService-361"><span class="linenos">361</span></a>            <span class="n">old_on_close</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterService-362"><a href="#TkinterService-362"><span class="linenos">362</span></a>        
</span><span id="TkinterService-363"><a href="#TkinterService-363"><span class="linenos">363</span></a>        <span class="n">on_create_on_closed</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_create_on_closed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">,</span> <span class="n">old_on_close</span><span class="p">)</span>
</span><span id="TkinterService-364"><a href="#TkinterService-364"><span class="linenos">364</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="n">on_create_on_closed</span><span class="p">)</span>
</span><span id="TkinterService-365"><a href="#TkinterService-365"><span class="linenos">365</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">tk</span>
</span><span id="TkinterService-366"><a href="#TkinterService-366"><span class="linenos">366</span></a>        <span class="n">coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span>
</span><span id="TkinterService-367"><a href="#TkinterService-367"><span class="linenos">367</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="TkinterService-368"><a href="#TkinterService-368"><span class="linenos">368</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">:</span>
</span><span id="TkinterService-369"><a href="#TkinterService-369"><span class="linenos">369</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TkinterService-370"><a href="#TkinterService-370"><span class="linenos">370</span></a>            <span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_created_coro_del_handler</span><span class="p">)</span>
</span><span id="TkinterService-371"><a href="#TkinterService-371"><span class="linenos">371</span></a>        
</span><span id="TkinterService-372"><a href="#TkinterService-372"><span class="linenos">372</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="TkinterService-373"><a href="#TkinterService-373"><span class="linenos">373</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">coro_id</span>
</span><span id="TkinterService-374"><a href="#TkinterService-374"><span class="linenos">374</span></a>        <span class="c1"># after_setup(tk, 1)</span>
</span><span id="TkinterService-375"><a href="#TkinterService-375"><span class="linenos">375</span></a>        <span class="n">after_idle_setup</span><span class="p">(</span><span class="n">tk</span><span class="p">)</span>
</span><span id="TkinterService-376"><a href="#TkinterService-376"><span class="linenos">376</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_tk_updater</span><span class="p">()</span>
</span><span id="TkinterService-377"><a href="#TkinterService-377"><span class="linenos">377</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TkinterService-378"><a href="#TkinterService-378"><span class="linenos">378</span></a>    
</span><span id="TkinterService-379"><a href="#TkinterService-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="nf">_on_put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService-380"><a href="#TkinterService-380"><span class="linenos">380</span></a>        <span class="n">tk</span><span class="p">:</span> <span class="n">Tk</span> <span class="o">=</span> <span class="n">tk_obj</span>
</span><span id="TkinterService-381"><a href="#TkinterService-381"><span class="linenos">381</span></a>        <span class="n">tk_id</span><span class="p">:</span> <span class="n">TkObjId</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="TkinterService-382"><a href="#TkinterService-382"><span class="linenos">382</span></a>        <span class="n">on_destroy</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_put_on_destroyed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">)</span>
</span><span id="TkinterService-383"><a href="#TkinterService-383"><span class="linenos">383</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Destroy&gt;&quot;</span><span class="p">,</span> <span class="n">on_destroy</span><span class="p">,</span> <span class="s1">&#39;+&#39;</span><span class="p">)</span>
</span><span id="TkinterService-384"><a href="#TkinterService-384"><span class="linenos">384</span></a>        <span class="n">old_on_close</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TkinterService-385"><a href="#TkinterService-385"><span class="linenos">385</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">isfunction</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ismethod</span><span class="p">(</span><span class="n">old_on_close</span><span class="p">)):</span>
</span><span id="TkinterService-386"><a href="#TkinterService-386"><span class="linenos">386</span></a>            <span class="n">old_on_close</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterService-387"><a href="#TkinterService-387"><span class="linenos">387</span></a>        
</span><span id="TkinterService-388"><a href="#TkinterService-388"><span class="linenos">388</span></a>        <span class="n">on_put_on_closed</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_put_on_closed</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk</span><span class="p">,</span> <span class="n">old_on_close</span><span class="p">)</span>
</span><span id="TkinterService-389"><a href="#TkinterService-389"><span class="linenos">389</span></a>        <span class="n">tk</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s2">&quot;WM_DELETE_WINDOW&quot;</span><span class="p">,</span> <span class="n">on_put_on_closed</span><span class="p">)</span>
</span><span id="TkinterService-390"><a href="#TkinterService-390"><span class="linenos">390</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">tk</span>
</span><span id="TkinterService-391"><a href="#TkinterService-391"><span class="linenos">391</span></a>        <span class="n">coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span>
</span><span id="TkinterService-392"><a href="#TkinterService-392"><span class="linenos">392</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="TkinterService-393"><a href="#TkinterService-393"><span class="linenos">393</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">:</span>
</span><span id="TkinterService-394"><a href="#TkinterService-394"><span class="linenos">394</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TkinterService-395"><a href="#TkinterService-395"><span class="linenos">395</span></a>            <span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_put_coro_del_handler</span><span class="p">)</span>
</span><span id="TkinterService-396"><a href="#TkinterService-396"><span class="linenos">396</span></a>        
</span><span id="TkinterService-397"><a href="#TkinterService-397"><span class="linenos">397</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="TkinterService-398"><a href="#TkinterService-398"><span class="linenos">398</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">coro_id</span>
</span><span id="TkinterService-399"><a href="#TkinterService-399"><span class="linenos">399</span></a>        <span class="c1"># after_setup(tk, 1)</span>
</span><span id="TkinterService-400"><a href="#TkinterService-400"><span class="linenos">400</span></a>        <span class="n">after_idle_setup</span><span class="p">(</span><span class="n">tk</span><span class="p">)</span>
</span><span id="TkinterService-401"><a href="#TkinterService-401"><span class="linenos">401</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_tk_updater</span><span class="p">()</span>
</span><span id="TkinterService-402"><a href="#TkinterService-402"><span class="linenos">402</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">tk_id</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TkinterService-403"><a href="#TkinterService-403"><span class="linenos">403</span></a>    
</span><span id="TkinterService-404"><a href="#TkinterService-404"><span class="linenos">404</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService-405"><a href="#TkinterService-405"><span class="linenos">405</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span>
</span><span id="TkinterService-406"><a href="#TkinterService-406"><span class="linenos">406</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">],</span> <span class="kc">None</span>
</span><span id="TkinterService-407"><a href="#TkinterService-407"><span class="linenos">407</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkinterService-408"><a href="#TkinterService-408"><span class="linenos">408</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">TkObjNotFoundError</span><span class="p">()</span>
</span><span id="TkinterService-409"><a href="#TkinterService-409"><span class="linenos">409</span></a>    
</span><span id="TkinterService-410"><a href="#TkinterService-410"><span class="linenos">410</span></a>    <span class="k">def</span> <span class="nf">_get_inline</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tk</span><span class="p">]:</span>
</span><span id="TkinterService-411"><a href="#TkinterService-411"><span class="linenos">411</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TkinterService-412"><a href="#TkinterService-412"><span class="linenos">412</span></a>    
</span><span id="TkinterService-413"><a href="#TkinterService-413"><span class="linenos">413</span></a>    <span class="k">def</span> <span class="nf">_on_destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService-414"><a href="#TkinterService-414"><span class="linenos">414</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">just_mark_as_destroyed</span>
</span><span id="TkinterService-415"><a href="#TkinterService-415"><span class="linenos">415</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-416"><a href="#TkinterService-416"><span class="linenos">416</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TkinterService-417"><a href="#TkinterService-417"><span class="linenos">417</span></a>    
</span><span id="TkinterService-418"><a href="#TkinterService-418"><span class="linenos">418</span></a>    <span class="k">def</span> <span class="nf">_on_destroy_and_wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService-419"><a href="#TkinterService-419"><span class="linenos">419</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">just_mark_as_destroyed</span>
</span><span id="TkinterService-420"><a href="#TkinterService-420"><span class="linenos">420</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_destroyed</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="TkinterService-421"><a href="#TkinterService-421"><span class="linenos">421</span></a>    
</span><span id="TkinterService-422"><a href="#TkinterService-422"><span class="linenos">422</span></a>    <span class="k">def</span> <span class="nf">_on_wait_for_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService-423"><a href="#TkinterService-423"><span class="linenos">423</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterService-424"><a href="#TkinterService-424"><span class="linenos">424</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TkinterService-425"><a href="#TkinterService-425"><span class="linenos">425</span></a>        
</span><span id="TkinterService-426"><a href="#TkinterService-426"><span class="linenos">426</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span>
</span><span id="TkinterService-427"><a href="#TkinterService-427"><span class="linenos">427</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TkinterService-428"><a href="#TkinterService-428"><span class="linenos">428</span></a>        
</span><span id="TkinterService-429"><a href="#TkinterService-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="TkinterService-430"><a href="#TkinterService-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-431"><a href="#TkinterService-431"><span class="linenos">431</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TkinterService-432"><a href="#TkinterService-432"><span class="linenos">432</span></a>    
</span><span id="TkinterService-433"><a href="#TkinterService-433"><span class="linenos">433</span></a>    <span class="k">def</span> <span class="nf">_on_put_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TkinterService-434"><a href="#TkinterService-434"><span class="linenos">434</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterService-435"><a href="#TkinterService-435"><span class="linenos">435</span></a>        <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterService-436"><a href="#TkinterService-436"><span class="linenos">436</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TkinterService-437"><a href="#TkinterService-437"><span class="linenos">437</span></a>            <span class="c1"># TODO: switch to an appropriate service</span>
</span><span id="TkinterService-438"><a href="#TkinterService-438"><span class="linenos">438</span></a>            <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="TkinterService-439"><a href="#TkinterService-439"><span class="linenos">439</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="TkinterService-440"><a href="#TkinterService-440"><span class="linenos">440</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TkinterService-441"><a href="#TkinterService-441"><span class="linenos">441</span></a>        
</span><span id="TkinterService-442"><a href="#TkinterService-442"><span class="linenos">442</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_register_coro_impl</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="TkinterService-443"><a href="#TkinterService-443"><span class="linenos">443</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="TkinterService-444"><a href="#TkinterService-444"><span class="linenos">444</span></a>    
</span><span id="TkinterService-445"><a href="#TkinterService-445"><span class="linenos">445</span></a>    <span class="k">def</span> <span class="nf">_on_register_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="TkinterService-446"><a href="#TkinterService-446"><span class="linenos">446</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TkinterService-447"><a href="#TkinterService-447"><span class="linenos">447</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TkinterService-448"><a href="#TkinterService-448"><span class="linenos">448</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_register_coro_impl</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="TkinterService-449"><a href="#TkinterService-449"><span class="linenos">449</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="TkinterService-450"><a href="#TkinterService-450"><span class="linenos">450</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TkinterService-451"><a href="#TkinterService-451"><span class="linenos">451</span></a>        
</span><span id="TkinterService-452"><a href="#TkinterService-452"><span class="linenos">452</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="TkinterService-453"><a href="#TkinterService-453"><span class="linenos">453</span></a>    
</span><span id="TkinterService-454"><a href="#TkinterService-454"><span class="linenos">454</span></a>    <span class="k">def</span> <span class="nf">_register_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">):</span>
</span><span id="TkinterService-455"><a href="#TkinterService-455"><span class="linenos">455</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span>
</span><span id="TkinterService-456"><a href="#TkinterService-456"><span class="linenos">456</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TkinterService-457"><a href="#TkinterService-457"><span class="linenos">457</span></a>        
</span><span id="TkinterService-458"><a href="#TkinterService-458"><span class="linenos">458</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="TkinterService-459"><a href="#TkinterService-459"><span class="linenos">459</span></a>
</span><span id="TkinterService-460"><a href="#TkinterService-460"><span class="linenos">460</span></a>    <span class="k">def</span> <span class="nf">_on_set_update_period</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">period</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="TkinterService-461"><a href="#TkinterService-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">period</span>
</span><span id="TkinterService-462"><a href="#TkinterService-462"><span class="linenos">462</span></a>        
</span><span id="TkinterService-463"><a href="#TkinterService-463"><span class="linenos">463</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-464"><a href="#TkinterService-464"><span class="linenos">464</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="TkinterService-465"><a href="#TkinterService-465"><span class="linenos">465</span></a>
</span><span id="TkinterService-466"><a href="#TkinterService-466"><span class="linenos">466</span></a>    <span class="k">def</span> <span class="nf">_on_created_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TkinterService-467"><a href="#TkinterService-467"><span class="linenos">467</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="TkinterService-468"><a href="#TkinterService-468"><span class="linenos">468</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TkinterService-469"><a href="#TkinterService-469"><span class="linenos">469</span></a>        
</span><span id="TkinterService-470"><a href="#TkinterService-470"><span class="linenos">470</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-471"><a href="#TkinterService-471"><span class="linenos">471</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="TkinterService-472"><a href="#TkinterService-472"><span class="linenos">472</span></a>
</span><span id="TkinterService-473"><a href="#TkinterService-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">_on_put_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TkinterService-474"><a href="#TkinterService-474"><span class="linenos">474</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="TkinterService-475"><a href="#TkinterService-475"><span class="linenos">475</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterService-476"><a href="#TkinterService-476"><span class="linenos">476</span></a>        
</span><span id="TkinterService-477"><a href="#TkinterService-477"><span class="linenos">477</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-478"><a href="#TkinterService-478"><span class="linenos">478</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="TkinterService-479"><a href="#TkinterService-479"><span class="linenos">479</span></a>    
</span><span id="TkinterService-480"><a href="#TkinterService-480"><span class="linenos">480</span></a>    <span class="k">def</span> <span class="nf">_on_create_on_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="TkinterService-481"><a href="#TkinterService-481"><span class="linenos">481</span></a>        <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">widget</span> <span class="ow">is</span> <span class="n">tk_obj</span><span class="p">:</span>
</span><span id="TkinterService-482"><a href="#TkinterService-482"><span class="linenos">482</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterService-483"><a href="#TkinterService-483"><span class="linenos">483</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterService-484"><a href="#TkinterService-484"><span class="linenos">484</span></a>        
</span><span id="TkinterService-485"><a href="#TkinterService-485"><span class="linenos">485</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-486"><a href="#TkinterService-486"><span class="linenos">486</span></a>    
</span><span id="TkinterService-487"><a href="#TkinterService-487"><span class="linenos">487</span></a>    <span class="k">def</span> <span class="nf">_on_put_on_destroyed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk_obj</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="TkinterService-488"><a href="#TkinterService-488"><span class="linenos">488</span></a>        <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">widget</span> <span class="ow">is</span> <span class="n">tk_obj</span><span class="p">:</span>
</span><span id="TkinterService-489"><a href="#TkinterService-489"><span class="linenos">489</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterService-490"><a href="#TkinterService-490"><span class="linenos">490</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterService-491"><a href="#TkinterService-491"><span class="linenos">491</span></a>        
</span><span id="TkinterService-492"><a href="#TkinterService-492"><span class="linenos">492</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-493"><a href="#TkinterService-493"><span class="linenos">493</span></a>    
</span><span id="TkinterService-494"><a href="#TkinterService-494"><span class="linenos">494</span></a>    <span class="k">def</span> <span class="nf">_on_create_on_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">previous_on_close</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]):</span>
</span><span id="TkinterService-495"><a href="#TkinterService-495"><span class="linenos">495</span></a>        <span class="k">if</span> <span class="n">previous_on_close</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterService-496"><a href="#TkinterService-496"><span class="linenos">496</span></a>            <span class="n">previous_on_close</span><span class="p">()</span>
</span><span id="TkinterService-497"><a href="#TkinterService-497"><span class="linenos">497</span></a>        
</span><span id="TkinterService-498"><a href="#TkinterService-498"><span class="linenos">498</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterService-499"><a href="#TkinterService-499"><span class="linenos">499</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TkinterService-500"><a href="#TkinterService-500"><span class="linenos">500</span></a>
</span><span id="TkinterService-501"><a href="#TkinterService-501"><span class="linenos">501</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="TkinterService-502"><a href="#TkinterService-502"><span class="linenos">502</span></a>    
</span><span id="TkinterService-503"><a href="#TkinterService-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="nf">_on_put_on_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tk_obj_id</span><span class="p">:</span> <span class="n">TkObjId</span><span class="p">,</span> <span class="n">tk</span><span class="p">:</span> <span class="n">Tk</span><span class="p">,</span> <span class="n">previous_on_close</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]):</span>
</span><span id="TkinterService-504"><a href="#TkinterService-504"><span class="linenos">504</span></a>        <span class="k">if</span> <span class="n">previous_on_close</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterService-505"><a href="#TkinterService-505"><span class="linenos">505</span></a>            <span class="n">previous_on_close</span><span class="p">()</span>
</span><span id="TkinterService-506"><a href="#TkinterService-506"><span class="linenos">506</span></a>        
</span><span id="TkinterService-507"><a href="#TkinterService-507"><span class="linenos">507</span></a>        <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterService-508"><a href="#TkinterService-508"><span class="linenos">508</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TkinterService-509"><a href="#TkinterService-509"><span class="linenos">509</span></a>
</span><span id="TkinterService-510"><a href="#TkinterService-510"><span class="linenos">510</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="TkinterService.__init__" class="classattr">
                                        <input id="TkinterService.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TkinterService</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="TkinterService.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterService.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterService.__init__-237"><a href="#TkinterService.__init__-237"><span class="linenos">237</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="TkinterService.__init__-238"><a href="#TkinterService.__init__-238"><span class="linenos">238</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">TkinterService</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TkinterService.__init__-239"><a href="#TkinterService.__init__-239"><span class="linenos">239</span></a>
</span><span id="TkinterService.__init__-240"><a href="#TkinterService.__init__-240"><span class="linenos">240</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="TkinterService.__init__-241"><a href="#TkinterService.__init__-241"><span class="linenos">241</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_create</span><span class="p">,</span>
</span><span id="TkinterService.__init__-242"><a href="#TkinterService.__init__-242"><span class="linenos">242</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put</span><span class="p">,</span>
</span><span id="TkinterService.__init__-243"><a href="#TkinterService.__init__-243"><span class="linenos">243</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="TkinterService.__init__-244"><a href="#TkinterService.__init__-244"><span class="linenos">244</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_destroy</span><span class="p">,</span>
</span><span id="TkinterService.__init__-245"><a href="#TkinterService.__init__-245"><span class="linenos">245</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_destroy_and_wait_for_destroyed</span><span class="p">,</span>
</span><span id="TkinterService.__init__-246"><a href="#TkinterService.__init__-246"><span class="linenos">246</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_destroyed</span><span class="p">,</span>
</span><span id="TkinterService.__init__-247"><a href="#TkinterService.__init__-247"><span class="linenos">247</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put_coro</span><span class="p">,</span>
</span><span id="TkinterService.__init__-248"><a href="#TkinterService.__init__-248"><span class="linenos">248</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_coro</span><span class="p">,</span>
</span><span id="TkinterService.__init__-249"><a href="#TkinterService.__init__-249"><span class="linenos">249</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_update_period</span><span class="p">,</span>
</span><span id="TkinterService.__init__-250"><a href="#TkinterService.__init__-250"><span class="linenos">250</span></a>        <span class="p">}</span>
</span><span id="TkinterService.__init__-251"><a href="#TkinterService.__init__-251"><span class="linenos">251</span></a>        
</span><span id="TkinterService.__init__-252"><a href="#TkinterService.__init__-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">standard_ui_update_interval</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="mi">60</span>
</span><span id="TkinterService.__init__-253"><a href="#TkinterService.__init__-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">get_usable_min_sleep_interval</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">standard_ui_update_interval</span><span class="p">)</span>
</span><span id="TkinterService.__init__-254"><a href="#TkinterService.__init__-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span>
</span><span id="TkinterService.__init__-255"><a href="#TkinterService.__init__-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-256"><a href="#TkinterService.__init__-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="TkinterService.__init__-257"><a href="#TkinterService.__init__-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Tk</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-258"><a href="#TkinterService.__init__-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-259"><a href="#TkinterService.__init__-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-260"><a href="#TkinterService.__init__-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-261"><a href="#TkinterService.__init__-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-262"><a href="#TkinterService.__init__-262"><span class="linenos">262</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TkinterService.__init__-263"><a href="#TkinterService.__init__-263"><span class="linenos">263</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-264"><a href="#TkinterService.__init__-264"><span class="linenos">264</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-265"><a href="#TkinterService.__init__-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tk_after_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TkObjId</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TkinterService.__init__-266"><a href="#TkinterService.__init__-266"><span class="linenos">266</span></a>        
</span><span id="TkinterService.__init__-267"><a href="#TkinterService.__init__-267"><span class="linenos">267</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterService.standard_ui_update_interval" class="classattr">
                                <div class="attr variable">
            <span class="name">standard_ui_update_interval</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.standard_ui_update_interval"></a>
    
    

                            </div>
                            <div id="TkinterService.default_update_period" class="classattr">
                                <div class="attr variable">
            <span class="name">default_update_period</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.default_update_period"></a>
    
    

                            </div>
                            <div id="TkinterService.update_period" class="classattr">
                                <div class="attr variable">
            <span class="name">update_period</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.update_period"></a>
    
    

                            </div>
                            <div id="TkinterService.update_periods" class="classattr">
                                <div class="attr variable">
            <span class="name">update_periods</span><span class="annotation">: Dict[int, float]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.update_periods"></a>
    
    

                            </div>
                            <div id="TkinterService.tk_counter" class="classattr">
                                <div class="attr variable">
            <span class="name">tk_counter</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.tk_counter"></a>
    
    

                            </div>
                            <div id="TkinterService.tk_by_id" class="classattr">
                                <div class="attr variable">
            <span class="name">tk_by_id</span><span class="annotation">: Dict[int, tkinter.Tk]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.tk_by_id"></a>
    
    

                            </div>
                            <div id="TkinterService.coroutines" class="classattr">
                                <div class="attr variable">
            <span class="name">coroutines</span><span class="annotation">: Dict[int, Set[int]]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.coroutines"></a>
    
    

                            </div>
                            <div id="TkinterService.waiting_for_destroyed" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_destroyed</span><span class="annotation">: Dict[int, Set[int]]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.waiting_for_destroyed"></a>
    
    

                            </div>
                            <div id="TkinterService.new_destroyed" class="classattr">
                                <div class="attr variable">
            <span class="name">new_destroyed</span><span class="annotation">: Dict[int, bool]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.new_destroyed"></a>
    
    

                            </div>
                            <div id="TkinterService.new_closed" class="classattr">
                                <div class="attr variable">
            <span class="name">new_closed</span><span class="annotation">: Dict[int, bool]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.new_closed"></a>
    
    

                            </div>
                            <div id="TkinterService.destroyed" class="classattr">
                                <div class="attr variable">
            <span class="name">destroyed</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.destroyed"></a>
    
    

                            </div>
                            <div id="TkinterService.coro_by_tk" class="classattr">
                                <div class="attr variable">
            <span class="name">coro_by_tk</span><span class="annotation">: Dict[int, int]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.coro_by_tk"></a>
    
    

                            </div>
                            <div id="TkinterService.tk_users" class="classattr">
                                <div class="attr variable">
            <span class="name">tk_users</span><span class="annotation">: Dict[int, Set[int]]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.tk_users"></a>
    
    

                            </div>
                            <div id="TkinterService.tk_after_ids" class="classattr">
                                <div class="attr variable">
            <span class="name">tk_after_ids</span><span class="annotation">: Dict[int, Set[str]]</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.tk_after_ids"></a>
    
    

                            </div>
                            <div id="TkinterService.updater_running" class="classattr">
                                <div class="attr variable">
            <span class="name">updater_running</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#TkinterService.updater_running"></a>
    
    

                            </div>
                            <div id="TkinterService.start_tk_updater" class="classattr">
                                        <input id="TkinterService.start_tk_updater-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start_tk_updater</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkinterService.start_tk_updater-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterService.start_tk_updater"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterService.start_tk_updater-269"><a href="#TkinterService.start_tk_updater-269"><span class="linenos">269</span></a>    <span class="k">def</span> <span class="nf">start_tk_updater</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkinterService.start_tk_updater-270"><a href="#TkinterService.start_tk_updater-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span><span class="p">:</span>
</span><span id="TkinterService.start_tk_updater-271"><a href="#TkinterService.start_tk_updater-271"><span class="linenos">271</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">updater_running</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TkinterService.start_tk_updater-272"><a href="#TkinterService.start_tk_updater-272"><span class="linenos">272</span></a>            <span class="n">tk_updater_coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">tk_updater</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="TkinterService.start_tk_updater-273"><a href="#TkinterService.start_tk_updater-273"><span class="linenos">273</span></a>            <span class="n">tk_updater_coro</span><span class="o">.</span><span class="n">is_background_coro</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterService.get_entity_stats" class="classattr">
                                        <input id="TkinterService.get_entity_stats-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_entity_stats</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">stats_level</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="TkinterService.get_entity_stats-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterService.get_entity_stats"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterService.get_entity_stats-275"><a href="#TkinterService.get_entity_stats-275"><span class="linenos">275</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="TkinterService.get_entity_stats-276"><a href="#TkinterService.get_entity_stats-276"><span class="linenos">276</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="TkinterService.get_entity_stats-277"><a href="#TkinterService.get_entity_stats-277"><span class="linenos">277</span></a>            <span class="s1">&#39;tk_counter&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_counter</span><span class="o">.</span><span class="n">_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="TkinterService.get_entity_stats-278"><a href="#TkinterService.get_entity_stats-278"><span class="linenos">278</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterService.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="TkinterService.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#TkinterServiceRequest">TkinterServiceRequest</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="TkinterService.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterService.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterService.single_task_registration_or_immediate_processing-280"><a href="#TkinterService.single_task_registration_or_immediate_processing-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TkinterServiceRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="TkinterService.single_task_registration_or_immediate_processing-281"><a href="#TkinterService.single_task_registration_or_immediate_processing-281"><span class="linenos">281</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="TkinterService.single_task_registration_or_immediate_processing-282"><a href="#TkinterService.single_task_registration_or_immediate_processing-282"><span class="linenos">282</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TkinterService.single_task_registration_or_immediate_processing-283"><a href="#TkinterService.single_task_registration_or_immediate_processing-283"><span class="linenos">283</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="TkinterService.single_task_registration_or_immediate_processing-284"><a href="#TkinterService.single_task_registration_or_immediate_processing-284"><span class="linenos">284</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterService.full_processing_iteration" class="classattr">
                                        <input id="TkinterService.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TkinterService.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterService.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterService.full_processing_iteration-286"><a href="#TkinterService.full_processing_iteration-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TkinterService.full_processing_iteration-287"><a href="#TkinterService.full_processing_iteration-287"><span class="linenos">287</span></a>        <span class="c1"># closed</span>
</span><span id="TkinterService.full_processing_iteration-288"><a href="#TkinterService.full_processing_iteration-288"><span class="linenos">288</span></a>        <span class="n">new_closed_bak</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span>
</span><span id="TkinterService.full_processing_iteration-289"><a href="#TkinterService.full_processing_iteration-289"><span class="linenos">289</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">new_closed_bak</span><span class="p">)()</span>
</span><span id="TkinterService.full_processing_iteration-290"><a href="#TkinterService.full_processing_iteration-290"><span class="linenos">290</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span> <span class="ow">in</span> <span class="n">new_closed_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TkinterService.full_processing_iteration-291"><a href="#TkinterService.full_processing_iteration-291"><span class="linenos">291</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">just_mark_as_destroyed</span>
</span><span id="TkinterService.full_processing_iteration-292"><a href="#TkinterService.full_processing_iteration-292"><span class="linenos">292</span></a>        
</span><span id="TkinterService.full_processing_iteration-293"><a href="#TkinterService.full_processing_iteration-293"><span class="linenos">293</span></a>        <span class="c1"># waiting_for_destroyed</span>
</span><span id="TkinterService.full_processing_iteration-294"><a href="#TkinterService.full_processing_iteration-294"><span class="linenos">294</span></a>        <span class="n">new_destroyed_bak</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span>
</span><span id="TkinterService.full_processing_iteration-295"><a href="#TkinterService.full_processing_iteration-295"><span class="linenos">295</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">)()</span>
</span><span id="TkinterService.full_processing_iteration-296"><a href="#TkinterService.full_processing_iteration-296"><span class="linenos">296</span></a>        <span class="k">for</span> <span class="n">tk_obj_id</span><span class="p">,</span> <span class="n">just_mark_as_destroyed</span> <span class="ow">in</span> <span class="n">new_destroyed_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TkinterService.full_processing_iteration-297"><a href="#TkinterService.full_processing_iteration-297"><span class="linenos">297</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-298"><a href="#TkinterService.full_processing_iteration-298"><span class="linenos">298</span></a>                <span class="k">continue</span>
</span><span id="TkinterService.full_processing_iteration-299"><a href="#TkinterService.full_processing_iteration-299"><span class="linenos">299</span></a>                
</span><span id="TkinterService.full_processing_iteration-300"><a href="#TkinterService.full_processing_iteration-300"><span class="linenos">300</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">destroyed</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="TkinterService.full_processing_iteration-301"><a href="#TkinterService.full_processing_iteration-301"><span class="linenos">301</span></a>            
</span><span id="TkinterService.full_processing_iteration-302"><a href="#TkinterService.full_processing_iteration-302"><span class="linenos">302</span></a>            <span class="n">tk_obj</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService.full_processing_iteration-303"><a href="#TkinterService.full_processing_iteration-303"><span class="linenos">303</span></a>            
</span><span id="TkinterService.full_processing_iteration-304"><a href="#TkinterService.full_processing_iteration-304"><span class="linenos">304</span></a>            <span class="c1"># if tk_obj_id in self.tk_after_ids:</span>
</span><span id="TkinterService.full_processing_iteration-305"><a href="#TkinterService.full_processing_iteration-305"><span class="linenos">305</span></a>            <span class="c1">#     after_ids = self.tk_after_ids[tk_obj_id]</span>
</span><span id="TkinterService.full_processing_iteration-306"><a href="#TkinterService.full_processing_iteration-306"><span class="linenos">306</span></a>            <span class="c1">#     for after_id in after_ids:</span>
</span><span id="TkinterService.full_processing_iteration-307"><a href="#TkinterService.full_processing_iteration-307"><span class="linenos">307</span></a>            <span class="c1">#         tk_obj.after_cancel(after_id)</span>
</span><span id="TkinterService.full_processing_iteration-308"><a href="#TkinterService.full_processing_iteration-308"><span class="linenos">308</span></a>                
</span><span id="TkinterService.full_processing_iteration-309"><a href="#TkinterService.full_processing_iteration-309"><span class="linenos">309</span></a>            <span class="c1">#     del self.tk_after_ids[tk_obj_id]</span>
</span><span id="TkinterService.full_processing_iteration-310"><a href="#TkinterService.full_processing_iteration-310"><span class="linenos">310</span></a>
</span><span id="TkinterService.full_processing_iteration-311"><a href="#TkinterService.full_processing_iteration-311"><span class="linenos">311</span></a>            <span class="c1"># cancel_all_after(tk_obj)</span>
</span><span id="TkinterService.full_processing_iteration-312"><a href="#TkinterService.full_processing_iteration-312"><span class="linenos">312</span></a>            
</span><span id="TkinterService.full_processing_iteration-313"><a href="#TkinterService.full_processing_iteration-313"><span class="linenos">313</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">just_mark_as_destroyed</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-314"><a href="#TkinterService.full_processing_iteration-314"><span class="linenos">314</span></a>                <span class="n">tk_obj</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span><span id="TkinterService.full_processing_iteration-315"><a href="#TkinterService.full_processing_iteration-315"><span class="linenos">315</span></a>            
</span><span id="TkinterService.full_processing_iteration-316"><a href="#TkinterService.full_processing_iteration-316"><span class="linenos">316</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-317"><a href="#TkinterService.full_processing_iteration-317"><span class="linenos">317</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService.full_processing_iteration-318"><a href="#TkinterService.full_processing_iteration-318"><span class="linenos">318</span></a>
</span><span id="TkinterService.full_processing_iteration-319"><a href="#TkinterService.full_processing_iteration-319"><span class="linenos">319</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-320"><a href="#TkinterService.full_processing_iteration-320"><span class="linenos">320</span></a>                <span class="k">for</span> <span class="n">waiter_coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]:</span>
</span><span id="TkinterService.full_processing_iteration-321"><a href="#TkinterService.full_processing_iteration-321"><span class="linenos">321</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">waiter_coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TkinterService.full_processing_iteration-322"><a href="#TkinterService.full_processing_iteration-322"><span class="linenos">322</span></a>                
</span><span id="TkinterService.full_processing_iteration-323"><a href="#TkinterService.full_processing_iteration-323"><span class="linenos">323</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_destroyed</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService.full_processing_iteration-324"><a href="#TkinterService.full_processing_iteration-324"><span class="linenos">324</span></a>            
</span><span id="TkinterService.full_processing_iteration-325"><a href="#TkinterService.full_processing_iteration-325"><span class="linenos">325</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-326"><a href="#TkinterService.full_processing_iteration-326"><span class="linenos">326</span></a>                <span class="n">coros_tks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]]</span>
</span><span id="TkinterService.full_processing_iteration-327"><a href="#TkinterService.full_processing_iteration-327"><span class="linenos">327</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_by_tk</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService.full_processing_iteration-328"><a href="#TkinterService.full_processing_iteration-328"><span class="linenos">328</span></a>                <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="n">coros_tks</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-329"><a href="#TkinterService.full_processing_iteration-329"><span class="linenos">329</span></a>                    <span class="n">coros_tks</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">tk_obj_id</span><span class="p">)</span>
</span><span id="TkinterService.full_processing_iteration-330"><a href="#TkinterService.full_processing_iteration-330"><span class="linenos">330</span></a>
</span><span id="TkinterService.full_processing_iteration-331"><a href="#TkinterService.full_processing_iteration-331"><span class="linenos">331</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-332"><a href="#TkinterService.full_processing_iteration-332"><span class="linenos">332</span></a>                <span class="n">tk_users</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tk_users</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService.full_processing_iteration-333"><a href="#TkinterService.full_processing_iteration-333"><span class="linenos">333</span></a>                <span class="k">for</span> <span class="n">tk_user_coro_id</span> <span class="ow">in</span> <span class="n">tk_users</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-334"><a href="#TkinterService.full_processing_iteration-334"><span class="linenos">334</span></a>                    <span class="c1"># TODO: switch to an appropriate service</span>
</span><span id="TkinterService.full_processing_iteration-335"><a href="#TkinterService.full_processing_iteration-335"><span class="linenos">335</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">kill_coro_by_id</span><span class="p">(</span><span class="n">tk_user_coro_id</span><span class="p">)</span>
</span><span id="TkinterService.full_processing_iteration-336"><a href="#TkinterService.full_processing_iteration-336"><span class="linenos">336</span></a>            
</span><span id="TkinterService.full_processing_iteration-337"><a href="#TkinterService.full_processing_iteration-337"><span class="linenos">337</span></a>            <span class="k">if</span> <span class="n">tk_obj_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-338"><a href="#TkinterService.full_processing_iteration-338"><span class="linenos">338</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">[</span><span class="n">tk_obj_id</span><span class="p">]</span>
</span><span id="TkinterService.full_processing_iteration-339"><a href="#TkinterService.full_processing_iteration-339"><span class="linenos">339</span></a>        
</span><span id="TkinterService.full_processing_iteration-340"><a href="#TkinterService.full_processing_iteration-340"><span class="linenos">340</span></a>        <span class="c1"># compute min update period</span>
</span><span id="TkinterService.full_processing_iteration-341"><a href="#TkinterService.full_processing_iteration-341"><span class="linenos">341</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-342"><a href="#TkinterService.full_processing_iteration-342"><span class="linenos">342</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
</span><span id="TkinterService.full_processing_iteration-343"><a href="#TkinterService.full_processing_iteration-343"><span class="linenos">343</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TkinterService.full_processing_iteration-344"><a href="#TkinterService.full_processing_iteration-344"><span class="linenos">344</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">update_period</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_update_period</span>
</span><span id="TkinterService.full_processing_iteration-345"><a href="#TkinterService.full_processing_iteration-345"><span class="linenos">345</span></a>        
</span><span id="TkinterService.full_processing_iteration-346"><a href="#TkinterService.full_processing_iteration-346"><span class="linenos">346</span></a>        <span class="c1"># general</span>
</span><span id="TkinterService.full_processing_iteration-347"><a href="#TkinterService.full_processing_iteration-347"><span class="linenos">347</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">):</span>
</span><span id="TkinterService.full_processing_iteration-348"><a href="#TkinterService.full_processing_iteration-348"><span class="linenos">348</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TkinterService.in_work" class="classattr">
                                        <input id="TkinterService.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TkinterService.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TkinterService.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TkinterService.in_work-350"><a href="#TkinterService.in_work-350"><span class="linenos">350</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TkinterService.in_work-351"><a href="#TkinterService.in_work-351"><span class="linenos">351</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_closed</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_destroyed</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">update_periods</span><span class="p">)</span>
</span><span id="TkinterService.in_work-352"><a href="#TkinterService.in_work-352"><span class="linenos">352</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="TkinterService.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="TkinterService.iteration" class="function">iteration</dd>
                <dd id="TkinterService.make_response" class="function">make_response</dd>
                <dd id="TkinterService.register_response" class="function">register_response</dd>
                <dd id="TkinterService.put_task" class="function">put_task</dd>
                <dd id="TkinterService.resolve_request" class="function">resolve_request</dd>
                <dd id="TkinterService.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="TkinterService.in_forground_work" class="function">in_forground_work</dd>
                <dd id="TkinterService.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="TkinterService.time_left_before_next_event" class="function">time_left_before_next_event</dd>
                <dd id="TkinterService.is_low_latency" class="function">is_low_latency</dd>
                <dd id="TkinterService.make_live" class="function">make_live</dd>
                <dd id="TkinterService.make_dead" class="function">make_dead</dd>
                <dd id="TkinterService.service_id_impl" class="function">service_id_impl</dd>
                <dd id="TkinterService.service_id" class="function">service_id</dd>
                <dd id="TkinterService.destroy" class="function">destroy</dd>

            </div>
            <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="TkinterService.StatsLevel" class="class">StatsLevel</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="tk_updater">
                            <input id="tk_updater-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">tk_updater</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="n">tkinter_service</span><span class="p">:</span> <span class="n"><a href="#TkinterService">TkinterService</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tk_updater-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tk_updater"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tk_updater-591"><a href="#tk_updater-591"><span class="linenos">591</span></a><span class="k">def</span> <span class="nf">tk_updater</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">tkinter_service</span><span class="p">:</span> <span class="n">TkinterService</span><span class="p">):</span>
</span><span id="tk_updater-592"><a href="#tk_updater-592"><span class="linenos">592</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="tk_updater-593"><a href="#tk_updater-593"><span class="linenos">593</span></a><span class="sd">    https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app</span>
</span><span id="tk_updater-594"><a href="#tk_updater-594"><span class="linenos">594</span></a><span class="sd">    https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py</span>
</span><span id="tk_updater-595"><a href="#tk_updater-595"><span class="linenos">595</span></a>
</span><span id="tk_updater-596"><a href="#tk_updater-596"><span class="linenos">596</span></a><span class="sd">    Args:</span>
</span><span id="tk_updater-597"><a href="#tk_updater-597"><span class="linenos">597</span></a><span class="sd">        i (Interface): [description]</span>
</span><span id="tk_updater-598"><a href="#tk_updater-598"><span class="linenos">598</span></a><span class="sd">        tkinter_service (TkinterService): [description]</span>
</span><span id="tk_updater-599"><a href="#tk_updater-599"><span class="linenos">599</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="tk_updater-600"><a href="#tk_updater-600"><span class="linenos">600</span></a>    <span class="kn">from</span> <span class="nn">_tkinter</span> <span class="kn">import</span> <span class="n">ALL_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__ALL_EVENTS</span><span class="p">,</span> <span class="n">WINDOW_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__WINDOW_EVENTS</span><span class="p">,</span> <span class="n">FILE_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__FILE_EVENTS</span><span class="p">,</span> <span class="n">TIMER_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__TIMER_EVENTS</span><span class="p">,</span> <span class="n">IDLE_EVENTS</span> <span class="k">as</span> <span class="n">_tkinter__IDLE_EVENTS</span><span class="p">,</span> <span class="n">DONT_WAIT</span> <span class="k">as</span> <span class="n">_tkinter__DONT_WAIT</span>
</span><span id="tk_updater-601"><a href="#tk_updater-601"><span class="linenos">601</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.sleep</span> <span class="kn">import</span> <span class="n">Sleep</span>
</span><span id="tk_updater-602"><a href="#tk_updater-602"><span class="linenos">602</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">get_loop_yield</span>
</span><span id="tk_updater-603"><a href="#tk_updater-603"><span class="linenos">603</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">get_loop_yield</span><span class="p">(</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">)</span>
</span><span id="tk_updater-604"><a href="#tk_updater-604"><span class="linenos">604</span></a>    <span class="k">while</span> <span class="n">tkinter_service</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">:</span>
</span><span id="tk_updater-605"><a href="#tk_updater-605"><span class="linenos">605</span></a>        <span class="n">ly</span><span class="p">()</span>
</span><span id="tk_updater-606"><a href="#tk_updater-606"><span class="linenos">606</span></a>        <span class="n">tk_by_id_bak</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="n">tkinter_service</span><span class="o">.</span><span class="n">tk_by_id</span><span class="p">)</span>
</span><span id="tk_updater-607"><a href="#tk_updater-607"><span class="linenos">607</span></a>        <span class="n">desired_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tk_by_id_bak</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="tk_updater-608"><a href="#tk_updater-608"><span class="linenos">608</span></a>        <span class="n">tk_ids_without_events</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="tk_updater-609"><a href="#tk_updater-609"><span class="linenos">609</span></a>        
</span><span id="tk_updater-610"><a href="#tk_updater-610"><span class="linenos">610</span></a>        <span class="k">while</span> <span class="nb">len</span><span class="p">(</span><span class="n">tk_ids_without_events</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">desired_length</span><span class="p">:</span>
</span><span id="tk_updater-611"><a href="#tk_updater-611"><span class="linenos">611</span></a>            <span class="k">for</span> <span class="n">tk_id</span><span class="p">,</span> <span class="n">tk_obj</span> <span class="ow">in</span> <span class="n">tk_by_id_bak</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="tk_updater-612"><a href="#tk_updater-612"><span class="linenos">612</span></a>                <span class="k">if</span> <span class="n">tk_id</span> <span class="ow">in</span> <span class="n">tk_ids_without_events</span><span class="p">:</span>
</span><span id="tk_updater-613"><a href="#tk_updater-613"><span class="linenos">613</span></a>                    <span class="k">continue</span>
</span><span id="tk_updater-614"><a href="#tk_updater-614"><span class="linenos">614</span></a>                
</span><span id="tk_updater-615"><a href="#tk_updater-615"><span class="linenos">615</span></a>                <span class="k">if</span> <span class="n">tk_id</span> <span class="ow">in</span> <span class="n">tkinter_service</span><span class="o">.</span><span class="n">destroyed</span><span class="p">:</span>
</span><span id="tk_updater-616"><a href="#tk_updater-616"><span class="linenos">616</span></a>                    <span class="n">tk_ids_without_events</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="tk_updater-617"><a href="#tk_updater-617"><span class="linenos">617</span></a>                    <span class="k">continue</span>
</span><span id="tk_updater-618"><a href="#tk_updater-618"><span class="linenos">618</span></a>                
</span><span id="tk_updater-619"><a href="#tk_updater-619"><span class="linenos">619</span></a>                <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-620"><a href="#tk_updater-620"><span class="linenos">620</span></a>                <span class="n">has_window_events</span> <span class="o">=</span> <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__WINDOW_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="tk_updater-621"><a href="#tk_updater-621"><span class="linenos">621</span></a>                <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-622"><a href="#tk_updater-622"><span class="linenos">622</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="tk_updater-623"><a href="#tk_updater-623"><span class="linenos">623</span></a>                    <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="tk_updater-624"><a href="#tk_updater-624"><span class="linenos">624</span></a>                <span class="c1"># ly()</span>
</span><span id="tk_updater-625"><a href="#tk_updater-625"><span class="linenos">625</span></a>                
</span><span id="tk_updater-626"><a href="#tk_updater-626"><span class="linenos">626</span></a>                <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-627"><a href="#tk_updater-627"><span class="linenos">627</span></a>                <span class="n">has_file_events</span> <span class="o">=</span> <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__FILE_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="tk_updater-628"><a href="#tk_updater-628"><span class="linenos">628</span></a>                <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-629"><a href="#tk_updater-629"><span class="linenos">629</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="tk_updater-630"><a href="#tk_updater-630"><span class="linenos">630</span></a>                    <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="tk_updater-631"><a href="#tk_updater-631"><span class="linenos">631</span></a>                <span class="c1"># ly()</span>
</span><span id="tk_updater-632"><a href="#tk_updater-632"><span class="linenos">632</span></a>                
</span><span id="tk_updater-633"><a href="#tk_updater-633"><span class="linenos">633</span></a>                <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-634"><a href="#tk_updater-634"><span class="linenos">634</span></a>                <span class="n">has_timer_events</span> <span class="o">=</span> <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__TIMER_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="tk_updater-635"><a href="#tk_updater-635"><span class="linenos">635</span></a>                <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-636"><a href="#tk_updater-636"><span class="linenos">636</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="tk_updater-637"><a href="#tk_updater-637"><span class="linenos">637</span></a>                    <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="tk_updater-638"><a href="#tk_updater-638"><span class="linenos">638</span></a>                <span class="c1"># ly()</span>
</span><span id="tk_updater-639"><a href="#tk_updater-639"><span class="linenos">639</span></a>                
</span><span id="tk_updater-640"><a href="#tk_updater-640"><span class="linenos">640</span></a>                <span class="n">has_events</span> <span class="o">=</span> <span class="n">has_window_events</span> <span class="ow">or</span> <span class="n">has_file_events</span> <span class="ow">or</span> <span class="n">has_timer_events</span>
</span><span id="tk_updater-641"><a href="#tk_updater-641"><span class="linenos">641</span></a>                
</span><span id="tk_updater-642"><a href="#tk_updater-642"><span class="linenos">642</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">has_events</span><span class="p">:</span>
</span><span id="tk_updater-643"><a href="#tk_updater-643"><span class="linenos">643</span></a>                    <span class="n">start</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-644"><a href="#tk_updater-644"><span class="linenos">644</span></a>                    <span class="n">tk_obj</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">(</span><span class="n">_tkinter__IDLE_EVENTS</span> <span class="o">|</span> <span class="n">_tkinter__DONT_WAIT</span><span class="p">)</span>
</span><span id="tk_updater-645"><a href="#tk_updater-645"><span class="linenos">645</span></a>                    <span class="n">stop</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tk_updater-646"><a href="#tk_updater-646"><span class="linenos">646</span></a>                    <span class="k">if</span> <span class="p">(</span><span class="n">stop</span> <span class="o">-</span> <span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.001</span><span class="p">:</span>
</span><span id="tk_updater-647"><a href="#tk_updater-647"><span class="linenos">647</span></a>                        <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="tk_updater-648"><a href="#tk_updater-648"><span class="linenos">648</span></a>                    <span class="c1"># ly()</span>
</span><span id="tk_updater-649"><a href="#tk_updater-649"><span class="linenos">649</span></a>                    <span class="n">tk_ids_without_events</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tk_id</span><span class="p">)</span>
</span><span id="tk_updater-650"><a href="#tk_updater-650"><span class="linenos">650</span></a>
</span><span id="tk_updater-651"><a href="#tk_updater-651"><span class="linenos">651</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="n">tkinter_service</span><span class="o">.</span><span class="n">update_period</span><span class="p">)</span>
</span><span id="tk_updater-652"><a href="#tk_updater-652"><span class="linenos">652</span></a>    
</span><span id="tk_updater-653"><a href="#tk_updater-653"><span class="linenos">653</span></a>    <span class="n">tkinter_service</span><span class="o">.</span><span class="n">updater_running</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


            <div class="docstring"><p><a href="https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app">https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app</a>
<a href="https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py">https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py</a></p>

<p>Args:
    i (Interface): [description]
    tkinter_service (TkinterService): [description]</p>
</div>


                </section>
                <section id="after_func">
                            <input id="after_func-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">after_func</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">root</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="after_func-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#after_func"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="after_func-656"><a href="#after_func-656"><span class="linenos">656</span></a><span class="k">def</span> <span class="nf">after_func</span><span class="p">(</span><span class="n">root</span><span class="p">):</span>
</span><span id="after_func-657"><a href="#after_func-657"><span class="linenos">657</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.simple_yield</span> <span class="kn">import</span> <span class="n">Yield</span>
</span><span id="after_func-658"><a href="#after_func-658"><span class="linenos">658</span></a>    <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="n">current_interface</span><span class="p">,</span> <span class="n">OutsideCoroSchedulerContext</span>
</span><span id="after_func-659"><a href="#after_func-659"><span class="linenos">659</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="after_func-660"><a href="#after_func-660"><span class="linenos">660</span></a>        <span class="n">i</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="after_func-661"><a href="#after_func-661"><span class="linenos">661</span></a>        <span class="k">if</span> <span class="n">i</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="after_func-662"><a href="#after_func-662"><span class="linenos">662</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="after_func-663"><a href="#after_func-663"><span class="linenos">663</span></a>    <span class="k">except</span> <span class="n">OutsideCoroSchedulerContext</span><span class="p">:</span>
</span><span id="after_func-664"><a href="#after_func-664"><span class="linenos">664</span></a>        <span class="k">pass</span>
</span><span id="after_func-665"><a href="#after_func-665"><span class="linenos">665</span></a>    
</span><span id="after_func-666"><a href="#after_func-666"><span class="linenos">666</span></a>    <span class="c1"># after_setup(root, 1)</span>
</span><span id="after_func-667"><a href="#after_func-667"><span class="linenos">667</span></a>    <span class="n">after_idle_setup</span><span class="p">(</span><span class="n">root</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="after_setup">
                            <input id="after_setup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">after_setup</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">root</span>, </span><span class="param"><span class="n">update_period</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="after_setup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#after_setup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="after_setup-670"><a href="#after_setup-670"><span class="linenos">670</span></a><span class="k">def</span> <span class="nf">after_setup</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">update_period</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="after_setup-671"><a href="#after_setup-671"><span class="linenos">671</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="after_setup-672"><a href="#after_setup-672"><span class="linenos">672</span></a>        <span class="n">handler</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">after</span><span class="p">(</span><span class="n">update_period</span><span class="p">,</span> <span class="n">after_func</span><span class="p">,</span> <span class="n">root</span><span class="p">)</span>
</span><span id="after_setup-673"><a href="#after_setup-673"><span class="linenos">673</span></a>    <span class="k">except</span> <span class="n">TclError</span><span class="p">:</span>
</span><span id="after_setup-674"><a href="#after_setup-674"><span class="linenos">674</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="after_setup-675"><a href="#after_setup-675"><span class="linenos">675</span></a>
</span><span id="after_setup-676"><a href="#after_setup-676"><span class="linenos">676</span></a>    <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                </section>
                <section id="after_idle_setup">
                            <input id="after_idle_setup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">after_idle_setup</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">root</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="after_idle_setup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#after_idle_setup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="after_idle_setup-679"><a href="#after_idle_setup-679"><span class="linenos">679</span></a><span class="k">def</span> <span class="nf">after_idle_setup</span><span class="p">(</span><span class="n">root</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="after_idle_setup-680"><a href="#after_idle_setup-680"><span class="linenos">680</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="after_idle_setup-681"><a href="#after_idle_setup-681"><span class="linenos">681</span></a>        <span class="n">handler</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">after_idle</span><span class="p">(</span><span class="n">after_setup</span><span class="p">,</span> <span class="n">root</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="after_idle_setup-682"><a href="#after_idle_setup-682"><span class="linenos">682</span></a>    <span class="k">except</span> <span class="n">TclError</span><span class="p">:</span>
</span><span id="after_idle_setup-683"><a href="#after_idle_setup-683"><span class="linenos">683</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="after_idle_setup-684"><a href="#after_idle_setup-684"><span class="linenos">684</span></a>
</span><span id="after_idle_setup-685"><a href="#after_idle_setup-685"><span class="linenos">685</span></a>    <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>