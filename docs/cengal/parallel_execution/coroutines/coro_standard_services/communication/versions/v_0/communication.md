---
title: communication
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.communication<wbr>.versions<wbr>.v_0<wbr>.communication    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-communication-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-communication-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.4&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Communication&#39;</span><span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">NoReturn</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Any</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="k">class</span> <span class="nc">Communication</span><span class="p">(</span><span class="n">Service</span><span class="p">):</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>    <span class="k">class</span> <span class="nc">Requests</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>        <span class="n">send_async</span> <span class="o">=</span> <span class="mi">0</span>        <span class="c1"># Coro will get control immediately after message sent</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>        <span class="n">send_sync</span> <span class="o">=</span> <span class="mi">1</span>         <span class="c1"># Coro will get control only after response will be received</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>        <span class="n">read_async</span> <span class="o">=</span> <span class="mi">2</span>        <span class="c1"># Coro will get control immediately even if input queue is empty</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>        <span class="n">read_sync</span> <span class="o">=</span> <span class="mi">3</span>         <span class="c1"># Coro will get control only if input queue is not empty or when new response will be</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>        <span class="c1"># received</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>        <span class="n">named_send_async</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># Coro will get control immediately after message sent</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>        <span class="n">named_send_sync</span> <span class="o">=</span> <span class="mi">5</span>   <span class="c1"># Coro will get control only after response will be received</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>        <span class="n">named_read_async</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># Coro will get control immediately even if input queue is empty</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="n">named_read_sync</span> <span class="o">=</span> <span class="mi">7</span>   <span class="c1"># Coro will get control only if input queue is not empty or when new response will be</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="c1"># received</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="k">class</span> <span class="nc">Request</span><span class="p">:</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_type</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># type: Optional[int]</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="kc">None</span>          <span class="c1"># type: Optional[Tuple]</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="kc">None</span>        <span class="c1"># type: Optional[Dict]</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="k">def</span> <span class="nf">send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="k">def</span> <span class="nf">send_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="k">def</span> <span class="nf">read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>        <span class="k">def</span> <span class="nf">read_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="k">def</span> <span class="nf">send_async_named</span><span class="p">(</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="k">def</span> <span class="nf">send_blocking_named</span><span class="p">(</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="k">def</span> <span class="nf">read_async_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="k">def</span> <span class="nf">read_blocking_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="k">def</span> <span class="nf">_save</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__request__type__</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_type</span> <span class="o">=</span> <span class="n">__request__type__</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Communication</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="s1">&#39;Communication.Requests&#39;</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_send_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_send_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_read_async</span><span class="p">()</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_read_sync</span><span class="p">()</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="k">elif</span> <span class="mi">4</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_send_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="k">elif</span> <span class="mi">5</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_send_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">elif</span> <span class="mi">6</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_named_read_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="k">elif</span> <span class="mi">7</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_read_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    <span class="k">def</span> <span class="nf">request_send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">request_send_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">request_read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a><span class="sd">        Will return tuple with sender coro ID and message</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a><span class="sd">        :rtype: Tuple[CoroID, Any]</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">request_read_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">request_named_send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">request_named_send_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">request_named_read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a><span class="sd">        Will return tuple with sender ID and message</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="sd">        :rtype: Tuple[Hashable, Any]</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>    <span class="k">def</span> <span class="nf">request_named_read_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="k">pass</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="Communication">
                            <input id="Communication-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Communication</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</span>):

                <label class="view-source-button" for="Communication-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication-45"><a href="#Communication-45"><span class="linenos"> 45</span></a><span class="k">class</span> <span class="nc">Communication</span><span class="p">(</span><span class="n">Service</span><span class="p">):</span>
</span><span id="Communication-46"><a href="#Communication-46"><span class="linenos"> 46</span></a>
</span><span id="Communication-47"><a href="#Communication-47"><span class="linenos"> 47</span></a>    <span class="k">class</span> <span class="nc">Requests</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="Communication-48"><a href="#Communication-48"><span class="linenos"> 48</span></a>        <span class="n">send_async</span> <span class="o">=</span> <span class="mi">0</span>        <span class="c1"># Coro will get control immediately after message sent</span>
</span><span id="Communication-49"><a href="#Communication-49"><span class="linenos"> 49</span></a>        <span class="n">send_sync</span> <span class="o">=</span> <span class="mi">1</span>         <span class="c1"># Coro will get control only after response will be received</span>
</span><span id="Communication-50"><a href="#Communication-50"><span class="linenos"> 50</span></a>        <span class="n">read_async</span> <span class="o">=</span> <span class="mi">2</span>        <span class="c1"># Coro will get control immediately even if input queue is empty</span>
</span><span id="Communication-51"><a href="#Communication-51"><span class="linenos"> 51</span></a>        <span class="n">read_sync</span> <span class="o">=</span> <span class="mi">3</span>         <span class="c1"># Coro will get control only if input queue is not empty or when new response will be</span>
</span><span id="Communication-52"><a href="#Communication-52"><span class="linenos"> 52</span></a>        <span class="c1"># received</span>
</span><span id="Communication-53"><a href="#Communication-53"><span class="linenos"> 53</span></a>        <span class="n">named_send_async</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># Coro will get control immediately after message sent</span>
</span><span id="Communication-54"><a href="#Communication-54"><span class="linenos"> 54</span></a>        <span class="n">named_send_sync</span> <span class="o">=</span> <span class="mi">5</span>   <span class="c1"># Coro will get control only after response will be received</span>
</span><span id="Communication-55"><a href="#Communication-55"><span class="linenos"> 55</span></a>        <span class="n">named_read_async</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># Coro will get control immediately even if input queue is empty</span>
</span><span id="Communication-56"><a href="#Communication-56"><span class="linenos"> 56</span></a>        <span class="n">named_read_sync</span> <span class="o">=</span> <span class="mi">7</span>   <span class="c1"># Coro will get control only if input queue is not empty or when new response will be</span>
</span><span id="Communication-57"><a href="#Communication-57"><span class="linenos"> 57</span></a>        <span class="c1"># received</span>
</span><span id="Communication-58"><a href="#Communication-58"><span class="linenos"> 58</span></a>
</span><span id="Communication-59"><a href="#Communication-59"><span class="linenos"> 59</span></a>    <span class="k">class</span> <span class="nc">Request</span><span class="p">:</span>
</span><span id="Communication-60"><a href="#Communication-60"><span class="linenos"> 60</span></a>        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Communication-61"><a href="#Communication-61"><span class="linenos"> 61</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_type</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># type: Optional[int]</span>
</span><span id="Communication-62"><a href="#Communication-62"><span class="linenos"> 62</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="kc">None</span>          <span class="c1"># type: Optional[Tuple]</span>
</span><span id="Communication-63"><a href="#Communication-63"><span class="linenos"> 63</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="kc">None</span>        <span class="c1"># type: Optional[Dict]</span>
</span><span id="Communication-64"><a href="#Communication-64"><span class="linenos"> 64</span></a>
</span><span id="Communication-65"><a href="#Communication-65"><span class="linenos"> 65</span></a>        <span class="k">def</span> <span class="nf">send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-66"><a href="#Communication-66"><span class="linenos"> 66</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication-67"><a href="#Communication-67"><span class="linenos"> 67</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-68"><a href="#Communication-68"><span class="linenos"> 68</span></a>
</span><span id="Communication-69"><a href="#Communication-69"><span class="linenos"> 69</span></a>        <span class="k">def</span> <span class="nf">send_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-70"><a href="#Communication-70"><span class="linenos"> 70</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication-71"><a href="#Communication-71"><span class="linenos"> 71</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-72"><a href="#Communication-72"><span class="linenos"> 72</span></a>
</span><span id="Communication-73"><a href="#Communication-73"><span class="linenos"> 73</span></a>        <span class="k">def</span> <span class="nf">read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-74"><a href="#Communication-74"><span class="linenos"> 74</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="Communication-75"><a href="#Communication-75"><span class="linenos"> 75</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-76"><a href="#Communication-76"><span class="linenos"> 76</span></a>
</span><span id="Communication-77"><a href="#Communication-77"><span class="linenos"> 77</span></a>        <span class="k">def</span> <span class="nf">read_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-78"><a href="#Communication-78"><span class="linenos"> 78</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="Communication-79"><a href="#Communication-79"><span class="linenos"> 79</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-80"><a href="#Communication-80"><span class="linenos"> 80</span></a>
</span><span id="Communication-81"><a href="#Communication-81"><span class="linenos"> 81</span></a>        <span class="k">def</span> <span class="nf">send_async_named</span><span class="p">(</span>
</span><span id="Communication-82"><a href="#Communication-82"><span class="linenos"> 82</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-83"><a href="#Communication-83"><span class="linenos"> 83</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication-84"><a href="#Communication-84"><span class="linenos"> 84</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-85"><a href="#Communication-85"><span class="linenos"> 85</span></a>
</span><span id="Communication-86"><a href="#Communication-86"><span class="linenos"> 86</span></a>        <span class="k">def</span> <span class="nf">send_blocking_named</span><span class="p">(</span>
</span><span id="Communication-87"><a href="#Communication-87"><span class="linenos"> 87</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-88"><a href="#Communication-88"><span class="linenos"> 88</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication-89"><a href="#Communication-89"><span class="linenos"> 89</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-90"><a href="#Communication-90"><span class="linenos"> 90</span></a>
</span><span id="Communication-91"><a href="#Communication-91"><span class="linenos"> 91</span></a>        <span class="k">def</span> <span class="nf">read_async_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-92"><a href="#Communication-92"><span class="linenos"> 92</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="Communication-93"><a href="#Communication-93"><span class="linenos"> 93</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-94"><a href="#Communication-94"><span class="linenos"> 94</span></a>
</span><span id="Communication-95"><a href="#Communication-95"><span class="linenos"> 95</span></a>        <span class="k">def</span> <span class="nf">read_blocking_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication-96"><a href="#Communication-96"><span class="linenos"> 96</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="Communication-97"><a href="#Communication-97"><span class="linenos"> 97</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication-98"><a href="#Communication-98"><span class="linenos"> 98</span></a>
</span><span id="Communication-99"><a href="#Communication-99"><span class="linenos"> 99</span></a>        <span class="k">def</span> <span class="nf">_save</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__request__type__</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Communication-100"><a href="#Communication-100"><span class="linenos">100</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_type</span> <span class="o">=</span> <span class="n">__request__type__</span>
</span><span id="Communication-101"><a href="#Communication-101"><span class="linenos">101</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="Communication-102"><a href="#Communication-102"><span class="linenos">102</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="Communication-103"><a href="#Communication-103"><span class="linenos">103</span></a>
</span><span id="Communication-104"><a href="#Communication-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Communication-105"><a href="#Communication-105"><span class="linenos">105</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Communication</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="Communication-106"><a href="#Communication-106"><span class="linenos">106</span></a>
</span><span id="Communication-107"><a href="#Communication-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Communication-108"><a href="#Communication-108"><span class="linenos">108</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="s1">&#39;Communication.Requests&#39;</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
</span><span id="Communication-109"><a href="#Communication-109"><span class="linenos">109</span></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="Communication-110"><a href="#Communication-110"><span class="linenos">110</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-111"><a href="#Communication-111"><span class="linenos">111</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_send_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication-112"><a href="#Communication-112"><span class="linenos">112</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-113"><a href="#Communication-113"><span class="linenos">113</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-114"><a href="#Communication-114"><span class="linenos">114</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_send_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication-115"><a href="#Communication-115"><span class="linenos">115</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-116"><a href="#Communication-116"><span class="linenos">116</span></a>        <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-117"><a href="#Communication-117"><span class="linenos">117</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_read_async</span><span class="p">()</span>
</span><span id="Communication-118"><a href="#Communication-118"><span class="linenos">118</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-119"><a href="#Communication-119"><span class="linenos">119</span></a>        <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-120"><a href="#Communication-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_read_sync</span><span class="p">()</span>
</span><span id="Communication-121"><a href="#Communication-121"><span class="linenos">121</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-122"><a href="#Communication-122"><span class="linenos">122</span></a>        <span class="k">elif</span> <span class="mi">4</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-123"><a href="#Communication-123"><span class="linenos">123</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_send_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication-124"><a href="#Communication-124"><span class="linenos">124</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-125"><a href="#Communication-125"><span class="linenos">125</span></a>        <span class="k">elif</span> <span class="mi">5</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-126"><a href="#Communication-126"><span class="linenos">126</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_send_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication-127"><a href="#Communication-127"><span class="linenos">127</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-128"><a href="#Communication-128"><span class="linenos">128</span></a>        <span class="k">elif</span> <span class="mi">6</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-129"><a href="#Communication-129"><span class="linenos">129</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_named_read_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication-130"><a href="#Communication-130"><span class="linenos">130</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-131"><a href="#Communication-131"><span class="linenos">131</span></a>        <span class="k">elif</span> <span class="mi">7</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication-132"><a href="#Communication-132"><span class="linenos">132</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_read_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication-133"><a href="#Communication-133"><span class="linenos">133</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication-134"><a href="#Communication-134"><span class="linenos">134</span></a>
</span><span id="Communication-135"><a href="#Communication-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">request_send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication-136"><a href="#Communication-136"><span class="linenos">136</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-137"><a href="#Communication-137"><span class="linenos">137</span></a>
</span><span id="Communication-138"><a href="#Communication-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">request_send_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication-139"><a href="#Communication-139"><span class="linenos">139</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-140"><a href="#Communication-140"><span class="linenos">140</span></a>
</span><span id="Communication-141"><a href="#Communication-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="nf">request_read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="Communication-142"><a href="#Communication-142"><span class="linenos">142</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Communication-143"><a href="#Communication-143"><span class="linenos">143</span></a><span class="sd">        Will return tuple with sender coro ID and message</span>
</span><span id="Communication-144"><a href="#Communication-144"><span class="linenos">144</span></a>
</span><span id="Communication-145"><a href="#Communication-145"><span class="linenos">145</span></a><span class="sd">        :rtype: Tuple[CoroID, Any]</span>
</span><span id="Communication-146"><a href="#Communication-146"><span class="linenos">146</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Communication-147"><a href="#Communication-147"><span class="linenos">147</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-148"><a href="#Communication-148"><span class="linenos">148</span></a>
</span><span id="Communication-149"><a href="#Communication-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">request_read_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication-150"><a href="#Communication-150"><span class="linenos">150</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-151"><a href="#Communication-151"><span class="linenos">151</span></a>
</span><span id="Communication-152"><a href="#Communication-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">request_named_send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication-153"><a href="#Communication-153"><span class="linenos">153</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-154"><a href="#Communication-154"><span class="linenos">154</span></a>
</span><span id="Communication-155"><a href="#Communication-155"><span class="linenos">155</span></a>    <span class="k">def</span> <span class="nf">request_named_send_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication-156"><a href="#Communication-156"><span class="linenos">156</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-157"><a href="#Communication-157"><span class="linenos">157</span></a>
</span><span id="Communication-158"><a href="#Communication-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">request_named_read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="Communication-159"><a href="#Communication-159"><span class="linenos">159</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Communication-160"><a href="#Communication-160"><span class="linenos">160</span></a><span class="sd">        Will return tuple with sender ID and message</span>
</span><span id="Communication-161"><a href="#Communication-161"><span class="linenos">161</span></a>
</span><span id="Communication-162"><a href="#Communication-162"><span class="linenos">162</span></a><span class="sd">        :rtype: Tuple[Hashable, Any]</span>
</span><span id="Communication-163"><a href="#Communication-163"><span class="linenos">163</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Communication-164"><a href="#Communication-164"><span class="linenos">164</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-165"><a href="#Communication-165"><span class="linenos">165</span></a>
</span><span id="Communication-166"><a href="#Communication-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">request_named_read_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication-167"><a href="#Communication-167"><span class="linenos">167</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Communication-168"><a href="#Communication-168"><span class="linenos">168</span></a>
</span><span id="Communication-169"><a href="#Communication-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Communication-170"><a href="#Communication-170"><span class="linenos">170</span></a>        <span class="k">pass</span>
</span><span id="Communication-171"><a href="#Communication-171"><span class="linenos">171</span></a>
</span><span id="Communication-172"><a href="#Communication-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Communication-173"><a href="#Communication-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="Communication.__init__" class="classattr">
                                        <input id="Communication.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Communication</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="Communication.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.__init__-104"><a href="#Communication.__init__-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Communication.__init__-105"><a href="#Communication.__init__-105"><span class="linenos">105</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Communication</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="Communication.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n"><a href="#Communication.Requests">Communication.Requests</a></span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="Communication.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.single_task_registration_or_immediate_processing-107"><a href="#Communication.single_task_registration_or_immediate_processing-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-108"><a href="#Communication.single_task_registration_or_immediate_processing-108"><span class="linenos">108</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="s1">&#39;Communication.Requests&#39;</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-109"><a href="#Communication.single_task_registration_or_immediate_processing-109"><span class="linenos">109</span></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-110"><a href="#Communication.single_task_registration_or_immediate_processing-110"><span class="linenos">110</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-111"><a href="#Communication.single_task_registration_or_immediate_processing-111"><span class="linenos">111</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_send_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-112"><a href="#Communication.single_task_registration_or_immediate_processing-112"><span class="linenos">112</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-113"><a href="#Communication.single_task_registration_or_immediate_processing-113"><span class="linenos">113</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-114"><a href="#Communication.single_task_registration_or_immediate_processing-114"><span class="linenos">114</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_send_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-115"><a href="#Communication.single_task_registration_or_immediate_processing-115"><span class="linenos">115</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-116"><a href="#Communication.single_task_registration_or_immediate_processing-116"><span class="linenos">116</span></a>        <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-117"><a href="#Communication.single_task_registration_or_immediate_processing-117"><span class="linenos">117</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_read_async</span><span class="p">()</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-118"><a href="#Communication.single_task_registration_or_immediate_processing-118"><span class="linenos">118</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-119"><a href="#Communication.single_task_registration_or_immediate_processing-119"><span class="linenos">119</span></a>        <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-120"><a href="#Communication.single_task_registration_or_immediate_processing-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_read_sync</span><span class="p">()</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-121"><a href="#Communication.single_task_registration_or_immediate_processing-121"><span class="linenos">121</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-122"><a href="#Communication.single_task_registration_or_immediate_processing-122"><span class="linenos">122</span></a>        <span class="k">elif</span> <span class="mi">4</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-123"><a href="#Communication.single_task_registration_or_immediate_processing-123"><span class="linenos">123</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_send_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-124"><a href="#Communication.single_task_registration_or_immediate_processing-124"><span class="linenos">124</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-125"><a href="#Communication.single_task_registration_or_immediate_processing-125"><span class="linenos">125</span></a>        <span class="k">elif</span> <span class="mi">5</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-126"><a href="#Communication.single_task_registration_or_immediate_processing-126"><span class="linenos">126</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_send_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-127"><a href="#Communication.single_task_registration_or_immediate_processing-127"><span class="linenos">127</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-128"><a href="#Communication.single_task_registration_or_immediate_processing-128"><span class="linenos">128</span></a>        <span class="k">elif</span> <span class="mi">6</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-129"><a href="#Communication.single_task_registration_or_immediate_processing-129"><span class="linenos">129</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_named_read_async</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-130"><a href="#Communication.single_task_registration_or_immediate_processing-130"><span class="linenos">130</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-131"><a href="#Communication.single_task_registration_or_immediate_processing-131"><span class="linenos">131</span></a>        <span class="k">elif</span> <span class="mi">7</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">:</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-132"><a href="#Communication.single_task_registration_or_immediate_processing-132"><span class="linenos">132</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_named_read_sync</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Communication.single_task_registration_or_immediate_processing-133"><a href="#Communication.single_task_registration_or_immediate_processing-133"><span class="linenos">133</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.request_send_async" class="classattr">
                                        <input id="Communication.request_send_async-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_send_async</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">recipient_id</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n">NoReturn</span>:</span></span>

                <label class="view-source-button" for="Communication.request_send_async-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_send_async"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_send_async-135"><a href="#Communication.request_send_async-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">request_send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication.request_send_async-136"><a href="#Communication.request_send_async-136"><span class="linenos">136</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.request_send_sync" class="classattr">
                                        <input id="Communication.request_send_sync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_send_sync</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">recipient_id</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n">NoReturn</span>:</span></span>

                <label class="view-source-button" for="Communication.request_send_sync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_send_sync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_send_sync-138"><a href="#Communication.request_send_sync-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">request_send_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication.request_send_sync-139"><a href="#Communication.request_send_sync-139"><span class="linenos">139</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.request_read_async" class="classattr">
                                        <input id="Communication.request_read_async-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_read_async</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="Communication.request_read_async-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_read_async"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_read_async-141"><a href="#Communication.request_read_async-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="nf">request_read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="Communication.request_read_async-142"><a href="#Communication.request_read_async-142"><span class="linenos">142</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Communication.request_read_async-143"><a href="#Communication.request_read_async-143"><span class="linenos">143</span></a><span class="sd">        Will return tuple with sender coro ID and message</span>
</span><span id="Communication.request_read_async-144"><a href="#Communication.request_read_async-144"><span class="linenos">144</span></a>
</span><span id="Communication.request_read_async-145"><a href="#Communication.request_read_async-145"><span class="linenos">145</span></a><span class="sd">        :rtype: Tuple[CoroID, Any]</span>
</span><span id="Communication.request_read_async-146"><a href="#Communication.request_read_async-146"><span class="linenos">146</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Communication.request_read_async-147"><a href="#Communication.request_read_async-147"><span class="linenos">147</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Will return tuple with sender coro ID and message</p>

<p>:rtype: Tuple[CoroID, Any]</p>
</div>


                            </div>
                            <div id="Communication.request_read_sync" class="classattr">
                                        <input id="Communication.request_read_sync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_read_sync</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">NoReturn</span>:</span></span>

                <label class="view-source-button" for="Communication.request_read_sync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_read_sync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_read_sync-149"><a href="#Communication.request_read_sync-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">request_read_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication.request_read_sync-150"><a href="#Communication.request_read_sync-150"><span class="linenos">150</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.request_named_send_async" class="classattr">
                                        <input id="Communication.request_named_send_async-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_named_send_async</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">sender_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n">NoReturn</span>:</span></span>

                <label class="view-source-button" for="Communication.request_named_send_async-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_named_send_async"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_named_send_async-152"><a href="#Communication.request_named_send_async-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">request_named_send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication.request_named_send_async-153"><a href="#Communication.request_named_send_async-153"><span class="linenos">153</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.request_named_send_sync" class="classattr">
                                        <input id="Communication.request_named_send_sync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_named_send_sync</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">sender_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n">NoReturn</span>:</span></span>

                <label class="view-source-button" for="Communication.request_named_send_sync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_named_send_sync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_named_send_sync-155"><a href="#Communication.request_named_send_sync-155"><span class="linenos">155</span></a>    <span class="k">def</span> <span class="nf">request_named_send_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication.request_named_send_sync-156"><a href="#Communication.request_named_send_sync-156"><span class="linenos">156</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.request_named_read_async" class="classattr">
                                        <input id="Communication.request_named_read_async-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_named_read_async</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="Communication.request_named_read_async-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_named_read_async"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_named_read_async-158"><a href="#Communication.request_named_read_async-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">request_named_read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="Communication.request_named_read_async-159"><a href="#Communication.request_named_read_async-159"><span class="linenos">159</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Communication.request_named_read_async-160"><a href="#Communication.request_named_read_async-160"><span class="linenos">160</span></a><span class="sd">        Will return tuple with sender ID and message</span>
</span><span id="Communication.request_named_read_async-161"><a href="#Communication.request_named_read_async-161"><span class="linenos">161</span></a>
</span><span id="Communication.request_named_read_async-162"><a href="#Communication.request_named_read_async-162"><span class="linenos">162</span></a><span class="sd">        :rtype: Tuple[Hashable, Any]</span>
</span><span id="Communication.request_named_read_async-163"><a href="#Communication.request_named_read_async-163"><span class="linenos">163</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Communication.request_named_read_async-164"><a href="#Communication.request_named_read_async-164"><span class="linenos">164</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Will return tuple with sender ID and message</p>

<p>:rtype: Tuple[Hashable, Any]</p>
</div>


                            </div>
                            <div id="Communication.request_named_read_sync" class="classattr">
                                        <input id="Communication.request_named_read_sync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_named_read_sync</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="n">NoReturn</span>:</span></span>

                <label class="view-source-button" for="Communication.request_named_read_sync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.request_named_read_sync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.request_named_read_sync-166"><a href="#Communication.request_named_read_sync-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">request_named_read_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NoReturn</span><span class="p">:</span>
</span><span id="Communication.request_named_read_sync-167"><a href="#Communication.request_named_read_sync-167"><span class="linenos">167</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.full_processing_iteration" class="classattr">
                                        <input id="Communication.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Communication.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.full_processing_iteration-169"><a href="#Communication.full_processing_iteration-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Communication.full_processing_iteration-170"><a href="#Communication.full_processing_iteration-170"><span class="linenos">170</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.in_work" class="classattr">
                                        <input id="Communication.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="Communication.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.in_work-172"><a href="#Communication.in_work-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Communication.in_work-173"><a href="#Communication.in_work-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span>
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
                                <dd id="Communication.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="Communication.iteration" class="function">iteration</dd>
                <dd id="Communication.make_response" class="function">make_response</dd>
                <dd id="Communication.register_response" class="function">register_response</dd>
                <dd id="Communication.put_task" class="function">put_task</dd>
                <dd id="Communication.resolve_request" class="function">resolve_request</dd>
                <dd id="Communication.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="Communication.in_forground_work" class="function">in_forground_work</dd>
                <dd id="Communication.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="Communication.time_left_before_next_event" class="function">time_left_before_next_event</dd>
                <dd id="Communication.is_low_latency" class="function">is_low_latency</dd>
                <dd id="Communication.make_live" class="function">make_live</dd>
                <dd id="Communication.make_dead" class="function">make_dead</dd>
                <dd id="Communication.service_id_impl" class="function">service_id_impl</dd>
                <dd id="Communication.service_id" class="function">service_id</dd>
                <dd id="Communication.destroy" class="function">destroy</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Communication.Requests">
                            <input id="Communication.Requests-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Communication.Requests</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="Communication.Requests-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Requests"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Requests-47"><a href="#Communication.Requests-47"><span class="linenos">47</span></a>    <span class="k">class</span> <span class="nc">Requests</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="Communication.Requests-48"><a href="#Communication.Requests-48"><span class="linenos">48</span></a>        <span class="n">send_async</span> <span class="o">=</span> <span class="mi">0</span>        <span class="c1"># Coro will get control immediately after message sent</span>
</span><span id="Communication.Requests-49"><a href="#Communication.Requests-49"><span class="linenos">49</span></a>        <span class="n">send_sync</span> <span class="o">=</span> <span class="mi">1</span>         <span class="c1"># Coro will get control only after response will be received</span>
</span><span id="Communication.Requests-50"><a href="#Communication.Requests-50"><span class="linenos">50</span></a>        <span class="n">read_async</span> <span class="o">=</span> <span class="mi">2</span>        <span class="c1"># Coro will get control immediately even if input queue is empty</span>
</span><span id="Communication.Requests-51"><a href="#Communication.Requests-51"><span class="linenos">51</span></a>        <span class="n">read_sync</span> <span class="o">=</span> <span class="mi">3</span>         <span class="c1"># Coro will get control only if input queue is not empty or when new response will be</span>
</span><span id="Communication.Requests-52"><a href="#Communication.Requests-52"><span class="linenos">52</span></a>        <span class="c1"># received</span>
</span><span id="Communication.Requests-53"><a href="#Communication.Requests-53"><span class="linenos">53</span></a>        <span class="n">named_send_async</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># Coro will get control immediately after message sent</span>
</span><span id="Communication.Requests-54"><a href="#Communication.Requests-54"><span class="linenos">54</span></a>        <span class="n">named_send_sync</span> <span class="o">=</span> <span class="mi">5</span>   <span class="c1"># Coro will get control only after response will be received</span>
</span><span id="Communication.Requests-55"><a href="#Communication.Requests-55"><span class="linenos">55</span></a>        <span class="n">named_read_async</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># Coro will get control immediately even if input queue is empty</span>
</span><span id="Communication.Requests-56"><a href="#Communication.Requests-56"><span class="linenos">56</span></a>        <span class="n">named_read_sync</span> <span class="o">=</span> <span class="mi">7</span>   <span class="c1"># Coro will get control only if input queue is not empty or when new response will be</span>
</span><span id="Communication.Requests-57"><a href="#Communication.Requests-57"><span class="linenos">57</span></a>        <span class="c1"># received</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="Communication.Requests.send_async" class="classattr">
                                <div class="attr variable">
            <span class="name">send_async</span>        =
<span class="default_value">&lt;Requests.send_async: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.send_async"></a>
    
    

                            </div>
                            <div id="Communication.Requests.send_sync" class="classattr">
                                <div class="attr variable">
            <span class="name">send_sync</span>        =
<span class="default_value">&lt;Requests.send_sync: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.send_sync"></a>
    
    

                            </div>
                            <div id="Communication.Requests.read_async" class="classattr">
                                <div class="attr variable">
            <span class="name">read_async</span>        =
<span class="default_value">&lt;Requests.read_async: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.read_async"></a>
    
    

                            </div>
                            <div id="Communication.Requests.read_sync" class="classattr">
                                <div class="attr variable">
            <span class="name">read_sync</span>        =
<span class="default_value">&lt;Requests.read_sync: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.read_sync"></a>
    
    

                            </div>
                            <div id="Communication.Requests.named_send_async" class="classattr">
                                <div class="attr variable">
            <span class="name">named_send_async</span>        =
<span class="default_value">&lt;Requests.named_send_async: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.named_send_async"></a>
    
    

                            </div>
                            <div id="Communication.Requests.named_send_sync" class="classattr">
                                <div class="attr variable">
            <span class="name">named_send_sync</span>        =
<span class="default_value">&lt;Requests.named_send_sync: 5&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.named_send_sync"></a>
    
    

                            </div>
                            <div id="Communication.Requests.named_read_async" class="classattr">
                                <div class="attr variable">
            <span class="name">named_read_async</span>        =
<span class="default_value">&lt;Requests.named_read_async: 6&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.named_read_async"></a>
    
    

                            </div>
                            <div id="Communication.Requests.named_read_sync" class="classattr">
                                <div class="attr variable">
            <span class="name">named_read_sync</span>        =
<span class="default_value">&lt;Requests.named_read_sync: 7&gt;</span>

        
    </div>
    <a class="headerlink" href="#Communication.Requests.named_read_sync"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="Communication.Requests.name" class="variable">name</dd>
                <dd id="Communication.Requests.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Communication.Request">
                            <input id="Communication.Request-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Communication.Request</span>:

                <label class="view-source-button" for="Communication.Request-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request-59"><a href="#Communication.Request-59"><span class="linenos"> 59</span></a>    <span class="k">class</span> <span class="nc">Request</span><span class="p">:</span>
</span><span id="Communication.Request-60"><a href="#Communication.Request-60"><span class="linenos"> 60</span></a>        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Communication.Request-61"><a href="#Communication.Request-61"><span class="linenos"> 61</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_type</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># type: Optional[int]</span>
</span><span id="Communication.Request-62"><a href="#Communication.Request-62"><span class="linenos"> 62</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="kc">None</span>          <span class="c1"># type: Optional[Tuple]</span>
</span><span id="Communication.Request-63"><a href="#Communication.Request-63"><span class="linenos"> 63</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="kc">None</span>        <span class="c1"># type: Optional[Dict]</span>
</span><span id="Communication.Request-64"><a href="#Communication.Request-64"><span class="linenos"> 64</span></a>
</span><span id="Communication.Request-65"><a href="#Communication.Request-65"><span class="linenos"> 65</span></a>        <span class="k">def</span> <span class="nf">send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-66"><a href="#Communication.Request-66"><span class="linenos"> 66</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request-67"><a href="#Communication.Request-67"><span class="linenos"> 67</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-68"><a href="#Communication.Request-68"><span class="linenos"> 68</span></a>
</span><span id="Communication.Request-69"><a href="#Communication.Request-69"><span class="linenos"> 69</span></a>        <span class="k">def</span> <span class="nf">send_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-70"><a href="#Communication.Request-70"><span class="linenos"> 70</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request-71"><a href="#Communication.Request-71"><span class="linenos"> 71</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-72"><a href="#Communication.Request-72"><span class="linenos"> 72</span></a>
</span><span id="Communication.Request-73"><a href="#Communication.Request-73"><span class="linenos"> 73</span></a>        <span class="k">def</span> <span class="nf">read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-74"><a href="#Communication.Request-74"><span class="linenos"> 74</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="Communication.Request-75"><a href="#Communication.Request-75"><span class="linenos"> 75</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-76"><a href="#Communication.Request-76"><span class="linenos"> 76</span></a>
</span><span id="Communication.Request-77"><a href="#Communication.Request-77"><span class="linenos"> 77</span></a>        <span class="k">def</span> <span class="nf">read_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-78"><a href="#Communication.Request-78"><span class="linenos"> 78</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="Communication.Request-79"><a href="#Communication.Request-79"><span class="linenos"> 79</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-80"><a href="#Communication.Request-80"><span class="linenos"> 80</span></a>
</span><span id="Communication.Request-81"><a href="#Communication.Request-81"><span class="linenos"> 81</span></a>        <span class="k">def</span> <span class="nf">send_async_named</span><span class="p">(</span>
</span><span id="Communication.Request-82"><a href="#Communication.Request-82"><span class="linenos"> 82</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-83"><a href="#Communication.Request-83"><span class="linenos"> 83</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request-84"><a href="#Communication.Request-84"><span class="linenos"> 84</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-85"><a href="#Communication.Request-85"><span class="linenos"> 85</span></a>
</span><span id="Communication.Request-86"><a href="#Communication.Request-86"><span class="linenos"> 86</span></a>        <span class="k">def</span> <span class="nf">send_blocking_named</span><span class="p">(</span>
</span><span id="Communication.Request-87"><a href="#Communication.Request-87"><span class="linenos"> 87</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-88"><a href="#Communication.Request-88"><span class="linenos"> 88</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request-89"><a href="#Communication.Request-89"><span class="linenos"> 89</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-90"><a href="#Communication.Request-90"><span class="linenos"> 90</span></a>
</span><span id="Communication.Request-91"><a href="#Communication.Request-91"><span class="linenos"> 91</span></a>        <span class="k">def</span> <span class="nf">read_async_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-92"><a href="#Communication.Request-92"><span class="linenos"> 92</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="Communication.Request-93"><a href="#Communication.Request-93"><span class="linenos"> 93</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-94"><a href="#Communication.Request-94"><span class="linenos"> 94</span></a>
</span><span id="Communication.Request-95"><a href="#Communication.Request-95"><span class="linenos"> 95</span></a>        <span class="k">def</span> <span class="nf">read_blocking_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request-96"><a href="#Communication.Request-96"><span class="linenos"> 96</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="Communication.Request-97"><a href="#Communication.Request-97"><span class="linenos"> 97</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span><span id="Communication.Request-98"><a href="#Communication.Request-98"><span class="linenos"> 98</span></a>
</span><span id="Communication.Request-99"><a href="#Communication.Request-99"><span class="linenos"> 99</span></a>        <span class="k">def</span> <span class="nf">_save</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__request__type__</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Communication.Request-100"><a href="#Communication.Request-100"><span class="linenos">100</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">request_type</span> <span class="o">=</span> <span class="n">__request__type__</span>
</span><span id="Communication.Request-101"><a href="#Communication.Request-101"><span class="linenos">101</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="Communication.Request-102"><a href="#Communication.Request-102"><span class="linenos">102</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            <div id="Communication.Request.request_type" class="classattr">
                                <div class="attr variable">
            <span class="name">request_type</span>

        
    </div>
    <a class="headerlink" href="#Communication.Request.request_type"></a>
    
    

                            </div>
                            <div id="Communication.Request.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span>

        
    </div>
    <a class="headerlink" href="#Communication.Request.args"></a>
    
    

                            </div>
                            <div id="Communication.Request.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span>

        
    </div>
    <a class="headerlink" href="#Communication.Request.kwargs"></a>
    
    

                            </div>
                            <div id="Communication.Request.send_async" class="classattr">
                                        <input id="Communication.Request.send_async-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">send_async</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.send_async-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.send_async"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.send_async-65"><a href="#Communication.Request.send_async-65"><span class="linenos">65</span></a>        <span class="k">def</span> <span class="nf">send_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.send_async-66"><a href="#Communication.Request.send_async-66"><span class="linenos">66</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request.send_async-67"><a href="#Communication.Request.send_async-67"><span class="linenos">67</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.Request.send_blocking" class="classattr">
                                        <input id="Communication.Request.send_blocking-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">send_blocking</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.send_blocking-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.send_blocking"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.send_blocking-69"><a href="#Communication.Request.send_blocking-69"><span class="linenos">69</span></a>        <span class="k">def</span> <span class="nf">send_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.send_blocking-70"><a href="#Communication.Request.send_blocking-70"><span class="linenos">70</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request.send_blocking-71"><a href="#Communication.Request.send_blocking-71"><span class="linenos">71</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.Request.read_async" class="classattr">
                                        <input id="Communication.Request.read_async-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_async</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.read_async-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.read_async"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.read_async-73"><a href="#Communication.Request.read_async-73"><span class="linenos">73</span></a>        <span class="k">def</span> <span class="nf">read_async</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.read_async-74"><a href="#Communication.Request.read_async-74"><span class="linenos">74</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="Communication.Request.read_async-75"><a href="#Communication.Request.read_async-75"><span class="linenos">75</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.Request.read_blocking" class="classattr">
                                        <input id="Communication.Request.read_blocking-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_blocking</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.read_blocking-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.read_blocking"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.read_blocking-77"><a href="#Communication.Request.read_blocking-77"><span class="linenos">77</span></a>        <span class="k">def</span> <span class="nf">read_blocking</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.read_blocking-78"><a href="#Communication.Request.read_blocking-78"><span class="linenos">78</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="Communication.Request.read_blocking-79"><a href="#Communication.Request.read_blocking-79"><span class="linenos">79</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.Request.send_async_named" class="classattr">
                                        <input id="Communication.Request.send_async_named-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">send_async_named</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">sender_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.send_async_named-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.send_async_named"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.send_async_named-81"><a href="#Communication.Request.send_async_named-81"><span class="linenos">81</span></a>        <span class="k">def</span> <span class="nf">send_async_named</span><span class="p">(</span>
</span><span id="Communication.Request.send_async_named-82"><a href="#Communication.Request.send_async_named-82"><span class="linenos">82</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.send_async_named-83"><a href="#Communication.Request.send_async_named-83"><span class="linenos">83</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request.send_async_named-84"><a href="#Communication.Request.send_async_named-84"><span class="linenos">84</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.Request.send_blocking_named" class="classattr">
                                        <input id="Communication.Request.send_blocking_named-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">send_blocking_named</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">sender_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">message</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.send_blocking_named-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.send_blocking_named"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.send_blocking_named-86"><a href="#Communication.Request.send_blocking_named-86"><span class="linenos">86</span></a>        <span class="k">def</span> <span class="nf">send_blocking_named</span><span class="p">(</span>
</span><span id="Communication.Request.send_blocking_named-87"><a href="#Communication.Request.send_blocking_named-87"><span class="linenos">87</span></a>                <span class="bp">self</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.send_blocking_named-88"><a href="#Communication.Request.send_blocking_named-88"><span class="linenos">88</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">sender_id</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>
</span><span id="Communication.Request.send_blocking_named-89"><a href="#Communication.Request.send_blocking_named-89"><span class="linenos">89</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.Request.read_async_named" class="classattr">
                                        <input id="Communication.Request.read_async_named-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_async_named</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.read_async_named-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.read_async_named"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.read_async_named-91"><a href="#Communication.Request.read_async_named-91"><span class="linenos">91</span></a>        <span class="k">def</span> <span class="nf">read_async_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.read_async_named-92"><a href="#Communication.Request.read_async_named-92"><span class="linenos">92</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="Communication.Request.read_async_named-93"><a href="#Communication.Request.read_async_named-93"><span class="linenos">93</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="Communication.Request.read_blocking_named" class="classattr">
                                        <input id="Communication.Request.read_blocking_named-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_blocking_named</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">recipient_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="n"><a href="#Communication.Request">Communication.Request</a></span>:</span></span>

                <label class="view-source-button" for="Communication.Request.read_blocking_named-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Communication.Request.read_blocking_named"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Communication.Request.read_blocking_named-95"><a href="#Communication.Request.read_blocking_named-95"><span class="linenos">95</span></a>        <span class="k">def</span> <span class="nf">read_blocking_named</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;Communication.Request&#39;</span><span class="p">:</span>
</span><span id="Communication.Request.read_blocking_named-96"><a href="#Communication.Request.read_blocking_named-96"><span class="linenos">96</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">recipient_id</span><span class="p">)</span>
</span><span id="Communication.Request.read_blocking_named-97"><a href="#Communication.Request.read_blocking_named-97"><span class="linenos">97</span></a>            <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>