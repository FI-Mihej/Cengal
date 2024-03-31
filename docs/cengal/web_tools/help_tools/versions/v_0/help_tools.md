---
title: help_tools
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.web_tools<wbr>.help_tools<wbr>.versions<wbr>.v_0<wbr>.help_tools    </h1>

                
                        <input id="mod-help_tools-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-help_tools-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">import</span> <span class="nn">platform</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="k">if</span> <span class="s1">&#39;PyPy&#39;</span> <span class="o">!=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_implementation</span><span class="p">():</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>    <span class="kn">import</span> <span class="nn">requests</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">import</span> <span class="nn">binascii</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">import</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">os.path</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">import</span> <span class="nn">pickle</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">import</span> <span class="nn">datetime</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="c1"># try to import C parser then fallback in pure python parser.</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a>    <span class="kn">from</span> <span class="nn">http_parser.parser</span> <span class="kn">import</span> <span class="n">HttpParser</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>    <span class="kn">from</span> <span class="nn">http_parser.pyparser</span> <span class="kn">import</span> <span class="n">HttpParser</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">from</span> <span class="nn">cengal.modules_management.alternative_import</span> <span class="kn">import</span> <span class="n">alt_import</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;lzma&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">lzma</span><span class="p">:</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>    <span class="k">if</span> <span class="n">lzma</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>        <span class="kn">import</span> <span class="nn">lzmaffi.compat</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>        <span class="n">lzmaffi</span><span class="o">.</span><span class="n">compat</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>        <span class="kn">import</span> <span class="nn">lzma</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="sd">Module Docstring</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.2.0&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="k">def</span> <span class="nf">remove_percent_encoding_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="n">plus</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="k">if</span> <span class="n">plus</span><span class="p">:</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>            <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;+&#39;</span><span class="p">,</span> <span class="s1">&#39; &#39;</span><span class="p">)</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="n">percentTypes</span> <span class="o">=</span> <span class="p">((</span><span class="sa">b</span><span class="s1">&#39;</span><span class="si">%u</span><span class="s1">&#39;</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)),</span> <span class="p">(</span><span class="sa">b</span><span class="s1">&#39;%&#39;</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">32</span><span class="p">))</span> <span class="o">+</span> <span class="p">(</span><span class="mi">34</span><span class="p">,</span> <span class="mi">42</span><span class="p">,</span> <span class="mi">58</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span> <span class="mi">62</span><span class="p">,</span> <span class="mi">63</span><span class="p">,</span> <span class="mi">124</span><span class="p">,</span> <span class="mi">127</span><span class="p">))))</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>        <span class="c1"># (prefix, full size, (allowed type or not at all, list of disallowed characters like backspace etc.))</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="k">for</span> <span class="n">percType</span> <span class="ow">in</span> <span class="n">percentTypes</span><span class="p">:</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>            <span class="n">isDone</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>            <span class="k">while</span> <span class="ow">not</span> <span class="n">isDone</span><span class="p">:</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>                <span class="n">index</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">percType</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>                    <span class="n">ind2</span> <span class="o">=</span> <span class="n">index</span><span class="o">+</span><span class="n">percType</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>                    <span class="k">if</span> <span class="n">ind2</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>                        <span class="n">ind2</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>                    <span class="n">hexString</span> <span class="o">=</span> <span class="n">string</span><span class="p">[</span><span class="n">index</span><span class="p">:</span><span class="n">ind2</span><span class="p">]</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>                    <span class="n">hexString</span> <span class="o">=</span> <span class="n">hexString</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">percType</span><span class="p">[</span><span class="mi">0</span><span class="p">]):]</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>                    <span class="n">decodedString</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>                    <span class="k">if</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>                        <span class="k">try</span><span class="p">:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>                            <span class="n">decodedStringBuff</span> <span class="o">=</span> <span class="n">binascii</span><span class="o">.</span><span class="n">unhexlify</span><span class="p">(</span><span class="n">hexString</span><span class="p">)</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>                            <span class="k">if</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">decodedStringBuff</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>                                <span class="n">decodedString</span> <span class="o">=</span> <span class="n">decodedStringBuff</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>                        <span class="k">except</span> <span class="n">binascii</span><span class="o">.</span><span class="n">Error</span><span class="p">:</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>                            <span class="k">pass</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>                    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="p">[:</span><span class="n">index</span><span class="p">]</span> <span class="o">+</span> <span class="n">decodedString</span> <span class="o">+</span> <span class="n">string</span><span class="p">[</span><span class="n">ind2</span><span class="p">:]</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>                    <span class="n">isDone</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>            <span class="k">if</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>                <span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">string</span><span class="p">)</span><span class="o">.</span><span class="n">intersection</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">])))</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>                    <span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>                    <span class="n">isDone</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>                    <span class="k">while</span> <span class="ow">not</span> <span class="n">isDone</span><span class="p">:</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>                        <span class="k">if</span> <span class="n">string</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="ow">in</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>                            <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="p">[:</span><span class="n">index</span><span class="p">]</span> <span class="o">+</span> <span class="n">string</span><span class="p">[</span><span class="n">index</span><span class="o">+</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>                        <span class="k">else</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>                            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>                        <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>                            <span class="n">isDone</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="k">except</span> <span class="ne">UnicodeDecodeError</span><span class="p">:</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="k">except</span> <span class="ne">UnicodeEncodeError</span><span class="p">:</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">return</span> <span class="n">string</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="k">def</span> <span class="nf">get_standard_folder_separator</span><span class="p">():</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">return</span> <span class="s1">&#39;/&#39;</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a><span class="k">def</span> <span class="nf">unify_folder_separators</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\\</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">get_standard_folder_separator</span><span class="p">())</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="k">return</span> <span class="n">string</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a><span class="k">def</span> <span class="nf">remove_forbidden_file_names_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>    <span class="c1"># replace forbidden file names with slash (&#39;/&#39;). Also will unify folder separators (replace &#39;\&#39; with &#39;/&#39;)</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="n">forbiddenFileNames</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;con&#39;</span><span class="p">,</span> <span class="s1">&#39;prn&#39;</span><span class="p">,</span> <span class="s1">&#39;aux&#39;</span><span class="p">,</span> <span class="s1">&#39;nul&#39;</span><span class="p">,</span> <span class="s1">&#39;com1&#39;</span><span class="p">,</span> <span class="s1">&#39;com2&#39;</span><span class="p">,</span> <span class="s1">&#39;com3&#39;</span><span class="p">,</span> <span class="s1">&#39;com4&#39;</span><span class="p">,</span> <span class="s1">&#39;com5&#39;</span><span class="p">,</span> <span class="s1">&#39;com6&#39;</span><span class="p">,</span> <span class="s1">&#39;com7&#39;</span><span class="p">,</span> <span class="s1">&#39;com8&#39;</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="p">,</span> <span class="s1">&#39;com9&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt1&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt2&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt3&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt4&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt5&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt6&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt7&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt8&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt9&#39;</span><span class="p">}</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">))</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="n">strBuffer</span> <span class="o">=</span> <span class="n">string</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="k">for</span> <span class="n">forbFile</span> <span class="ow">in</span> <span class="n">forbiddenFileNames</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">get_standard_folder_separator</span><span class="p">()</span> <span class="o">+</span> <span class="n">forbFile</span> <span class="o">+</span> <span class="n">get_standard_folder_separator</span><span class="p">(),</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">get_standard_folder_separator</span><span class="p">()</span> <span class="o">+</span> <span class="n">forbFile</span> <span class="o">+</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    <span class="n">isStrWasChanged</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>    <span class="k">if</span> <span class="n">strBuffer</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">!=</span> <span class="n">string</span><span class="p">:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="n">isStrWasChanged</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">strBuffer</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="n">isStrWasChanged</span><span class="p">)</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="k">def</span> <span class="nf">remove_path_to_the_parent_of_the_current_directory</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">))</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;../&#39;</span><span class="p">,</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;/..&#39;</span><span class="p">,</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">return</span> <span class="n">string</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a><span class="k">def</span> <span class="nf">is_path_is_trying_to_leave_site_sandbox</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="n">itemsList</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">get_standard_folder_separator</span><span class="p">())</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    <span class="k">while</span> <span class="s1">&#39;&#39;</span> <span class="ow">in</span> <span class="n">itemsList</span><span class="p">:</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="n">itemsList</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">itemsList</span><span class="p">:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="k">if</span> <span class="n">item</span> <span class="o">==</span> <span class="s1">&#39;..&#39;</span><span class="p">:</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>            <span class="n">counter</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="k">elif</span> <span class="n">item</span> <span class="o">==</span> <span class="s1">&#39;.&#39;</span><span class="p">:</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>            <span class="k">pass</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">if</span> <span class="n">counter</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a><span class="k">def</span> <span class="nf">is_path_is_not_safe</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="c1"># return tuple (decoded string, is_path_is_not_safe)</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">remove_percent_encoding_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>    <span class="k">if</span> <span class="n">string</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">remove_forbidden_file_names_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>    <span class="k">if</span> <span class="n">string</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>    <span class="n">is_not_safe</span> <span class="o">=</span> <span class="n">is_path_is_trying_to_leave_site_sandbox</span><span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">is_not_safe</span><span class="p">)</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="k">def</span> <span class="nf">web_server__is_redirection_to_the_main_domain_needed</span><span class="p">(</span><span class="n">httpParser</span><span class="p">:</span> <span class="n">HttpParser</span><span class="p">,</span> <span class="n">prefix</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>    <span class="n">host</span> <span class="o">=</span> <span class="n">httpParser</span><span class="o">.</span><span class="n">get_headers</span><span class="p">()[</span><span class="s1">&#39;Host&#39;</span><span class="p">]</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>    <span class="n">domain</span> <span class="o">=</span> <span class="n">host</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>    <span class="k">if</span> <span class="s1">&#39;:&#39;</span> <span class="ow">in</span> <span class="n">host</span><span class="p">:</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="n">host</span> <span class="o">=</span> <span class="n">host</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;:&#39;</span><span class="p">)</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="k">while</span> <span class="s1">&#39;&#39;</span> <span class="ow">in</span> <span class="n">host</span><span class="p">:</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>            <span class="n">host</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="n">domain</span> <span class="o">=</span> <span class="n">host</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    <span class="k">if</span> <span class="s1">&#39;.&#39;</span> <span class="ow">in</span> <span class="n">domain</span><span class="p">:</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="n">domain</span> <span class="o">=</span> <span class="n">domain</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="k">if</span> <span class="n">domain</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;&#39;</span><span class="p">:</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>            <span class="k">del</span> <span class="n">domain</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>            <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">if</span> <span class="n">prefix</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            <span class="k">if</span> <span class="n">domain</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="n">prefix</span><span class="p">:</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>                <span class="n">domain</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">prefix</span><span class="p">)</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>                <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="n">lastDLen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">domain</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="k">if</span> <span class="n">domain</span><span class="p">[</span><span class="n">lastDLen</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;&#39;</span><span class="p">:</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>            <span class="k">del</span> <span class="n">domain</span><span class="p">[</span><span class="n">lastDLen</span><span class="p">]</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>            <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="n">domain</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">domain</span><span class="p">)</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>    <span class="k">if</span> <span class="n">host</span><span class="o">.</span><span class="vm">__class__</span> <span class="ow">is</span> <span class="nb">list</span><span class="p">:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">host</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>            <span class="n">host</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">domain</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>            <span class="n">domain</span> <span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">host</span><span class="p">)</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>    <span class="n">functionResult</span> <span class="o">=</span> <span class="p">(</span><span class="n">functionResult</span><span class="p">,</span> <span class="n">domain</span><span class="p">)</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>    <span class="k">return</span> <span class="n">functionResult</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a><span class="k">def</span> <span class="nf">load_cache_from_file</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="n">originalCache</span><span class="p">):</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>    <span class="n">cache</span> <span class="o">=</span> <span class="n">originalCache</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>    <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>            <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="n">dataBuff</span> <span class="o">=</span> <span class="n">originalCache</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>                <span class="c1"># cacheDataFile = open(fileName, &#39;rb&#39;)</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>                <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="n">lzma</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>                <span class="n">cache</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">cacheDataFile</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>                <span class="n">dataBuff</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>                <span class="n">cache</span> <span class="o">=</span> <span class="n">dataBuff</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="k">except</span><span class="p">(</span><span class="ne">EnvironmentError</span><span class="p">,</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PicklingError</span><span class="p">)</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>                <span class="n">cache</span> <span class="o">=</span> <span class="n">dataBuff</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>            <span class="k">finally</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>                <span class="k">if</span> <span class="n">cacheDataFile</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                    <span class="n">cacheDataFile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="k">return</span> <span class="n">cache</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a><span class="k">def</span> <span class="nf">save_cache_to_file</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="n">cache</span><span class="p">):</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>    <span class="k">if</span> <span class="n">cache</span><span class="o">.</span><span class="n">isWasChanged</span><span class="p">:</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="n">isRenamedToBak</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>                <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">):</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                        <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">)</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                    <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>                        <span class="k">pass</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>                <span class="n">os</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">)</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>                <span class="n">isRenamedToBak</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>                <span class="k">pass</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>        <span class="n">isDumped</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            <span class="c1"># cacheDataFile = open(fileName, &#39;wb&#39;)</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>            <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="n">lzma</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="n">lzma</span><span class="o">.</span><span class="n">FORMAT_XZ</span><span class="p">,</span> <span class="n">check</span><span class="o">=</span><span class="n">lzma</span><span class="o">.</span><span class="n">CHECK_CRC64</span><span class="p">,</span> <span class="n">preset</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>            <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">cacheDataFile</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>            <span class="n">cache</span><span class="o">.</span><span class="n">isWasChanged</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>            <span class="n">isDumped</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        <span class="k">except</span><span class="p">(</span><span class="ne">EnvironmentError</span><span class="p">,</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PicklingError</span><span class="p">)</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>            <span class="k">pass</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            <span class="k">if</span> <span class="n">cacheDataFile</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>                <span class="n">cacheDataFile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="k">if</span> <span class="n">isRenamedToBak</span> <span class="ow">and</span> <span class="n">isDumped</span><span class="p">:</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>                <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">)</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>                <span class="k">pass</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a><span class="k">class</span> <span class="nc">CachedRequestError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span> <span class="k">pass</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a><span class="k">def</span> <span class="nf">make_cached_request__get</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">useOnlyCachedResults</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>    <span class="k">if</span> <span class="p">(</span><span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="n">result</span><span class="o">.</span><span class="n">ok</span><span class="p">):</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="k">if</span> <span class="n">useOnlyCachedResults</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>            <span class="k">raise</span> <span class="n">CachedRequestError</span><span class="p">()</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">request</span><span class="p">))</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">SerializableHttpResponseFromRequests</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        <span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a><span class="k">def</span> <span class="nf">make_cached_request__universal</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">workerFunction</span><span class="p">,</span> <span class="n">useOnlyCachedResults</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">workerFunctionParams</span><span class="p">):</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="k">if</span> <span class="n">useOnlyCachedResults</span><span class="p">:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>            <span class="k">raise</span> <span class="n">CachedRequestError</span><span class="p">()</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">workerFunction</span><span class="p">(</span><span class="o">**</span><span class="n">workerFunctionParams</span><span class="p">)</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a><span class="k">def</span> <span class="nf">make_a_copy_of_cached_request_with_another_keyname</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">current_name</span><span class="p">,</span> <span class="n">new_name</span><span class="p">,</span> <span class="n">make_first_copy_only</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>    <span class="n">is_copy_avaliable</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>    <span class="k">if</span> <span class="n">make_first_copy_only</span><span class="p">:</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        <span class="n">test</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">current_name</span><span class="p">)</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="k">if</span> <span class="n">test</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>            <span class="n">is_copy_avaliable</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    <span class="k">if</span> <span class="n">is_copy_avaliable</span><span class="p">:</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">current_name</span><span class="p">)</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>            <span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">new_name</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a><span class="k">class</span> <span class="nc">SerializableHttpResponseFromRequests</span><span class="p">:</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">isBinaryFile</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">SerializableHttpResponseFromRequests</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">isBinaryFile</span> <span class="o">=</span> <span class="n">isBinaryFile</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">url</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ok</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">ok</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reason</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">reason</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">status_code</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">status_code</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">headers</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">encoding</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>        <span class="k">if</span> <span class="s1">&#39;content&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">content</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>        <span class="c1"># if not isBinaryFile:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>        <span class="c1">#     if &#39;apparent_encoding&#39; in dir(request):</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        <span class="c1">#         self.apparent_encoding = request.apparent_encoding</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>        <span class="c1">#     else:</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="c1">#         self.apparent_encoding = None</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="c1"># else:</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="c1">#     self.apparent_encoding = None</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="c1"># if (self.encoding is not None) or (self.apparent_encoding is not None):</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="c1">#     self.text = request.text</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="c1"># else:</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>        <span class="c1">#     self.text = None</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>    <span class="k">def</span> <span class="nf">getResultEncoding</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>            <span class="k">return</span> <span class="s1">&#39;utf-8&#39;</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>    <span class="k">def</span> <span class="nf">getBytesContent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>            <span class="n">bData</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">getResultEncoding</span><span class="p">())</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>            <span class="k">return</span> <span class="n">bData</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Can&#39;t get data from the request object on url &quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>            <span class="k">raise</span> <span class="ne">Exception</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a><span class="k">def</span> <span class="nf">saveRequestedFileToFS</span><span class="p">(</span><span class="n">folderName</span><span class="p">,</span> <span class="n">requestResult</span><span class="p">):</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">folderName</span> <span class="o">+</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>        <span class="k">if</span> <span class="n">requestResult</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>            <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        <span class="k">elif</span> <span class="n">requestResult</span><span class="o">.</span><span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>            <span class="n">bData</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">requestResult</span><span class="o">.</span><span class="n">getResultEncoding</span><span class="p">())</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>            <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">bData</span><span class="p">)</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>            <span class="n">ex_text</span> <span class="o">=</span> <span class="s2">&quot;Can&#39;t save object from </span><span class="si">{}</span><span class="s2"> to the fie. Can&#39;t get data to save&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>            <span class="nb">print</span><span class="p">(</span><span class="n">ex_text</span><span class="p">)</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="n">ex_text</span><span class="p">)</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a><span class="k">def</span> <span class="nf">getFileModificationDate</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>    <span class="n">t</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getmtime</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>    <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="remove_percent_encoding_from_the_URI">
                            <input id="remove_percent_encoding_from_the_URI-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_percent_encoding_from_the_URI</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">string</span>, </span><span class="param"><span class="n">plus</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="remove_percent_encoding_from_the_URI-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#remove_percent_encoding_from_the_URI"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="remove_percent_encoding_from_the_URI-59"><a href="#remove_percent_encoding_from_the_URI-59"><span class="linenos"> 59</span></a><span class="k">def</span> <span class="nf">remove_percent_encoding_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="n">plus</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="remove_percent_encoding_from_the_URI-60"><a href="#remove_percent_encoding_from_the_URI-60"><span class="linenos"> 60</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-61"><a href="#remove_percent_encoding_from_the_URI-61"><span class="linenos"> 61</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="remove_percent_encoding_from_the_URI-62"><a href="#remove_percent_encoding_from_the_URI-62"><span class="linenos"> 62</span></a>        <span class="k">if</span> <span class="n">plus</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-63"><a href="#remove_percent_encoding_from_the_URI-63"><span class="linenos"> 63</span></a>            <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;+&#39;</span><span class="p">,</span> <span class="s1">&#39; &#39;</span><span class="p">)</span>
</span><span id="remove_percent_encoding_from_the_URI-64"><a href="#remove_percent_encoding_from_the_URI-64"><span class="linenos"> 64</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="remove_percent_encoding_from_the_URI-65"><a href="#remove_percent_encoding_from_the_URI-65"><span class="linenos"> 65</span></a>        <span class="n">percentTypes</span> <span class="o">=</span> <span class="p">((</span><span class="sa">b</span><span class="s1">&#39;</span><span class="si">%u</span><span class="s1">&#39;</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)),</span> <span class="p">(</span><span class="sa">b</span><span class="s1">&#39;%&#39;</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">32</span><span class="p">))</span> <span class="o">+</span> <span class="p">(</span><span class="mi">34</span><span class="p">,</span> <span class="mi">42</span><span class="p">,</span> <span class="mi">58</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span> <span class="mi">62</span><span class="p">,</span> <span class="mi">63</span><span class="p">,</span> <span class="mi">124</span><span class="p">,</span> <span class="mi">127</span><span class="p">))))</span>
</span><span id="remove_percent_encoding_from_the_URI-66"><a href="#remove_percent_encoding_from_the_URI-66"><span class="linenos"> 66</span></a>        <span class="c1"># (prefix, full size, (allowed type or not at all, list of disallowed characters like backspace etc.))</span>
</span><span id="remove_percent_encoding_from_the_URI-67"><a href="#remove_percent_encoding_from_the_URI-67"><span class="linenos"> 67</span></a>        <span class="k">for</span> <span class="n">percType</span> <span class="ow">in</span> <span class="n">percentTypes</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-68"><a href="#remove_percent_encoding_from_the_URI-68"><span class="linenos"> 68</span></a>            <span class="n">isDone</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="remove_percent_encoding_from_the_URI-69"><a href="#remove_percent_encoding_from_the_URI-69"><span class="linenos"> 69</span></a>            <span class="k">while</span> <span class="ow">not</span> <span class="n">isDone</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-70"><a href="#remove_percent_encoding_from_the_URI-70"><span class="linenos"> 70</span></a>                <span class="n">index</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">percType</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="remove_percent_encoding_from_the_URI-71"><a href="#remove_percent_encoding_from_the_URI-71"><span class="linenos"> 71</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-72"><a href="#remove_percent_encoding_from_the_URI-72"><span class="linenos"> 72</span></a>                    <span class="n">ind2</span> <span class="o">=</span> <span class="n">index</span><span class="o">+</span><span class="n">percType</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="remove_percent_encoding_from_the_URI-73"><a href="#remove_percent_encoding_from_the_URI-73"><span class="linenos"> 73</span></a>                    <span class="k">if</span> <span class="n">ind2</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="remove_percent_encoding_from_the_URI-74"><a href="#remove_percent_encoding_from_the_URI-74"><span class="linenos"> 74</span></a>                        <span class="n">ind2</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="remove_percent_encoding_from_the_URI-75"><a href="#remove_percent_encoding_from_the_URI-75"><span class="linenos"> 75</span></a>                    <span class="n">hexString</span> <span class="o">=</span> <span class="n">string</span><span class="p">[</span><span class="n">index</span><span class="p">:</span><span class="n">ind2</span><span class="p">]</span>
</span><span id="remove_percent_encoding_from_the_URI-76"><a href="#remove_percent_encoding_from_the_URI-76"><span class="linenos"> 76</span></a>                    <span class="n">hexString</span> <span class="o">=</span> <span class="n">hexString</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">percType</span><span class="p">[</span><span class="mi">0</span><span class="p">]):]</span>
</span><span id="remove_percent_encoding_from_the_URI-77"><a href="#remove_percent_encoding_from_the_URI-77"><span class="linenos"> 77</span></a>                    <span class="n">decodedString</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="remove_percent_encoding_from_the_URI-78"><a href="#remove_percent_encoding_from_the_URI-78"><span class="linenos"> 78</span></a>                    <span class="k">if</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="remove_percent_encoding_from_the_URI-79"><a href="#remove_percent_encoding_from_the_URI-79"><span class="linenos"> 79</span></a>                        <span class="k">try</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-80"><a href="#remove_percent_encoding_from_the_URI-80"><span class="linenos"> 80</span></a>                            <span class="n">decodedStringBuff</span> <span class="o">=</span> <span class="n">binascii</span><span class="o">.</span><span class="n">unhexlify</span><span class="p">(</span><span class="n">hexString</span><span class="p">)</span>
</span><span id="remove_percent_encoding_from_the_URI-81"><a href="#remove_percent_encoding_from_the_URI-81"><span class="linenos"> 81</span></a>                            <span class="k">if</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">decodedStringBuff</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="remove_percent_encoding_from_the_URI-82"><a href="#remove_percent_encoding_from_the_URI-82"><span class="linenos"> 82</span></a>                                <span class="n">decodedString</span> <span class="o">=</span> <span class="n">decodedStringBuff</span>
</span><span id="remove_percent_encoding_from_the_URI-83"><a href="#remove_percent_encoding_from_the_URI-83"><span class="linenos"> 83</span></a>                        <span class="k">except</span> <span class="n">binascii</span><span class="o">.</span><span class="n">Error</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-84"><a href="#remove_percent_encoding_from_the_URI-84"><span class="linenos"> 84</span></a>                            <span class="k">pass</span>
</span><span id="remove_percent_encoding_from_the_URI-85"><a href="#remove_percent_encoding_from_the_URI-85"><span class="linenos"> 85</span></a>                    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="p">[:</span><span class="n">index</span><span class="p">]</span> <span class="o">+</span> <span class="n">decodedString</span> <span class="o">+</span> <span class="n">string</span><span class="p">[</span><span class="n">ind2</span><span class="p">:]</span>
</span><span id="remove_percent_encoding_from_the_URI-86"><a href="#remove_percent_encoding_from_the_URI-86"><span class="linenos"> 86</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-87"><a href="#remove_percent_encoding_from_the_URI-87"><span class="linenos"> 87</span></a>                    <span class="n">isDone</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="remove_percent_encoding_from_the_URI-88"><a href="#remove_percent_encoding_from_the_URI-88"><span class="linenos"> 88</span></a>            <span class="k">if</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="remove_percent_encoding_from_the_URI-89"><a href="#remove_percent_encoding_from_the_URI-89"><span class="linenos"> 89</span></a>                <span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">string</span><span class="p">)</span><span class="o">.</span><span class="n">intersection</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">])))</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="remove_percent_encoding_from_the_URI-90"><a href="#remove_percent_encoding_from_the_URI-90"><span class="linenos"> 90</span></a>                    <span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="remove_percent_encoding_from_the_URI-91"><a href="#remove_percent_encoding_from_the_URI-91"><span class="linenos"> 91</span></a>                    <span class="n">isDone</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="remove_percent_encoding_from_the_URI-92"><a href="#remove_percent_encoding_from_the_URI-92"><span class="linenos"> 92</span></a>                    <span class="k">while</span> <span class="ow">not</span> <span class="n">isDone</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-93"><a href="#remove_percent_encoding_from_the_URI-93"><span class="linenos"> 93</span></a>                        <span class="k">if</span> <span class="n">string</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="ow">in</span> <span class="n">percType</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="remove_percent_encoding_from_the_URI-94"><a href="#remove_percent_encoding_from_the_URI-94"><span class="linenos"> 94</span></a>                            <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="p">[:</span><span class="n">index</span><span class="p">]</span> <span class="o">+</span> <span class="n">string</span><span class="p">[</span><span class="n">index</span><span class="o">+</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="remove_percent_encoding_from_the_URI-95"><a href="#remove_percent_encoding_from_the_URI-95"><span class="linenos"> 95</span></a>                        <span class="k">else</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-96"><a href="#remove_percent_encoding_from_the_URI-96"><span class="linenos"> 96</span></a>                            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="remove_percent_encoding_from_the_URI-97"><a href="#remove_percent_encoding_from_the_URI-97"><span class="linenos"> 97</span></a>                        <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="remove_percent_encoding_from_the_URI-98"><a href="#remove_percent_encoding_from_the_URI-98"><span class="linenos"> 98</span></a>                            <span class="n">isDone</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="remove_percent_encoding_from_the_URI-99"><a href="#remove_percent_encoding_from_the_URI-99"><span class="linenos"> 99</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="remove_percent_encoding_from_the_URI-100"><a href="#remove_percent_encoding_from_the_URI-100"><span class="linenos">100</span></a>    <span class="k">except</span> <span class="ne">UnicodeDecodeError</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-101"><a href="#remove_percent_encoding_from_the_URI-101"><span class="linenos">101</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="remove_percent_encoding_from_the_URI-102"><a href="#remove_percent_encoding_from_the_URI-102"><span class="linenos">102</span></a>    <span class="k">except</span> <span class="ne">UnicodeEncodeError</span><span class="p">:</span>
</span><span id="remove_percent_encoding_from_the_URI-103"><a href="#remove_percent_encoding_from_the_URI-103"><span class="linenos">103</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="remove_percent_encoding_from_the_URI-104"><a href="#remove_percent_encoding_from_the_URI-104"><span class="linenos">104</span></a>    <span class="k">return</span> <span class="n">string</span>
</span></pre></div>


    

                </section>
                <section id="get_standard_folder_separator">
                            <input id="get_standard_folder_separator-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_standard_folder_separator</span><span class="signature pdoc-code condensed">(<span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_standard_folder_separator-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_standard_folder_separator"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_standard_folder_separator-107"><a href="#get_standard_folder_separator-107"><span class="linenos">107</span></a><span class="k">def</span> <span class="nf">get_standard_folder_separator</span><span class="p">():</span>
</span><span id="get_standard_folder_separator-108"><a href="#get_standard_folder_separator-108"><span class="linenos">108</span></a>    <span class="k">return</span> <span class="s1">&#39;/&#39;</span>
</span></pre></div>


    

                </section>
                <section id="unify_folder_separators">
                            <input id="unify_folder_separators-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unify_folder_separators</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">string</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="unify_folder_separators-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#unify_folder_separators"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="unify_folder_separators-111"><a href="#unify_folder_separators-111"><span class="linenos">111</span></a><span class="k">def</span> <span class="nf">unify_folder_separators</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="unify_folder_separators-112"><a href="#unify_folder_separators-112"><span class="linenos">112</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="unify_folder_separators-113"><a href="#unify_folder_separators-113"><span class="linenos">113</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\\</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">get_standard_folder_separator</span><span class="p">())</span>
</span><span id="unify_folder_separators-114"><a href="#unify_folder_separators-114"><span class="linenos">114</span></a>    <span class="k">return</span> <span class="n">string</span>
</span></pre></div>


    

                </section>
                <section id="remove_forbidden_file_names_from_the_URI">
                            <input id="remove_forbidden_file_names_from_the_URI-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_forbidden_file_names_from_the_URI</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">string</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="remove_forbidden_file_names_from_the_URI-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#remove_forbidden_file_names_from_the_URI"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="remove_forbidden_file_names_from_the_URI-117"><a href="#remove_forbidden_file_names_from_the_URI-117"><span class="linenos">117</span></a><span class="k">def</span> <span class="nf">remove_forbidden_file_names_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="remove_forbidden_file_names_from_the_URI-118"><a href="#remove_forbidden_file_names_from_the_URI-118"><span class="linenos">118</span></a>    <span class="c1"># replace forbidden file names with slash (&#39;/&#39;). Also will unify folder separators (replace &#39;\&#39; with &#39;/&#39;)</span>
</span><span id="remove_forbidden_file_names_from_the_URI-119"><a href="#remove_forbidden_file_names_from_the_URI-119"><span class="linenos">119</span></a>    <span class="n">forbiddenFileNames</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;con&#39;</span><span class="p">,</span> <span class="s1">&#39;prn&#39;</span><span class="p">,</span> <span class="s1">&#39;aux&#39;</span><span class="p">,</span> <span class="s1">&#39;nul&#39;</span><span class="p">,</span> <span class="s1">&#39;com1&#39;</span><span class="p">,</span> <span class="s1">&#39;com2&#39;</span><span class="p">,</span> <span class="s1">&#39;com3&#39;</span><span class="p">,</span> <span class="s1">&#39;com4&#39;</span><span class="p">,</span> <span class="s1">&#39;com5&#39;</span><span class="p">,</span> <span class="s1">&#39;com6&#39;</span><span class="p">,</span> <span class="s1">&#39;com7&#39;</span><span class="p">,</span> <span class="s1">&#39;com8&#39;</span>
</span><span id="remove_forbidden_file_names_from_the_URI-120"><a href="#remove_forbidden_file_names_from_the_URI-120"><span class="linenos">120</span></a>        <span class="p">,</span> <span class="s1">&#39;com9&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt1&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt2&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt3&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt4&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt5&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt6&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt7&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt8&#39;</span><span class="p">,</span> <span class="s1">&#39;lpt9&#39;</span><span class="p">}</span>
</span><span id="remove_forbidden_file_names_from_the_URI-121"><a href="#remove_forbidden_file_names_from_the_URI-121"><span class="linenos">121</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">))</span>
</span><span id="remove_forbidden_file_names_from_the_URI-122"><a href="#remove_forbidden_file_names_from_the_URI-122"><span class="linenos">122</span></a>    <span class="n">strBuffer</span> <span class="o">=</span> <span class="n">string</span>
</span><span id="remove_forbidden_file_names_from_the_URI-123"><a href="#remove_forbidden_file_names_from_the_URI-123"><span class="linenos">123</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
</span><span id="remove_forbidden_file_names_from_the_URI-124"><a href="#remove_forbidden_file_names_from_the_URI-124"><span class="linenos">124</span></a>    <span class="k">for</span> <span class="n">forbFile</span> <span class="ow">in</span> <span class="n">forbiddenFileNames</span><span class="p">:</span>
</span><span id="remove_forbidden_file_names_from_the_URI-125"><a href="#remove_forbidden_file_names_from_the_URI-125"><span class="linenos">125</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">get_standard_folder_separator</span><span class="p">()</span> <span class="o">+</span> <span class="n">forbFile</span> <span class="o">+</span> <span class="n">get_standard_folder_separator</span><span class="p">(),</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="remove_forbidden_file_names_from_the_URI-126"><a href="#remove_forbidden_file_names_from_the_URI-126"><span class="linenos">126</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">get_standard_folder_separator</span><span class="p">()</span> <span class="o">+</span> <span class="n">forbFile</span> <span class="o">+</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="remove_forbidden_file_names_from_the_URI-127"><a href="#remove_forbidden_file_names_from_the_URI-127"><span class="linenos">127</span></a>    <span class="n">isStrWasChanged</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="remove_forbidden_file_names_from_the_URI-128"><a href="#remove_forbidden_file_names_from_the_URI-128"><span class="linenos">128</span></a>    <span class="k">if</span> <span class="n">strBuffer</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">!=</span> <span class="n">string</span><span class="p">:</span>
</span><span id="remove_forbidden_file_names_from_the_URI-129"><a href="#remove_forbidden_file_names_from_the_URI-129"><span class="linenos">129</span></a>        <span class="n">isStrWasChanged</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="remove_forbidden_file_names_from_the_URI-130"><a href="#remove_forbidden_file_names_from_the_URI-130"><span class="linenos">130</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="remove_forbidden_file_names_from_the_URI-131"><a href="#remove_forbidden_file_names_from_the_URI-131"><span class="linenos">131</span></a>        <span class="n">string</span> <span class="o">=</span> <span class="n">strBuffer</span>
</span><span id="remove_forbidden_file_names_from_the_URI-132"><a href="#remove_forbidden_file_names_from_the_URI-132"><span class="linenos">132</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="n">isStrWasChanged</span><span class="p">)</span>
</span><span id="remove_forbidden_file_names_from_the_URI-133"><a href="#remove_forbidden_file_names_from_the_URI-133"><span class="linenos">133</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="remove_path_to_the_parent_of_the_current_directory">
                            <input id="remove_path_to_the_parent_of_the_current_directory-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_path_to_the_parent_of_the_current_directory</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">string</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="remove_path_to_the_parent_of_the_current_directory-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#remove_path_to_the_parent_of_the_current_directory"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="remove_path_to_the_parent_of_the_current_directory-136"><a href="#remove_path_to_the_parent_of_the_current_directory-136"><span class="linenos">136</span></a><span class="k">def</span> <span class="nf">remove_path_to_the_parent_of_the_current_directory</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="remove_path_to_the_parent_of_the_current_directory-137"><a href="#remove_path_to_the_parent_of_the_current_directory-137"><span class="linenos">137</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">string</span><span class="p">))</span>
</span><span id="remove_path_to_the_parent_of_the_current_directory-138"><a href="#remove_path_to_the_parent_of_the_current_directory-138"><span class="linenos">138</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;../&#39;</span><span class="p">,</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="remove_path_to_the_parent_of_the_current_directory-139"><a href="#remove_path_to_the_parent_of_the_current_directory-139"><span class="linenos">139</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;/..&#39;</span><span class="p">,</span> <span class="s1">&#39;/&#39;</span><span class="p">)</span>
</span><span id="remove_path_to_the_parent_of_the_current_directory-140"><a href="#remove_path_to_the_parent_of_the_current_directory-140"><span class="linenos">140</span></a>    <span class="k">return</span> <span class="n">string</span>
</span></pre></div>


    

                </section>
                <section id="is_path_is_trying_to_leave_site_sandbox">
                            <input id="is_path_is_trying_to_leave_site_sandbox-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_path_is_trying_to_leave_site_sandbox</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">string</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_path_is_trying_to_leave_site_sandbox-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_path_is_trying_to_leave_site_sandbox"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_path_is_trying_to_leave_site_sandbox-143"><a href="#is_path_is_trying_to_leave_site_sandbox-143"><span class="linenos">143</span></a><span class="k">def</span> <span class="nf">is_path_is_trying_to_leave_site_sandbox</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-144"><a href="#is_path_is_trying_to_leave_site_sandbox-144"><span class="linenos">144</span></a>    <span class="n">itemsList</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">get_standard_folder_separator</span><span class="p">())</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-145"><a href="#is_path_is_trying_to_leave_site_sandbox-145"><span class="linenos">145</span></a>    <span class="k">while</span> <span class="s1">&#39;&#39;</span> <span class="ow">in</span> <span class="n">itemsList</span><span class="p">:</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-146"><a href="#is_path_is_trying_to_leave_site_sandbox-146"><span class="linenos">146</span></a>        <span class="n">itemsList</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-147"><a href="#is_path_is_trying_to_leave_site_sandbox-147"><span class="linenos">147</span></a>    <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-148"><a href="#is_path_is_trying_to_leave_site_sandbox-148"><span class="linenos">148</span></a>    <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">itemsList</span><span class="p">:</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-149"><a href="#is_path_is_trying_to_leave_site_sandbox-149"><span class="linenos">149</span></a>        <span class="k">if</span> <span class="n">item</span> <span class="o">==</span> <span class="s1">&#39;..&#39;</span><span class="p">:</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-150"><a href="#is_path_is_trying_to_leave_site_sandbox-150"><span class="linenos">150</span></a>            <span class="n">counter</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-151"><a href="#is_path_is_trying_to_leave_site_sandbox-151"><span class="linenos">151</span></a>        <span class="k">elif</span> <span class="n">item</span> <span class="o">==</span> <span class="s1">&#39;.&#39;</span><span class="p">:</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-152"><a href="#is_path_is_trying_to_leave_site_sandbox-152"><span class="linenos">152</span></a>            <span class="k">pass</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-153"><a href="#is_path_is_trying_to_leave_site_sandbox-153"><span class="linenos">153</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-154"><a href="#is_path_is_trying_to_leave_site_sandbox-154"><span class="linenos">154</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-155"><a href="#is_path_is_trying_to_leave_site_sandbox-155"><span class="linenos">155</span></a>        <span class="k">if</span> <span class="n">counter</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-156"><a href="#is_path_is_trying_to_leave_site_sandbox-156"><span class="linenos">156</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="is_path_is_trying_to_leave_site_sandbox-157"><a href="#is_path_is_trying_to_leave_site_sandbox-157"><span class="linenos">157</span></a>    <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                </section>
                <section id="is_path_is_not_safe">
                            <input id="is_path_is_not_safe-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_path_is_not_safe</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">string</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_path_is_not_safe-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_path_is_not_safe"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_path_is_not_safe-160"><a href="#is_path_is_not_safe-160"><span class="linenos">160</span></a><span class="k">def</span> <span class="nf">is_path_is_not_safe</span><span class="p">(</span><span class="n">string</span><span class="p">):</span>
</span><span id="is_path_is_not_safe-161"><a href="#is_path_is_not_safe-161"><span class="linenos">161</span></a>    <span class="c1"># return tuple (decoded string, is_path_is_not_safe)</span>
</span><span id="is_path_is_not_safe-162"><a href="#is_path_is_not_safe-162"><span class="linenos">162</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="is_path_is_not_safe-163"><a href="#is_path_is_not_safe-163"><span class="linenos">163</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">remove_percent_encoding_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="is_path_is_not_safe-164"><a href="#is_path_is_not_safe-164"><span class="linenos">164</span></a>    <span class="k">if</span> <span class="n">string</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="is_path_is_not_safe-165"><a href="#is_path_is_not_safe-165"><span class="linenos">165</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="is_path_is_not_safe-166"><a href="#is_path_is_not_safe-166"><span class="linenos">166</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="is_path_is_not_safe-167"><a href="#is_path_is_not_safe-167"><span class="linenos">167</span></a>    <span class="n">string</span> <span class="o">=</span> <span class="n">remove_forbidden_file_names_from_the_URI</span><span class="p">(</span><span class="n">string</span><span class="p">)</span>
</span><span id="is_path_is_not_safe-168"><a href="#is_path_is_not_safe-168"><span class="linenos">168</span></a>    <span class="k">if</span> <span class="n">string</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="is_path_is_not_safe-169"><a href="#is_path_is_not_safe-169"><span class="linenos">169</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="is_path_is_not_safe-170"><a href="#is_path_is_not_safe-170"><span class="linenos">170</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="is_path_is_not_safe-171"><a href="#is_path_is_not_safe-171"><span class="linenos">171</span></a>    <span class="n">is_not_safe</span> <span class="o">=</span> <span class="n">is_path_is_trying_to_leave_site_sandbox</span><span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="is_path_is_not_safe-172"><a href="#is_path_is_not_safe-172"><span class="linenos">172</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">is_not_safe</span><span class="p">)</span>
</span><span id="is_path_is_not_safe-173"><a href="#is_path_is_not_safe-173"><span class="linenos">173</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="web_server__is_redirection_to_the_main_domain_needed">
                            <input id="web_server__is_redirection_to_the_main_domain_needed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">web_server__is_redirection_to_the_main_domain_needed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">httpParser</span><span class="p">:</span> <span class="n">http_parser</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">HttpParser</span>, </span><span class="param"><span class="n">prefix</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="web_server__is_redirection_to_the_main_domain_needed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#web_server__is_redirection_to_the_main_domain_needed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="web_server__is_redirection_to_the_main_domain_needed-176"><a href="#web_server__is_redirection_to_the_main_domain_needed-176"><span class="linenos">176</span></a><span class="k">def</span> <span class="nf">web_server__is_redirection_to_the_main_domain_needed</span><span class="p">(</span><span class="n">httpParser</span><span class="p">:</span> <span class="n">HttpParser</span><span class="p">,</span> <span class="n">prefix</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-177"><a href="#web_server__is_redirection_to_the_main_domain_needed-177"><span class="linenos">177</span></a>    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-178"><a href="#web_server__is_redirection_to_the_main_domain_needed-178"><span class="linenos">178</span></a>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-179"><a href="#web_server__is_redirection_to_the_main_domain_needed-179"><span class="linenos">179</span></a>    <span class="n">host</span> <span class="o">=</span> <span class="n">httpParser</span><span class="o">.</span><span class="n">get_headers</span><span class="p">()[</span><span class="s1">&#39;Host&#39;</span><span class="p">]</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-180"><a href="#web_server__is_redirection_to_the_main_domain_needed-180"><span class="linenos">180</span></a>    <span class="n">domain</span> <span class="o">=</span> <span class="n">host</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-181"><a href="#web_server__is_redirection_to_the_main_domain_needed-181"><span class="linenos">181</span></a>    <span class="k">if</span> <span class="s1">&#39;:&#39;</span> <span class="ow">in</span> <span class="n">host</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-182"><a href="#web_server__is_redirection_to_the_main_domain_needed-182"><span class="linenos">182</span></a>        <span class="n">host</span> <span class="o">=</span> <span class="n">host</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;:&#39;</span><span class="p">)</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-183"><a href="#web_server__is_redirection_to_the_main_domain_needed-183"><span class="linenos">183</span></a>        <span class="k">while</span> <span class="s1">&#39;&#39;</span> <span class="ow">in</span> <span class="n">host</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-184"><a href="#web_server__is_redirection_to_the_main_domain_needed-184"><span class="linenos">184</span></a>            <span class="n">host</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-185"><a href="#web_server__is_redirection_to_the_main_domain_needed-185"><span class="linenos">185</span></a>        <span class="n">domain</span> <span class="o">=</span> <span class="n">host</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-186"><a href="#web_server__is_redirection_to_the_main_domain_needed-186"><span class="linenos">186</span></a>    <span class="k">if</span> <span class="s1">&#39;.&#39;</span> <span class="ow">in</span> <span class="n">domain</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-187"><a href="#web_server__is_redirection_to_the_main_domain_needed-187"><span class="linenos">187</span></a>        <span class="n">domain</span> <span class="o">=</span> <span class="n">domain</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-188"><a href="#web_server__is_redirection_to_the_main_domain_needed-188"><span class="linenos">188</span></a>        <span class="k">if</span> <span class="n">domain</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;&#39;</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-189"><a href="#web_server__is_redirection_to_the_main_domain_needed-189"><span class="linenos">189</span></a>            <span class="k">del</span> <span class="n">domain</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-190"><a href="#web_server__is_redirection_to_the_main_domain_needed-190"><span class="linenos">190</span></a>            <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-191"><a href="#web_server__is_redirection_to_the_main_domain_needed-191"><span class="linenos">191</span></a>        <span class="k">if</span> <span class="n">prefix</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-192"><a href="#web_server__is_redirection_to_the_main_domain_needed-192"><span class="linenos">192</span></a>            <span class="k">if</span> <span class="n">domain</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="n">prefix</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-193"><a href="#web_server__is_redirection_to_the_main_domain_needed-193"><span class="linenos">193</span></a>                <span class="n">domain</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">prefix</span><span class="p">)</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-194"><a href="#web_server__is_redirection_to_the_main_domain_needed-194"><span class="linenos">194</span></a>                <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-195"><a href="#web_server__is_redirection_to_the_main_domain_needed-195"><span class="linenos">195</span></a>        <span class="n">lastDLen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">domain</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-196"><a href="#web_server__is_redirection_to_the_main_domain_needed-196"><span class="linenos">196</span></a>        <span class="k">if</span> <span class="n">domain</span><span class="p">[</span><span class="n">lastDLen</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;&#39;</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-197"><a href="#web_server__is_redirection_to_the_main_domain_needed-197"><span class="linenos">197</span></a>            <span class="k">del</span> <span class="n">domain</span><span class="p">[</span><span class="n">lastDLen</span><span class="p">]</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-198"><a href="#web_server__is_redirection_to_the_main_domain_needed-198"><span class="linenos">198</span></a>            <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-199"><a href="#web_server__is_redirection_to_the_main_domain_needed-199"><span class="linenos">199</span></a>        <span class="n">domain</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">domain</span><span class="p">)</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-200"><a href="#web_server__is_redirection_to_the_main_domain_needed-200"><span class="linenos">200</span></a>    <span class="k">if</span> <span class="n">host</span><span class="o">.</span><span class="vm">__class__</span> <span class="ow">is</span> <span class="nb">list</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-201"><a href="#web_server__is_redirection_to_the_main_domain_needed-201"><span class="linenos">201</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">host</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-202"><a href="#web_server__is_redirection_to_the_main_domain_needed-202"><span class="linenos">202</span></a>            <span class="n">host</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">domain</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-203"><a href="#web_server__is_redirection_to_the_main_domain_needed-203"><span class="linenos">203</span></a>            <span class="n">domain</span> <span class="o">=</span> <span class="s1">&#39;:&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">host</span><span class="p">)</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-204"><a href="#web_server__is_redirection_to_the_main_domain_needed-204"><span class="linenos">204</span></a>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-205"><a href="#web_server__is_redirection_to_the_main_domain_needed-205"><span class="linenos">205</span></a>    <span class="n">functionResult</span> <span class="o">=</span> <span class="p">(</span><span class="n">functionResult</span><span class="p">,</span> <span class="n">domain</span><span class="p">)</span>
</span><span id="web_server__is_redirection_to_the_main_domain_needed-206"><a href="#web_server__is_redirection_to_the_main_domain_needed-206"><span class="linenos">206</span></a>    <span class="k">return</span> <span class="n">functionResult</span>
</span></pre></div>


    

                </section>
                <section id="load_cache_from_file">
                            <input id="load_cache_from_file-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">load_cache_from_file</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">fileName</span>, </span><span class="param"><span class="n">originalCache</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="load_cache_from_file-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#load_cache_from_file"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="load_cache_from_file-209"><a href="#load_cache_from_file-209"><span class="linenos">209</span></a><span class="k">def</span> <span class="nf">load_cache_from_file</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="n">originalCache</span><span class="p">):</span>
</span><span id="load_cache_from_file-210"><a href="#load_cache_from_file-210"><span class="linenos">210</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="load_cache_from_file-211"><a href="#load_cache_from_file-211"><span class="linenos">211</span></a>    <span class="n">cache</span> <span class="o">=</span> <span class="n">originalCache</span>
</span><span id="load_cache_from_file-212"><a href="#load_cache_from_file-212"><span class="linenos">212</span></a>    <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="load_cache_from_file-213"><a href="#load_cache_from_file-213"><span class="linenos">213</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="load_cache_from_file-214"><a href="#load_cache_from_file-214"><span class="linenos">214</span></a>            <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="load_cache_from_file-215"><a href="#load_cache_from_file-215"><span class="linenos">215</span></a>            <span class="n">dataBuff</span> <span class="o">=</span> <span class="n">originalCache</span>
</span><span id="load_cache_from_file-216"><a href="#load_cache_from_file-216"><span class="linenos">216</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="load_cache_from_file-217"><a href="#load_cache_from_file-217"><span class="linenos">217</span></a>                <span class="c1"># cacheDataFile = open(fileName, &#39;rb&#39;)</span>
</span><span id="load_cache_from_file-218"><a href="#load_cache_from_file-218"><span class="linenos">218</span></a>                <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="n">lzma</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span>
</span><span id="load_cache_from_file-219"><a href="#load_cache_from_file-219"><span class="linenos">219</span></a>                <span class="n">cache</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">cacheDataFile</span><span class="p">)</span>
</span><span id="load_cache_from_file-220"><a href="#load_cache_from_file-220"><span class="linenos">220</span></a>                <span class="n">dataBuff</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">cache</span><span class="p">)</span>
</span><span id="load_cache_from_file-221"><a href="#load_cache_from_file-221"><span class="linenos">221</span></a>                <span class="n">cache</span> <span class="o">=</span> <span class="n">dataBuff</span>
</span><span id="load_cache_from_file-222"><a href="#load_cache_from_file-222"><span class="linenos">222</span></a>            <span class="k">except</span><span class="p">(</span><span class="ne">EnvironmentError</span><span class="p">,</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PicklingError</span><span class="p">)</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
</span><span id="load_cache_from_file-223"><a href="#load_cache_from_file-223"><span class="linenos">223</span></a>                <span class="n">cache</span> <span class="o">=</span> <span class="n">dataBuff</span>
</span><span id="load_cache_from_file-224"><a href="#load_cache_from_file-224"><span class="linenos">224</span></a>            <span class="k">finally</span><span class="p">:</span>
</span><span id="load_cache_from_file-225"><a href="#load_cache_from_file-225"><span class="linenos">225</span></a>                <span class="k">if</span> <span class="n">cacheDataFile</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="load_cache_from_file-226"><a href="#load_cache_from_file-226"><span class="linenos">226</span></a>                    <span class="n">cacheDataFile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="load_cache_from_file-227"><a href="#load_cache_from_file-227"><span class="linenos">227</span></a>    <span class="k">return</span> <span class="n">cache</span>
</span></pre></div>


    

                </section>
                <section id="save_cache_to_file">
                            <input id="save_cache_to_file-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">save_cache_to_file</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">fileName</span>, </span><span class="param"><span class="n">cache</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="save_cache_to_file-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#save_cache_to_file"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="save_cache_to_file-230"><a href="#save_cache_to_file-230"><span class="linenos">230</span></a><span class="k">def</span> <span class="nf">save_cache_to_file</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="n">cache</span><span class="p">):</span>
</span><span id="save_cache_to_file-231"><a href="#save_cache_to_file-231"><span class="linenos">231</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="save_cache_to_file-232"><a href="#save_cache_to_file-232"><span class="linenos">232</span></a>    <span class="k">if</span> <span class="n">cache</span><span class="o">.</span><span class="n">isWasChanged</span><span class="p">:</span>
</span><span id="save_cache_to_file-233"><a href="#save_cache_to_file-233"><span class="linenos">233</span></a>        <span class="n">isRenamedToBak</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="save_cache_to_file-234"><a href="#save_cache_to_file-234"><span class="linenos">234</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="save_cache_to_file-235"><a href="#save_cache_to_file-235"><span class="linenos">235</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="save_cache_to_file-236"><a href="#save_cache_to_file-236"><span class="linenos">236</span></a>                <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">):</span>
</span><span id="save_cache_to_file-237"><a href="#save_cache_to_file-237"><span class="linenos">237</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="save_cache_to_file-238"><a href="#save_cache_to_file-238"><span class="linenos">238</span></a>                        <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">)</span>
</span><span id="save_cache_to_file-239"><a href="#save_cache_to_file-239"><span class="linenos">239</span></a>                    <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span>
</span><span id="save_cache_to_file-240"><a href="#save_cache_to_file-240"><span class="linenos">240</span></a>                        <span class="k">pass</span>
</span><span id="save_cache_to_file-241"><a href="#save_cache_to_file-241"><span class="linenos">241</span></a>                <span class="n">os</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">)</span>
</span><span id="save_cache_to_file-242"><a href="#save_cache_to_file-242"><span class="linenos">242</span></a>                <span class="n">isRenamedToBak</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="save_cache_to_file-243"><a href="#save_cache_to_file-243"><span class="linenos">243</span></a>            <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span>
</span><span id="save_cache_to_file-244"><a href="#save_cache_to_file-244"><span class="linenos">244</span></a>                <span class="k">pass</span>
</span><span id="save_cache_to_file-245"><a href="#save_cache_to_file-245"><span class="linenos">245</span></a>
</span><span id="save_cache_to_file-246"><a href="#save_cache_to_file-246"><span class="linenos">246</span></a>        <span class="n">isDumped</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="save_cache_to_file-247"><a href="#save_cache_to_file-247"><span class="linenos">247</span></a>        <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="save_cache_to_file-248"><a href="#save_cache_to_file-248"><span class="linenos">248</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="save_cache_to_file-249"><a href="#save_cache_to_file-249"><span class="linenos">249</span></a>            <span class="c1"># cacheDataFile = open(fileName, &#39;wb&#39;)</span>
</span><span id="save_cache_to_file-250"><a href="#save_cache_to_file-250"><span class="linenos">250</span></a>            <span class="n">cacheDataFile</span> <span class="o">=</span> <span class="n">lzma</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="n">lzma</span><span class="o">.</span><span class="n">FORMAT_XZ</span><span class="p">,</span> <span class="n">check</span><span class="o">=</span><span class="n">lzma</span><span class="o">.</span><span class="n">CHECK_CRC64</span><span class="p">,</span> <span class="n">preset</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</span><span id="save_cache_to_file-251"><a href="#save_cache_to_file-251"><span class="linenos">251</span></a>            <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">cacheDataFile</span><span class="p">)</span>
</span><span id="save_cache_to_file-252"><a href="#save_cache_to_file-252"><span class="linenos">252</span></a>            <span class="n">cache</span><span class="o">.</span><span class="n">isWasChanged</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="save_cache_to_file-253"><a href="#save_cache_to_file-253"><span class="linenos">253</span></a>            <span class="n">isDumped</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="save_cache_to_file-254"><a href="#save_cache_to_file-254"><span class="linenos">254</span></a>        <span class="k">except</span><span class="p">(</span><span class="ne">EnvironmentError</span><span class="p">,</span> <span class="n">pickle</span><span class="o">.</span><span class="n">PicklingError</span><span class="p">)</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
</span><span id="save_cache_to_file-255"><a href="#save_cache_to_file-255"><span class="linenos">255</span></a>            <span class="k">pass</span>
</span><span id="save_cache_to_file-256"><a href="#save_cache_to_file-256"><span class="linenos">256</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="save_cache_to_file-257"><a href="#save_cache_to_file-257"><span class="linenos">257</span></a>            <span class="k">if</span> <span class="n">cacheDataFile</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="save_cache_to_file-258"><a href="#save_cache_to_file-258"><span class="linenos">258</span></a>                <span class="n">cacheDataFile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="save_cache_to_file-259"><a href="#save_cache_to_file-259"><span class="linenos">259</span></a>
</span><span id="save_cache_to_file-260"><a href="#save_cache_to_file-260"><span class="linenos">260</span></a>        <span class="k">if</span> <span class="n">isRenamedToBak</span> <span class="ow">and</span> <span class="n">isDumped</span><span class="p">:</span>
</span><span id="save_cache_to_file-261"><a href="#save_cache_to_file-261"><span class="linenos">261</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="save_cache_to_file-262"><a href="#save_cache_to_file-262"><span class="linenos">262</span></a>                <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">fileName</span><span class="o">+</span><span class="s1">&#39;.bak&#39;</span><span class="p">)</span>
</span><span id="save_cache_to_file-263"><a href="#save_cache_to_file-263"><span class="linenos">263</span></a>            <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span>
</span><span id="save_cache_to_file-264"><a href="#save_cache_to_file-264"><span class="linenos">264</span></a>                <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="CachedRequestError">
                            <input id="CachedRequestError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CachedRequestError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="CachedRequestError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CachedRequestError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CachedRequestError-267"><a href="#CachedRequestError-267"><span class="linenos">267</span></a><span class="k">class</span> <span class="nc">CachedRequestError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span> <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="CachedRequestError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="CachedRequestError.with_traceback" class="function">with_traceback</dd>
                <dd id="CachedRequestError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="make_cached_request__get">
                            <input id="make_cached_request__get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">make_cached_request__get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">cache</span>, </span><span class="param"><span class="n">request</span>, </span><span class="param"><span class="n">useOnlyCachedResults</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="make_cached_request__get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#make_cached_request__get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="make_cached_request__get-270"><a href="#make_cached_request__get-270"><span class="linenos">270</span></a><span class="k">def</span> <span class="nf">make_cached_request__get</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">useOnlyCachedResults</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="make_cached_request__get-271"><a href="#make_cached_request__get-271"><span class="linenos">271</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="make_cached_request__get-272"><a href="#make_cached_request__get-272"><span class="linenos">272</span></a>    <span class="k">if</span> <span class="p">(</span><span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="ow">not</span> <span class="n">result</span><span class="o">.</span><span class="n">ok</span><span class="p">):</span>
</span><span id="make_cached_request__get-273"><a href="#make_cached_request__get-273"><span class="linenos">273</span></a>        <span class="k">if</span> <span class="n">useOnlyCachedResults</span><span class="p">:</span>
</span><span id="make_cached_request__get-274"><a href="#make_cached_request__get-274"><span class="linenos">274</span></a>            <span class="k">raise</span> <span class="n">CachedRequestError</span><span class="p">()</span>
</span><span id="make_cached_request__get-275"><a href="#make_cached_request__get-275"><span class="linenos">275</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">request</span><span class="p">))</span>
</span><span id="make_cached_request__get-276"><a href="#make_cached_request__get-276"><span class="linenos">276</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">SerializableHttpResponseFromRequests</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="make_cached_request__get-277"><a href="#make_cached_request__get-277"><span class="linenos">277</span></a>        <span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="make_cached_request__get-278"><a href="#make_cached_request__get-278"><span class="linenos">278</span></a>
</span><span id="make_cached_request__get-279"><a href="#make_cached_request__get-279"><span class="linenos">279</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="make_cached_request__universal">
                            <input id="make_cached_request__universal-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">make_cached_request__universal</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">cache</span>,</span><span class="param">	<span class="n">request</span>,</span><span class="param">	<span class="n">workerFunction</span>,</span><span class="param">	<span class="n">useOnlyCachedResults</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="o">**</span><span class="n">workerFunctionParams</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="make_cached_request__universal-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#make_cached_request__universal"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="make_cached_request__universal-282"><a href="#make_cached_request__universal-282"><span class="linenos">282</span></a><span class="k">def</span> <span class="nf">make_cached_request__universal</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">workerFunction</span><span class="p">,</span> <span class="n">useOnlyCachedResults</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">workerFunctionParams</span><span class="p">):</span>
</span><span id="make_cached_request__universal-283"><a href="#make_cached_request__universal-283"><span class="linenos">283</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="make_cached_request__universal-284"><a href="#make_cached_request__universal-284"><span class="linenos">284</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="make_cached_request__universal-285"><a href="#make_cached_request__universal-285"><span class="linenos">285</span></a>        <span class="k">if</span> <span class="n">useOnlyCachedResults</span><span class="p">:</span>
</span><span id="make_cached_request__universal-286"><a href="#make_cached_request__universal-286"><span class="linenos">286</span></a>            <span class="k">raise</span> <span class="n">CachedRequestError</span><span class="p">()</span>
</span><span id="make_cached_request__universal-287"><a href="#make_cached_request__universal-287"><span class="linenos">287</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">workerFunction</span><span class="p">(</span><span class="o">**</span><span class="n">workerFunctionParams</span><span class="p">)</span>
</span><span id="make_cached_request__universal-288"><a href="#make_cached_request__universal-288"><span class="linenos">288</span></a>        <span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="make_cached_request__universal-289"><a href="#make_cached_request__universal-289"><span class="linenos">289</span></a>
</span><span id="make_cached_request__universal-290"><a href="#make_cached_request__universal-290"><span class="linenos">290</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="make_a_copy_of_cached_request_with_another_keyname">
                            <input id="make_a_copy_of_cached_request_with_another_keyname-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">make_a_copy_of_cached_request_with_another_keyname</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">cache</span>, </span><span class="param"><span class="n">current_name</span>, </span><span class="param"><span class="n">new_name</span>, </span><span class="param"><span class="n">make_first_copy_only</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="make_a_copy_of_cached_request_with_another_keyname-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#make_a_copy_of_cached_request_with_another_keyname"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="make_a_copy_of_cached_request_with_another_keyname-293"><a href="#make_a_copy_of_cached_request_with_another_keyname-293"><span class="linenos">293</span></a><span class="k">def</span> <span class="nf">make_a_copy_of_cached_request_with_another_keyname</span><span class="p">(</span><span class="n">cache</span><span class="p">,</span> <span class="n">current_name</span><span class="p">,</span> <span class="n">new_name</span><span class="p">,</span> <span class="n">make_first_copy_only</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-294"><a href="#make_a_copy_of_cached_request_with_another_keyname-294"><span class="linenos">294</span></a>    <span class="n">is_copy_avaliable</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-295"><a href="#make_a_copy_of_cached_request_with_another_keyname-295"><span class="linenos">295</span></a>    <span class="k">if</span> <span class="n">make_first_copy_only</span><span class="p">:</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-296"><a href="#make_a_copy_of_cached_request_with_another_keyname-296"><span class="linenos">296</span></a>        <span class="n">test</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">current_name</span><span class="p">)</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-297"><a href="#make_a_copy_of_cached_request_with_another_keyname-297"><span class="linenos">297</span></a>        <span class="k">if</span> <span class="n">test</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-298"><a href="#make_a_copy_of_cached_request_with_another_keyname-298"><span class="linenos">298</span></a>            <span class="n">is_copy_avaliable</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-299"><a href="#make_a_copy_of_cached_request_with_another_keyname-299"><span class="linenos">299</span></a>    <span class="k">if</span> <span class="n">is_copy_avaliable</span><span class="p">:</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-300"><a href="#make_a_copy_of_cached_request_with_another_keyname-300"><span class="linenos">300</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">current_name</span><span class="p">)</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-301"><a href="#make_a_copy_of_cached_request_with_another_keyname-301"><span class="linenos">301</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="make_a_copy_of_cached_request_with_another_keyname-302"><a href="#make_a_copy_of_cached_request_with_another_keyname-302"><span class="linenos">302</span></a>            <span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">new_name</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="SerializableHttpResponseFromRequests">
                            <input id="SerializableHttpResponseFromRequests-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SerializableHttpResponseFromRequests</span>:

                <label class="view-source-button" for="SerializableHttpResponseFromRequests-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SerializableHttpResponseFromRequests-305"><a href="#SerializableHttpResponseFromRequests-305"><span class="linenos">305</span></a><span class="k">class</span> <span class="nc">SerializableHttpResponseFromRequests</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-306"><a href="#SerializableHttpResponseFromRequests-306"><span class="linenos">306</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">isBinaryFile</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests-307"><a href="#SerializableHttpResponseFromRequests-307"><span class="linenos">307</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">SerializableHttpResponseFromRequests</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="SerializableHttpResponseFromRequests-308"><a href="#SerializableHttpResponseFromRequests-308"><span class="linenos">308</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">isBinaryFile</span> <span class="o">=</span> <span class="n">isBinaryFile</span>
</span><span id="SerializableHttpResponseFromRequests-309"><a href="#SerializableHttpResponseFromRequests-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">url</span>
</span><span id="SerializableHttpResponseFromRequests-310"><a href="#SerializableHttpResponseFromRequests-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ok</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">ok</span>
</span><span id="SerializableHttpResponseFromRequests-311"><a href="#SerializableHttpResponseFromRequests-311"><span class="linenos">311</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reason</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">reason</span>
</span><span id="SerializableHttpResponseFromRequests-312"><a href="#SerializableHttpResponseFromRequests-312"><span class="linenos">312</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">status_code</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">status_code</span>
</span><span id="SerializableHttpResponseFromRequests-313"><a href="#SerializableHttpResponseFromRequests-313"><span class="linenos">313</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">headers</span>
</span><span id="SerializableHttpResponseFromRequests-314"><a href="#SerializableHttpResponseFromRequests-314"><span class="linenos">314</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">encoding</span>
</span><span id="SerializableHttpResponseFromRequests-315"><a href="#SerializableHttpResponseFromRequests-315"><span class="linenos">315</span></a>
</span><span id="SerializableHttpResponseFromRequests-316"><a href="#SerializableHttpResponseFromRequests-316"><span class="linenos">316</span></a>        <span class="k">if</span> <span class="s1">&#39;content&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests-317"><a href="#SerializableHttpResponseFromRequests-317"><span class="linenos">317</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">content</span>
</span><span id="SerializableHttpResponseFromRequests-318"><a href="#SerializableHttpResponseFromRequests-318"><span class="linenos">318</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-319"><a href="#SerializableHttpResponseFromRequests-319"><span class="linenos">319</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SerializableHttpResponseFromRequests-320"><a href="#SerializableHttpResponseFromRequests-320"><span class="linenos">320</span></a>
</span><span id="SerializableHttpResponseFromRequests-321"><a href="#SerializableHttpResponseFromRequests-321"><span class="linenos">321</span></a>        <span class="c1"># if not isBinaryFile:</span>
</span><span id="SerializableHttpResponseFromRequests-322"><a href="#SerializableHttpResponseFromRequests-322"><span class="linenos">322</span></a>        <span class="c1">#     if &#39;apparent_encoding&#39; in dir(request):</span>
</span><span id="SerializableHttpResponseFromRequests-323"><a href="#SerializableHttpResponseFromRequests-323"><span class="linenos">323</span></a>        <span class="c1">#         self.apparent_encoding = request.apparent_encoding</span>
</span><span id="SerializableHttpResponseFromRequests-324"><a href="#SerializableHttpResponseFromRequests-324"><span class="linenos">324</span></a>        <span class="c1">#     else:</span>
</span><span id="SerializableHttpResponseFromRequests-325"><a href="#SerializableHttpResponseFromRequests-325"><span class="linenos">325</span></a>        <span class="c1">#         self.apparent_encoding = None</span>
</span><span id="SerializableHttpResponseFromRequests-326"><a href="#SerializableHttpResponseFromRequests-326"><span class="linenos">326</span></a>        <span class="c1"># else:</span>
</span><span id="SerializableHttpResponseFromRequests-327"><a href="#SerializableHttpResponseFromRequests-327"><span class="linenos">327</span></a>        <span class="c1">#     self.apparent_encoding = None</span>
</span><span id="SerializableHttpResponseFromRequests-328"><a href="#SerializableHttpResponseFromRequests-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SerializableHttpResponseFromRequests-329"><a href="#SerializableHttpResponseFromRequests-329"><span class="linenos">329</span></a>
</span><span id="SerializableHttpResponseFromRequests-330"><a href="#SerializableHttpResponseFromRequests-330"><span class="linenos">330</span></a>        <span class="c1"># if (self.encoding is not None) or (self.apparent_encoding is not None):</span>
</span><span id="SerializableHttpResponseFromRequests-331"><a href="#SerializableHttpResponseFromRequests-331"><span class="linenos">331</span></a>        <span class="c1">#     self.text = request.text</span>
</span><span id="SerializableHttpResponseFromRequests-332"><a href="#SerializableHttpResponseFromRequests-332"><span class="linenos">332</span></a>        <span class="c1"># else:</span>
</span><span id="SerializableHttpResponseFromRequests-333"><a href="#SerializableHttpResponseFromRequests-333"><span class="linenos">333</span></a>        <span class="c1">#     self.text = None</span>
</span><span id="SerializableHttpResponseFromRequests-334"><a href="#SerializableHttpResponseFromRequests-334"><span class="linenos">334</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SerializableHttpResponseFromRequests-335"><a href="#SerializableHttpResponseFromRequests-335"><span class="linenos">335</span></a>
</span><span id="SerializableHttpResponseFromRequests-336"><a href="#SerializableHttpResponseFromRequests-336"><span class="linenos">336</span></a>    <span class="k">def</span> <span class="nf">getResultEncoding</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests-337"><a href="#SerializableHttpResponseFromRequests-337"><span class="linenos">337</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-338"><a href="#SerializableHttpResponseFromRequests-338"><span class="linenos">338</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span>
</span><span id="SerializableHttpResponseFromRequests-339"><a href="#SerializableHttpResponseFromRequests-339"><span class="linenos">339</span></a>        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-340"><a href="#SerializableHttpResponseFromRequests-340"><span class="linenos">340</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span>
</span><span id="SerializableHttpResponseFromRequests-341"><a href="#SerializableHttpResponseFromRequests-341"><span class="linenos">341</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-342"><a href="#SerializableHttpResponseFromRequests-342"><span class="linenos">342</span></a>            <span class="k">return</span> <span class="s1">&#39;utf-8&#39;</span>
</span><span id="SerializableHttpResponseFromRequests-343"><a href="#SerializableHttpResponseFromRequests-343"><span class="linenos">343</span></a>
</span><span id="SerializableHttpResponseFromRequests-344"><a href="#SerializableHttpResponseFromRequests-344"><span class="linenos">344</span></a>    <span class="k">def</span> <span class="nf">getBytesContent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests-345"><a href="#SerializableHttpResponseFromRequests-345"><span class="linenos">345</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-346"><a href="#SerializableHttpResponseFromRequests-346"><span class="linenos">346</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
</span><span id="SerializableHttpResponseFromRequests-347"><a href="#SerializableHttpResponseFromRequests-347"><span class="linenos">347</span></a>        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-348"><a href="#SerializableHttpResponseFromRequests-348"><span class="linenos">348</span></a>            <span class="n">bData</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">getResultEncoding</span><span class="p">())</span>
</span><span id="SerializableHttpResponseFromRequests-349"><a href="#SerializableHttpResponseFromRequests-349"><span class="linenos">349</span></a>            <span class="k">return</span> <span class="n">bData</span>
</span><span id="SerializableHttpResponseFromRequests-350"><a href="#SerializableHttpResponseFromRequests-350"><span class="linenos">350</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests-351"><a href="#SerializableHttpResponseFromRequests-351"><span class="linenos">351</span></a>            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Can&#39;t get data from the request object on url &quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
</span><span id="SerializableHttpResponseFromRequests-352"><a href="#SerializableHttpResponseFromRequests-352"><span class="linenos">352</span></a>            <span class="k">raise</span> <span class="ne">Exception</span>
</span></pre></div>


    

                            <div id="SerializableHttpResponseFromRequests.__init__" class="classattr">
                                        <input id="SerializableHttpResponseFromRequests.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">SerializableHttpResponseFromRequests</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">request</span>, </span><span class="param"><span class="n">isBinaryFile</span><span class="o">=</span><span class="kc">False</span></span>)</span>

                <label class="view-source-button" for="SerializableHttpResponseFromRequests.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SerializableHttpResponseFromRequests.__init__-306"><a href="#SerializableHttpResponseFromRequests.__init__-306"><span class="linenos">306</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">isBinaryFile</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-307"><a href="#SerializableHttpResponseFromRequests.__init__-307"><span class="linenos">307</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">SerializableHttpResponseFromRequests</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-308"><a href="#SerializableHttpResponseFromRequests.__init__-308"><span class="linenos">308</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">isBinaryFile</span> <span class="o">=</span> <span class="n">isBinaryFile</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-309"><a href="#SerializableHttpResponseFromRequests.__init__-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">url</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-310"><a href="#SerializableHttpResponseFromRequests.__init__-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ok</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">ok</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-311"><a href="#SerializableHttpResponseFromRequests.__init__-311"><span class="linenos">311</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reason</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">reason</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-312"><a href="#SerializableHttpResponseFromRequests.__init__-312"><span class="linenos">312</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">status_code</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">status_code</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-313"><a href="#SerializableHttpResponseFromRequests.__init__-313"><span class="linenos">313</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">headers</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-314"><a href="#SerializableHttpResponseFromRequests.__init__-314"><span class="linenos">314</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">encoding</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-315"><a href="#SerializableHttpResponseFromRequests.__init__-315"><span class="linenos">315</span></a>
</span><span id="SerializableHttpResponseFromRequests.__init__-316"><a href="#SerializableHttpResponseFromRequests.__init__-316"><span class="linenos">316</span></a>        <span class="k">if</span> <span class="s1">&#39;content&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-317"><a href="#SerializableHttpResponseFromRequests.__init__-317"><span class="linenos">317</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">content</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-318"><a href="#SerializableHttpResponseFromRequests.__init__-318"><span class="linenos">318</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-319"><a href="#SerializableHttpResponseFromRequests.__init__-319"><span class="linenos">319</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-320"><a href="#SerializableHttpResponseFromRequests.__init__-320"><span class="linenos">320</span></a>
</span><span id="SerializableHttpResponseFromRequests.__init__-321"><a href="#SerializableHttpResponseFromRequests.__init__-321"><span class="linenos">321</span></a>        <span class="c1"># if not isBinaryFile:</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-322"><a href="#SerializableHttpResponseFromRequests.__init__-322"><span class="linenos">322</span></a>        <span class="c1">#     if &#39;apparent_encoding&#39; in dir(request):</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-323"><a href="#SerializableHttpResponseFromRequests.__init__-323"><span class="linenos">323</span></a>        <span class="c1">#         self.apparent_encoding = request.apparent_encoding</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-324"><a href="#SerializableHttpResponseFromRequests.__init__-324"><span class="linenos">324</span></a>        <span class="c1">#     else:</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-325"><a href="#SerializableHttpResponseFromRequests.__init__-325"><span class="linenos">325</span></a>        <span class="c1">#         self.apparent_encoding = None</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-326"><a href="#SerializableHttpResponseFromRequests.__init__-326"><span class="linenos">326</span></a>        <span class="c1"># else:</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-327"><a href="#SerializableHttpResponseFromRequests.__init__-327"><span class="linenos">327</span></a>        <span class="c1">#     self.apparent_encoding = None</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-328"><a href="#SerializableHttpResponseFromRequests.__init__-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-329"><a href="#SerializableHttpResponseFromRequests.__init__-329"><span class="linenos">329</span></a>
</span><span id="SerializableHttpResponseFromRequests.__init__-330"><a href="#SerializableHttpResponseFromRequests.__init__-330"><span class="linenos">330</span></a>        <span class="c1"># if (self.encoding is not None) or (self.apparent_encoding is not None):</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-331"><a href="#SerializableHttpResponseFromRequests.__init__-331"><span class="linenos">331</span></a>        <span class="c1">#     self.text = request.text</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-332"><a href="#SerializableHttpResponseFromRequests.__init__-332"><span class="linenos">332</span></a>        <span class="c1"># else:</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-333"><a href="#SerializableHttpResponseFromRequests.__init__-333"><span class="linenos">333</span></a>        <span class="c1">#     self.text = None</span>
</span><span id="SerializableHttpResponseFromRequests.__init__-334"><a href="#SerializableHttpResponseFromRequests.__init__-334"><span class="linenos">334</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.isBinaryFile" class="classattr">
                                <div class="attr variable">
            <span class="name">isBinaryFile</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.isBinaryFile"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.url" class="classattr">
                                <div class="attr variable">
            <span class="name">url</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.url"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.ok" class="classattr">
                                <div class="attr variable">
            <span class="name">ok</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.ok"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.reason" class="classattr">
                                <div class="attr variable">
            <span class="name">reason</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.reason"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.status_code" class="classattr">
                                <div class="attr variable">
            <span class="name">status_code</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.status_code"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.headers" class="classattr">
                                <div class="attr variable">
            <span class="name">headers</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.headers"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.encoding" class="classattr">
                                <div class="attr variable">
            <span class="name">encoding</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.encoding"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.apparent_encoding" class="classattr">
                                <div class="attr variable">
            <span class="name">apparent_encoding</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.apparent_encoding"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.text" class="classattr">
                                <div class="attr variable">
            <span class="name">text</span>

        
    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.text"></a>
    
    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.getResultEncoding" class="classattr">
                                        <input id="SerializableHttpResponseFromRequests.getResultEncoding-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">getResultEncoding</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SerializableHttpResponseFromRequests.getResultEncoding-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.getResultEncoding"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SerializableHttpResponseFromRequests.getResultEncoding-336"><a href="#SerializableHttpResponseFromRequests.getResultEncoding-336"><span class="linenos">336</span></a>    <span class="k">def</span> <span class="nf">getResultEncoding</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests.getResultEncoding-337"><a href="#SerializableHttpResponseFromRequests.getResultEncoding-337"><span class="linenos">337</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests.getResultEncoding-338"><a href="#SerializableHttpResponseFromRequests.getResultEncoding-338"><span class="linenos">338</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span>
</span><span id="SerializableHttpResponseFromRequests.getResultEncoding-339"><a href="#SerializableHttpResponseFromRequests.getResultEncoding-339"><span class="linenos">339</span></a>        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests.getResultEncoding-340"><a href="#SerializableHttpResponseFromRequests.getResultEncoding-340"><span class="linenos">340</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">apparent_encoding</span>
</span><span id="SerializableHttpResponseFromRequests.getResultEncoding-341"><a href="#SerializableHttpResponseFromRequests.getResultEncoding-341"><span class="linenos">341</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests.getResultEncoding-342"><a href="#SerializableHttpResponseFromRequests.getResultEncoding-342"><span class="linenos">342</span></a>            <span class="k">return</span> <span class="s1">&#39;utf-8&#39;</span>
</span></pre></div>


    

                            </div>
                            <div id="SerializableHttpResponseFromRequests.getBytesContent" class="classattr">
                                        <input id="SerializableHttpResponseFromRequests.getBytesContent-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">getBytesContent</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SerializableHttpResponseFromRequests.getBytesContent-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SerializableHttpResponseFromRequests.getBytesContent"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SerializableHttpResponseFromRequests.getBytesContent-344"><a href="#SerializableHttpResponseFromRequests.getBytesContent-344"><span class="linenos">344</span></a>    <span class="k">def</span> <span class="nf">getBytesContent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-345"><a href="#SerializableHttpResponseFromRequests.getBytesContent-345"><span class="linenos">345</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-346"><a href="#SerializableHttpResponseFromRequests.getBytesContent-346"><span class="linenos">346</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">content</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-347"><a href="#SerializableHttpResponseFromRequests.getBytesContent-347"><span class="linenos">347</span></a>        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-348"><a href="#SerializableHttpResponseFromRequests.getBytesContent-348"><span class="linenos">348</span></a>            <span class="n">bData</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">getResultEncoding</span><span class="p">())</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-349"><a href="#SerializableHttpResponseFromRequests.getBytesContent-349"><span class="linenos">349</span></a>            <span class="k">return</span> <span class="n">bData</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-350"><a href="#SerializableHttpResponseFromRequests.getBytesContent-350"><span class="linenos">350</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-351"><a href="#SerializableHttpResponseFromRequests.getBytesContent-351"><span class="linenos">351</span></a>            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Can&#39;t get data from the request object on url &quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
</span><span id="SerializableHttpResponseFromRequests.getBytesContent-352"><a href="#SerializableHttpResponseFromRequests.getBytesContent-352"><span class="linenos">352</span></a>            <span class="k">raise</span> <span class="ne">Exception</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="saveRequestedFileToFS">
                            <input id="saveRequestedFileToFS-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">saveRequestedFileToFS</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">folderName</span>, </span><span class="param"><span class="n">requestResult</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="saveRequestedFileToFS-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#saveRequestedFileToFS"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="saveRequestedFileToFS-355"><a href="#saveRequestedFileToFS-355"><span class="linenos">355</span></a><span class="k">def</span> <span class="nf">saveRequestedFileToFS</span><span class="p">(</span><span class="n">folderName</span><span class="p">,</span> <span class="n">requestResult</span><span class="p">):</span>
</span><span id="saveRequestedFileToFS-356"><a href="#saveRequestedFileToFS-356"><span class="linenos">356</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">folderName</span> <span class="o">+</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
</span><span id="saveRequestedFileToFS-357"><a href="#saveRequestedFileToFS-357"><span class="linenos">357</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="saveRequestedFileToFS-358"><a href="#saveRequestedFileToFS-358"><span class="linenos">358</span></a>    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">fileName</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="saveRequestedFileToFS-359"><a href="#saveRequestedFileToFS-359"><span class="linenos">359</span></a>        <span class="k">if</span> <span class="n">requestResult</span><span class="o">.</span><span class="n">content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="saveRequestedFileToFS-360"><a href="#saveRequestedFileToFS-360"><span class="linenos">360</span></a>            <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
</span><span id="saveRequestedFileToFS-361"><a href="#saveRequestedFileToFS-361"><span class="linenos">361</span></a>        <span class="k">elif</span> <span class="n">requestResult</span><span class="o">.</span><span class="n">text</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="saveRequestedFileToFS-362"><a href="#saveRequestedFileToFS-362"><span class="linenos">362</span></a>            <span class="n">bData</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">requestResult</span><span class="o">.</span><span class="n">getResultEncoding</span><span class="p">())</span>
</span><span id="saveRequestedFileToFS-363"><a href="#saveRequestedFileToFS-363"><span class="linenos">363</span></a>            <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">bData</span><span class="p">)</span>
</span><span id="saveRequestedFileToFS-364"><a href="#saveRequestedFileToFS-364"><span class="linenos">364</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="saveRequestedFileToFS-365"><a href="#saveRequestedFileToFS-365"><span class="linenos">365</span></a>            <span class="n">ex_text</span> <span class="o">=</span> <span class="s2">&quot;Can&#39;t save object from </span><span class="si">{}</span><span class="s2"> to the fie. Can&#39;t get data to save&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">requestResult</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
</span><span id="saveRequestedFileToFS-366"><a href="#saveRequestedFileToFS-366"><span class="linenos">366</span></a>            <span class="nb">print</span><span class="p">(</span><span class="n">ex_text</span><span class="p">)</span>
</span><span id="saveRequestedFileToFS-367"><a href="#saveRequestedFileToFS-367"><span class="linenos">367</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="n">ex_text</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="getFileModificationDate">
                            <input id="getFileModificationDate-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">getFileModificationDate</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">fileName</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="getFileModificationDate-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#getFileModificationDate"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="getFileModificationDate-370"><a href="#getFileModificationDate-370"><span class="linenos">370</span></a><span class="k">def</span> <span class="nf">getFileModificationDate</span><span class="p">(</span><span class="n">fileName</span><span class="p">):</span>
</span><span id="getFileModificationDate-371"><a href="#getFileModificationDate-371"><span class="linenos">371</span></a>    <span class="n">fileName</span> <span class="o">=</span> <span class="n">unify_folder_separators</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="getFileModificationDate-372"><a href="#getFileModificationDate-372"><span class="linenos">372</span></a>    <span class="n">t</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getmtime</span><span class="p">(</span><span class="n">fileName</span><span class="p">)</span>
</span><span id="getFileModificationDate-373"><a href="#getFileModificationDate-373"><span class="linenos">373</span></a>    <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>