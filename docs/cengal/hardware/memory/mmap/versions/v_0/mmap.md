---
title: mmap
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.hardware<wbr>.memory<wbr>.mmap<wbr>.versions<wbr>.v_0<wbr>.mmap    </h1>

                
                        <input id="mod-mmap-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-mmap-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos">19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;SmartMap&#39;</span><span class="p">]</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos">20</span></a>
</span><span id="L-21"><a href="#L-21"><span class="linenos">21</span></a>
</span><span id="L-22"><a href="#L-22"><span class="linenos">22</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos">23</span></a><span class="sd">Module Docstring</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos">24</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos">25</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos">26</span></a>
</span><span id="L-27"><a href="#L-27"><span class="linenos">27</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos">28</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos">29</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos">30</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos">31</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos">32</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos">33</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos">34</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos">35</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos">36</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos">37</span></a>
</span><span id="L-38"><a href="#L-38"><span class="linenos">38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos">39</span></a><span class="kn">import</span> <span class="nn">os</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos">40</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos">41</span></a><span class="kn">import</span> <span class="nn">mmap</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos">42</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos">43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos">44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos">45</span></a><span class="k">class</span> <span class="nc">SmartMap</span><span class="p">:</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos">46</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos">47</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pagesize</span> <span class="o">=</span> <span class="n">mmap</span><span class="o">.</span><span class="n">PAGESIZE</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos">48</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_mswindows</span> <span class="o">=</span> <span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;win32&quot;</span><span class="p">)</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos">49</span></a>        <span class="k">pass</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos">50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos">51</span></a>    <span class="k">def</span> <span class="nf">flush</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos">52</span></a>        <span class="k">pass</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos">53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos">54</span></a>    <span class="k">def</span> <span class="nf">generate_temp_file_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">str</span><span class="p">:</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos">55</span></a>        <span class="k">pass</span>
</span></pre></div>


            </section>
                <section id="SmartMap">
                            <input id="SmartMap-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SmartMap</span>:

                <label class="view-source-button" for="SmartMap-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SmartMap"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SmartMap-46"><a href="#SmartMap-46"><span class="linenos">46</span></a><span class="k">class</span> <span class="nc">SmartMap</span><span class="p">:</span>
</span><span id="SmartMap-47"><a href="#SmartMap-47"><span class="linenos">47</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SmartMap-48"><a href="#SmartMap-48"><span class="linenos">48</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pagesize</span> <span class="o">=</span> <span class="n">mmap</span><span class="o">.</span><span class="n">PAGESIZE</span>
</span><span id="SmartMap-49"><a href="#SmartMap-49"><span class="linenos">49</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_mswindows</span> <span class="o">=</span> <span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;win32&quot;</span><span class="p">)</span>
</span><span id="SmartMap-50"><a href="#SmartMap-50"><span class="linenos">50</span></a>        <span class="k">pass</span>
</span><span id="SmartMap-51"><a href="#SmartMap-51"><span class="linenos">51</span></a>
</span><span id="SmartMap-52"><a href="#SmartMap-52"><span class="linenos">52</span></a>    <span class="k">def</span> <span class="nf">flush</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SmartMap-53"><a href="#SmartMap-53"><span class="linenos">53</span></a>        <span class="k">pass</span>
</span><span id="SmartMap-54"><a href="#SmartMap-54"><span class="linenos">54</span></a>
</span><span id="SmartMap-55"><a href="#SmartMap-55"><span class="linenos">55</span></a>    <span class="k">def</span> <span class="nf">generate_temp_file_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">str</span><span class="p">:</span>
</span><span id="SmartMap-56"><a href="#SmartMap-56"><span class="linenos">56</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            <div id="SmartMap.pagesize" class="classattr">
                                <div class="attr variable">
            <span class="name">pagesize</span>

        
    </div>
    <a class="headerlink" href="#SmartMap.pagesize"></a>
    
    

                            </div>
                            <div id="SmartMap.is_mswindows" class="classattr">
                                <div class="attr variable">
            <span class="name">is_mswindows</span>

        
    </div>
    <a class="headerlink" href="#SmartMap.is_mswindows"></a>
    
    

                            </div>
                            <div id="SmartMap.flush" class="classattr">
                                        <input id="SmartMap.flush-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">flush</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SmartMap.flush-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SmartMap.flush"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SmartMap.flush-52"><a href="#SmartMap.flush-52"><span class="linenos">52</span></a>    <span class="k">def</span> <span class="nf">flush</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SmartMap.flush-53"><a href="#SmartMap.flush-53"><span class="linenos">53</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="SmartMap.generate_temp_file_name" class="classattr">
                                        <input id="SmartMap.generate_temp_file_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">generate_temp_file_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="SmartMap.generate_temp_file_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SmartMap.generate_temp_file_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SmartMap.generate_temp_file_name-55"><a href="#SmartMap.generate_temp_file_name-55"><span class="linenos">55</span></a>    <span class="k">def</span> <span class="nf">generate_temp_file_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">str</span><span class="p">:</span>
</span><span id="SmartMap.generate_temp_file_name-56"><a href="#SmartMap.generate_temp_file_name-56"><span class="linenos">56</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>