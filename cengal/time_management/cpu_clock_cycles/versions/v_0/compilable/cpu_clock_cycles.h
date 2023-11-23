// Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


#ifndef RDTSCP_H
#define RDTSCP_H

#if defined(IS_X86)

unsigned long long c_cpu_clock_cycles();

#elif defined(IS_ARM)

unsigned u64 c_cpu_clock_cycles();

#else

unsigned long long c_cpu_clock_cycles();

#endif

#endif
