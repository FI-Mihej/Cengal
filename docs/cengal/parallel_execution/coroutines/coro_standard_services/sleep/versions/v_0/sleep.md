---
title: sleep
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.sleep<wbr>.versions<wbr>.v_0<wbr>.sleep    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-sleep-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-sleep-view-source"><span>View Source</span></label>

                        <div class="pdoc-code codehilite"><pre><span></span><span id="L-1"><a href="#L-1"><span class="linenos"> 1</span></a><span class="ch">#!/usr/bin/env python</span>
</span><span id="L-2"><a href="#L-2"><span class="linenos"> 2</span></a><span class="c1"># coding=utf-8</span>
</span><span id="L-3"><a href="#L-3"><span class="linenos"> 3</span></a>
</span><span id="L-4"><a href="#L-4"><span class="linenos"> 4</span></a><span class="c1"># Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;</span>
</span><span id="L-5"><a href="#L-5"><span class="linenos"> 5</span></a><span class="c1"># </span>
</span><span id="L-6"><a href="#L-6"><span class="linenos"> 6</span></a><span class="c1"># Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span>
</span><span id="L-7"><a href="#L-7"><span class="linenos"> 7</span></a><span class="c1"># you may not use this file except in compliance with the License.</span>
</span><span id="L-8"><a href="#L-8"><span class="linenos"> 8</span></a><span class="c1"># You may obtain a copy of the License at</span>
</span><span id="L-9"><a href="#L-9"><span class="linenos"> 9</span></a><span class="c1"># </span>
</span><span id="L-10"><a href="#L-10"><span class="linenos">10</span></a><span class="c1">#     http://www.apache.org/licenses/LICENSE-2.0</span>
</span><span id="L-11"><a href="#L-11"><span class="linenos">11</span></a><span class="c1"># </span>
</span><span id="L-12"><a href="#L-12"><span class="linenos">12</span></a><span class="c1"># Unless required by applicable law or agreed to in writing, software</span>
</span><span id="L-13"><a href="#L-13"><span class="linenos">13</span></a><span class="c1"># distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span>
</span><span id="L-14"><a href="#L-14"><span class="linenos">14</span></a><span class="c1"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span>
</span><span id="L-15"><a href="#L-15"><span class="linenos">15</span></a><span class="c1"># See the License for the specific language governing permissions and</span>
</span><span id="L-16"><a href="#L-16"><span class="linenos">16</span></a><span class="c1"># limitations under the License.</span>
</span><span id="L-17"><a href="#L-17"><span class="linenos">17</span></a>
</span><span id="L-18"><a href="#L-18"><span class="linenos">18</span></a>
</span><span id="L-19"><a href="#L-19"><span class="linenos">19</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos">20</span></a><span class="sd">Module Docstring</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos">21</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos">22</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos">23</span></a>
</span><span id="L-24"><a href="#L-24"><span class="linenos">24</span></a>
</span><span id="L-25"><a href="#L-25"><span class="linenos">25</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos">26</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos">27</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos">28</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos">29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos">30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos">31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos">32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos">33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos">34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos">35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos">36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos">37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Sleep&#39;</span><span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos">38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos">39</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos">40</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.cpu_clock_cycles</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos">41</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.timer</span> <span class="kn">import</span> <span class="n">Timer</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos">42</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos">43</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos">44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos">45</span></a>
</span><span id="L-46"><a href="#L-46"><span class="linenos">46</span></a><span class="k">class</span> <span class="nc">Sleep</span><span class="p">(</span><span class="n">TypedService</span><span class="p">[</span><span class="nb">float</span><span class="p">]):</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos">47</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos">48</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos">49</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span> <span class="o">=</span> <span class="n">Timer</span><span class="p">()</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos">50</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos">51</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos">52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos">53</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos">54</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos">55</span></a>        <span class="k">def</span> <span class="nf">timer_handler_func</span><span class="p">(</span><span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">start_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos">56</span></a>            <span class="n">current_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos">57</span></a>            <span class="k">if</span> <span class="n">start_time</span> <span class="o">&gt;</span> <span class="n">current_time</span><span class="p">:</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos">58</span></a>                <span class="n">start_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos">59</span></a>            <span class="n">real_delay</span> <span class="o">=</span> <span class="n">current_time</span> <span class="o">-</span> <span class="n">start_time</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos">60</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos">61</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">real_delay</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos">62</span></a>
</span><span id="L-63"><a href="#L-63"><span class="linenos">63</span></a>        <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">is_background_coro</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos">64</span></a>        <span class="n">handler</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">timer_handler_func</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">foreground</span><span class="p">,</span> <span class="n">perf_counter</span><span class="p">())</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos">65</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_added</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos">66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">handler</span><span class="p">,</span> <span class="n">delay</span><span class="p">)</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos">67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos">68</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos">69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos">70</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos">71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="p">()</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos">72</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span><span class="p">:</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos">73</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos">74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos">75</span></a>    <span class="k">def</span> <span class="nf">task_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos">76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos">77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos">78</span></a>
</span><span id="L-79"><a href="#L-79"><span class="linenos">79</span></a>    <span class="k">def</span> <span class="nf">task_triggered</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos">80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos">81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos">82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos">83</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos">84</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos">85</span></a>    
</span><span id="L-86"><a href="#L-86"><span class="linenos">86</span></a>    <span class="k">def</span> <span class="nf">in_forground_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos">87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos">88</span></a>    
</span><span id="L-89"><a href="#L-89"><span class="linenos">89</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos">90</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">nearest_event</span><span class="p">()</span>
</span></pre></div>


            </section>
                <section id="Sleep">
                            <input id="Sleep-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Sleep</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.TypedService[float]</span>):

                <label class="view-source-button" for="Sleep-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep-47"><a href="#Sleep-47"><span class="linenos">47</span></a><span class="k">class</span> <span class="nc">Sleep</span><span class="p">(</span><span class="n">TypedService</span><span class="p">[</span><span class="nb">float</span><span class="p">]):</span>
</span><span id="Sleep-48"><a href="#Sleep-48"><span class="linenos">48</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Sleep-49"><a href="#Sleep-49"><span class="linenos">49</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="Sleep-50"><a href="#Sleep-50"><span class="linenos">50</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span> <span class="o">=</span> <span class="n">Timer</span><span class="p">()</span>
</span><span id="Sleep-51"><a href="#Sleep-51"><span class="linenos">51</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Sleep-52"><a href="#Sleep-52"><span class="linenos">52</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Sleep-53"><a href="#Sleep-53"><span class="linenos">53</span></a>
</span><span id="Sleep-54"><a href="#Sleep-54"><span class="linenos">54</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Sleep-55"><a href="#Sleep-55"><span class="linenos">55</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="Sleep-56"><a href="#Sleep-56"><span class="linenos">56</span></a>        <span class="k">def</span> <span class="nf">timer_handler_func</span><span class="p">(</span><span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">start_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="Sleep-57"><a href="#Sleep-57"><span class="linenos">57</span></a>            <span class="n">current_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Sleep-58"><a href="#Sleep-58"><span class="linenos">58</span></a>            <span class="k">if</span> <span class="n">start_time</span> <span class="o">&gt;</span> <span class="n">current_time</span><span class="p">:</span>
</span><span id="Sleep-59"><a href="#Sleep-59"><span class="linenos">59</span></a>                <span class="n">start_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="Sleep-60"><a href="#Sleep-60"><span class="linenos">60</span></a>            <span class="n">real_delay</span> <span class="o">=</span> <span class="n">current_time</span> <span class="o">-</span> <span class="n">start_time</span>
</span><span id="Sleep-61"><a href="#Sleep-61"><span class="linenos">61</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="Sleep-62"><a href="#Sleep-62"><span class="linenos">62</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">real_delay</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Sleep-63"><a href="#Sleep-63"><span class="linenos">63</span></a>
</span><span id="Sleep-64"><a href="#Sleep-64"><span class="linenos">64</span></a>        <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">is_background_coro</span>
</span><span id="Sleep-65"><a href="#Sleep-65"><span class="linenos">65</span></a>        <span class="n">handler</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">timer_handler_func</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">foreground</span><span class="p">,</span> <span class="n">perf_counter</span><span class="p">())</span>
</span><span id="Sleep-66"><a href="#Sleep-66"><span class="linenos">66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_added</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="Sleep-67"><a href="#Sleep-67"><span class="linenos">67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">handler</span><span class="p">,</span> <span class="n">delay</span><span class="p">)</span>
</span><span id="Sleep-68"><a href="#Sleep-68"><span class="linenos">68</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Sleep-69"><a href="#Sleep-69"><span class="linenos">69</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Sleep-70"><a href="#Sleep-70"><span class="linenos">70</span></a>
</span><span id="Sleep-71"><a href="#Sleep-71"><span class="linenos">71</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Sleep-72"><a href="#Sleep-72"><span class="linenos">72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="p">()</span>
</span><span id="Sleep-73"><a href="#Sleep-73"><span class="linenos">73</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span><span class="p">:</span>
</span><span id="Sleep-74"><a href="#Sleep-74"><span class="linenos">74</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="Sleep-75"><a href="#Sleep-75"><span class="linenos">75</span></a>
</span><span id="Sleep-76"><a href="#Sleep-76"><span class="linenos">76</span></a>    <span class="k">def</span> <span class="nf">task_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Sleep-77"><a href="#Sleep-77"><span class="linenos">77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Sleep-78"><a href="#Sleep-78"><span class="linenos">78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="Sleep-79"><a href="#Sleep-79"><span class="linenos">79</span></a>
</span><span id="Sleep-80"><a href="#Sleep-80"><span class="linenos">80</span></a>    <span class="k">def</span> <span class="nf">task_triggered</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Sleep-81"><a href="#Sleep-81"><span class="linenos">81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="Sleep-82"><a href="#Sleep-82"><span class="linenos">82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="Sleep-83"><a href="#Sleep-83"><span class="linenos">83</span></a>
</span><span id="Sleep-84"><a href="#Sleep-84"><span class="linenos">84</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Sleep-85"><a href="#Sleep-85"><span class="linenos">85</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="Sleep-86"><a href="#Sleep-86"><span class="linenos">86</span></a>    
</span><span id="Sleep-87"><a href="#Sleep-87"><span class="linenos">87</span></a>    <span class="k">def</span> <span class="nf">in_forground_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Sleep-88"><a href="#Sleep-88"><span class="linenos">88</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span>
</span><span id="Sleep-89"><a href="#Sleep-89"><span class="linenos">89</span></a>    
</span><span id="Sleep-90"><a href="#Sleep-90"><span class="linenos">90</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="Sleep-91"><a href="#Sleep-91"><span class="linenos">91</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">nearest_event</span><span class="p">()</span>
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


                            <div id="Sleep.__init__" class="classattr">
                                        <input id="Sleep.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Sleep</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="Sleep.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.__init__-48"><a href="#Sleep.__init__-48"><span class="linenos">48</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Sleep.__init__-49"><a href="#Sleep.__init__-49"><span class="linenos">49</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="Sleep.__init__-50"><a href="#Sleep.__init__-50"><span class="linenos">50</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span> <span class="o">=</span> <span class="n">Timer</span><span class="p">()</span>
</span><span id="Sleep.__init__-51"><a href="#Sleep.__init__-51"><span class="linenos">51</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Sleep.__init__-52"><a href="#Sleep.__init__-52"><span class="linenos">52</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">=</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="Sleep.timer" class="classattr">
                                <div class="attr variable">
            <span class="name">timer</span>

        
    </div>
    <a class="headerlink" href="#Sleep.timer"></a>
    
    

                            </div>
                            <div id="Sleep.pending_tasks_number" class="classattr">
                                <div class="attr variable">
            <span class="name">pending_tasks_number</span>

        
    </div>
    <a class="headerlink" href="#Sleep.pending_tasks_number"></a>
    
    

                            </div>
                            <div id="Sleep.pending_foreground_tasks_number" class="classattr">
                                <div class="attr variable">
            <span class="name">pending_foreground_tasks_number</span>

        
    </div>
    <a class="headerlink" href="#Sleep.pending_foreground_tasks_number"></a>
    
    

                            </div>
                            <div id="Sleep.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="Sleep.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">delay</span><span class="p">:</span> <span class="nb">float</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="Sleep.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.single_task_registration_or_immediate_processing-54"><a href="#Sleep.single_task_registration_or_immediate_processing-54"><span class="linenos">54</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-55"><a href="#Sleep.single_task_registration_or_immediate_processing-55"><span class="linenos">55</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-56"><a href="#Sleep.single_task_registration_or_immediate_processing-56"><span class="linenos">56</span></a>        <span class="k">def</span> <span class="nf">timer_handler_func</span><span class="p">(</span><span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">start_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-57"><a href="#Sleep.single_task_registration_or_immediate_processing-57"><span class="linenos">57</span></a>            <span class="n">current_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-58"><a href="#Sleep.single_task_registration_or_immediate_processing-58"><span class="linenos">58</span></a>            <span class="k">if</span> <span class="n">start_time</span> <span class="o">&gt;</span> <span class="n">current_time</span><span class="p">:</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-59"><a href="#Sleep.single_task_registration_or_immediate_processing-59"><span class="linenos">59</span></a>                <span class="n">start_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-60"><a href="#Sleep.single_task_registration_or_immediate_processing-60"><span class="linenos">60</span></a>            <span class="n">real_delay</span> <span class="o">=</span> <span class="n">current_time</span> <span class="o">-</span> <span class="n">start_time</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-61"><a href="#Sleep.single_task_registration_or_immediate_processing-61"><span class="linenos">61</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">task_triggered</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-62"><a href="#Sleep.single_task_registration_or_immediate_processing-62"><span class="linenos">62</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">real_delay</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-63"><a href="#Sleep.single_task_registration_or_immediate_processing-63"><span class="linenos">63</span></a>
</span><span id="Sleep.single_task_registration_or_immediate_processing-64"><a href="#Sleep.single_task_registration_or_immediate_processing-64"><span class="linenos">64</span></a>        <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">is_background_coro</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-65"><a href="#Sleep.single_task_registration_or_immediate_processing-65"><span class="linenos">65</span></a>        <span class="n">handler</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">timer_handler_func</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">foreground</span><span class="p">,</span> <span class="n">perf_counter</span><span class="p">())</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-66"><a href="#Sleep.single_task_registration_or_immediate_processing-66"><span class="linenos">66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_added</span><span class="p">(</span><span class="n">foreground</span><span class="p">)</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-67"><a href="#Sleep.single_task_registration_or_immediate_processing-67"><span class="linenos">67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">handler</span><span class="p">,</span> <span class="n">delay</span><span class="p">)</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-68"><a href="#Sleep.single_task_registration_or_immediate_processing-68"><span class="linenos">68</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Sleep.single_task_registration_or_immediate_processing-69"><a href="#Sleep.single_task_registration_or_immediate_processing-69"><span class="linenos">69</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="Sleep.full_processing_iteration" class="classattr">
                                        <input id="Sleep.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Sleep.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.full_processing_iteration-71"><a href="#Sleep.full_processing_iteration-71"><span class="linenos">71</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Sleep.full_processing_iteration-72"><a href="#Sleep.full_processing_iteration-72"><span class="linenos">72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="p">()</span>
</span><span id="Sleep.full_processing_iteration-73"><a href="#Sleep.full_processing_iteration-73"><span class="linenos">73</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span><span class="p">:</span>
</span><span id="Sleep.full_processing_iteration-74"><a href="#Sleep.full_processing_iteration-74"><span class="linenos">74</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="Sleep.task_added" class="classattr">
                                        <input id="Sleep.task_added-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">task_added</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Sleep.task_added-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.task_added"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.task_added-76"><a href="#Sleep.task_added-76"><span class="linenos">76</span></a>    <span class="k">def</span> <span class="nf">task_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Sleep.task_added-77"><a href="#Sleep.task_added-77"><span class="linenos">77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Sleep.task_added-78"><a href="#Sleep.task_added-78"><span class="linenos">78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">+=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="Sleep.task_triggered" class="classattr">
                                        <input id="Sleep.task_triggered-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">task_triggered</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Sleep.task_triggered-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.task_triggered"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.task_triggered-80"><a href="#Sleep.task_triggered-80"><span class="linenos">80</span></a>    <span class="k">def</span> <span class="nf">task_triggered</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">foreground</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Sleep.task_triggered-81"><a href="#Sleep.task_triggered-81"><span class="linenos">81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="Sleep.task_triggered-82"><a href="#Sleep.task_triggered-82"><span class="linenos">82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span> <span class="o">-=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">foreground</span> <span class="k">else</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="Sleep.in_work" class="classattr">
                                        <input id="Sleep.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="Sleep.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.in_work-84"><a href="#Sleep.in_work-84"><span class="linenos">84</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Sleep.in_work-85"><a href="#Sleep.in_work-85"><span class="linenos">85</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="Sleep.in_forground_work" class="classattr">
                                        <input id="Sleep.in_forground_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_forground_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="Sleep.in_forground_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.in_forground_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.in_forground_work-87"><a href="#Sleep.in_forground_work-87"><span class="linenos">87</span></a>    <span class="k">def</span> <span class="nf">in_forground_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Sleep.in_forground_work-88"><a href="#Sleep.in_forground_work-88"><span class="linenos">88</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_foreground_tasks_number</span>
</span></pre></div>


    

                            </div>
                            <div id="Sleep.time_left_before_next_event" class="classattr">
                                        <input id="Sleep.time_left_before_next_event-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">time_left_before_next_event</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="Sleep.time_left_before_next_event-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Sleep.time_left_before_next_event"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Sleep.time_left_before_next_event-90"><a href="#Sleep.time_left_before_next_event-90"><span class="linenos">90</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="Sleep.time_left_before_next_event-91"><a href="#Sleep.time_left_before_next_event-91"><span class="linenos">91</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_tasks_number</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">nearest_event</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="Sleep.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="Sleep.iteration" class="function">iteration</dd>
                <dd id="Sleep.make_response" class="function">make_response</dd>
                <dd id="Sleep.register_response" class="function">register_response</dd>
                <dd id="Sleep.put_task" class="function">put_task</dd>
                <dd id="Sleep.resolve_request" class="function">resolve_request</dd>
                <dd id="Sleep.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="Sleep.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="Sleep.is_low_latency" class="function">is_low_latency</dd>
                <dd id="Sleep.make_live" class="function">make_live</dd>
                <dd id="Sleep.make_dead" class="function">make_dead</dd>
                <dd id="Sleep.service_id_impl" class="function">service_id_impl</dd>
                <dd id="Sleep.service_id" class="function">service_id</dd>
                <dd id="Sleep.destroy" class="function">destroy</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>