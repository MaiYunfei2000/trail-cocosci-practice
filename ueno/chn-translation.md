- Ueno, T., Saito, S., Rogers, T. T., & Lambon Ralph, M. A. (2011). Lichtheim 2: Synthesizing Aphasia and the Neural Basis of Language in a Neurocomputational Model of the Dual Dorsal-Ventral Language Pathways. Neuron, 72(2), 385–396. https://doi.org/10.1016/j.neuron.2011.09.013

⚠️神经解剖学术语需要在整理知识清单（若进行这种整理）时再次对照生理心理学及认知神经科学课本进行交叉验证。

# Lichtheim 2：双背腹语言通路的神经计算模型——合成性失语症与语言的神经基础

## SUMMARY

传统的语言的神经模型基于单神经通路 (single neural pathway) （由弓状束 (arcuate fasciculus) 支撑的背侧通路 (dorsal pathway)）。当代神经科学指出，前颞叶区域 (anterior temporal regions) 以及“腹侧”语言通路 ("ventral" language pathway) 也有显著的贡献，然而尚未有双通路的计算模型 (computationally-implemented model) ，或是任何正常及失语行为的综合 (synthesis of normal and aphasic behavior) 。“Lichtheim 2”模型是通过开发一类新的计算模型来实现的，这类模型产生和解释正常人及患者的数据，也将神经解剖学的 (neuroanatomical) 信息纳入其结构。通过建立心智与脑之间的gap的桥梁，作为结果的神经计算模型提供了一个独特的机，会去探索损伤区域与行为缺陷之间的关系，以及为功能性神经影像数据 (functional neuroimaging) 的仿真提供了一个平台。

## INTRODUCTION

19世纪的神经学家先驱证明，语言能力是由皮质区域一个分布式的网络来支持的。Lichtheim (1885) 将这些思想吸收为一个模型，此模型涉及到左半球的外侧裂 (perisylvian) 和前额叶 (prefrontal) 区域，并指出它们相互交流以产生语言功能。Lichtheim 的模型解释了脑损伤带来的语言损坏的主要形式，解释了为什么不同脑区的损伤会产生不同的失语综合征。在这个模型被提出的125年之后，Lichtheim 的模型仍然是众多研究者和临床医生考虑语言的神经基础及其病理学时的主要组织架构。

尽管它具有可观的和长期的成功，早期的批评者指出，此理论缺乏关于不同皮质区域计算出的功能的特异性。近期比较明显的是，需要纳入大量信息，包括有关语言系统的功能的及结构解剖的当代神经科学数据。本论文提出了一个新的关于语言的神经计算模型，它与Lichtheim的模型一脉相承，但结合了有关语言的结构和功能的新事实。特别地，我们提出，单字理解、产生（出声/命名）以及重复 (single-word comprehension, prodcution (speaking/naming) and repetition) 能力由背腹语言通路的交互作用来支持。

我们的模型借鉴了先前的语言和短期记忆计算模型的重要且有影响力的贡献（引用一堆大牛小牛的模型，此处略，译者注）。我们重新配置了这些纯计算模型中使用的结构，以更好地反映我们当前对真实的语言系统神经解剖学知识的理解。借助由此产生的约束在神经解剖学范围内的计算模型，我们展示了既经典又有所进步的失语症——在此结构中出现的失语症——的形式，以及该模型是如何解释良好建立的各形式的损伤症状之间的相关性的。我们进一步阐述了如何将神经解剖学并入一个明确的神经计算形式主义中，以解决 Lichtheim 时代模型的缺点。首先，模型发展出的内在表征的定量分析让理论家可以去指定每个大脑区域计算出的功能的性质，并将其与功能神经影像学的实证观察联系起来。其次，与可塑性相关的恢复 (plasticity-related recovery) 的仿真提供了关于许多患者再损伤后观察到的部分自发恢复 (partial spontaneous recovery) 的外显的、可测试的假设。

经典的语言的神经解剖模型被背侧语言通路支配，其中外侧裂语言区域 (perisylvian language areas) 如后上颞回 (posterior superior temporal gyrus, pSTG)、下侧缘上回 (inferior supramarginal gyrus, iSMG) 和上前回 (inferior frontal gyrus, iFG) ，与弓状束 (arcuate fasciculus, AF) 相连。近期神经科学文献（也很可能包括威尔尼克 (Wernicke) 本人）已经超越了这些区域和单一通路，提出了一条“腹侧”通路（包括中纵向束 (middle longitudinal fasciculus)、极外囊 (extreme capsule, EmC) 以及可能的，钩束 (uncinate fasciculus, UF)）。多数提议指出，每个通路中至少有一定的专门化，背侧通路捕获给定语言的声音-运动统计结构 (sound-to-motor statistical structure) ，并作为失语症患者重复性缺陷 (repetition deficits) 的主要来源。相反的是，腹侧通路与词汇语义 (lexical-semantic) 对语词重复 (word repetition) 的影响有关，并且相关地，此通路在前颞叶区域汇聚其它感觉输入所整合形成的概念知识，对于从声学-音韵学 (acoustic-phonological input) 输入中提取意义至关重要。尽管这不是语言的经典神经学模型的一部分，但现在有来自功能性神经影像学、rTMS、患者和直接的白质及皮质刺激 (white-matter and cortical stimulation) 的研究的可观证据表明该区域和通路的重要性。

此次实现的双通路模型可以正式考虑该区域及相关加工是如何适应更大的语言网络的，并提供了基于计算和神经解剖假设的表面效度(face validity) 的一个关键的测试。该模型还直接提供了一个独特的机会来探究每个“区域”内执行的计算以及它们之间的交互。通过以这种方式将计算与神经解剖相联系，得到的神经计算模型提供了理解失语症的神经基础以及模拟功能性神经影像的基石（两者都需要一座连接解剖学与行为学的桥梁）。

### Aims of the Current Study

#### Assessing the Face Validity of the "Lichtheim 2" Model

（评估 Lichtheim 2 模型的表面效度）

使用先前工作中的技术和方法，我们重新表示了语言的纯计算模型的结构，以便更忠实地反映双通道神经解剖理论。我们测试了神经计算模型的合成正常语言行为（出声/命名，理解，重复 (speaking/naming, comprehending, repeating) ）的能力。有了成功的模型，我们便能够探究框架的每个“神经解剖学”元素，以了解其功能以及两种通路之间的相互作用。

#### Understanding Aphasia in Lichtheim2

（理解 Lichtheim 2 模型中的失语症）

双通路假出声现在当代纤维跟踪成像 (tractography)、功能性神经影像学和失语学 (aphasiological) 数据的背景下，而经典的语言模型主要旨在解释（尽管不是综合）不同类型的慢性失语症。因此，我们探讨了 Lichtheim 2 神经计算模型受损后，慢性（中风相关 (stroke-related)）和进行性（语义性痴呆 (semantic dementia)）形式的失语症如何出现。此外，我们还提出了一种新的观点，即慢性患者的表现反映了损害和部分恢复过程的结合，这可能是由于重新调整神经连接权重以优化剩余的计算能力而引起的。

#### Understanding Contemporary Neuroscience Findings

（理解当代神经科学的发现）

复杂的结构和功能性神经影像学的兴起催生了大量关于以下内容的新信息：

1. 与不同语言网络部分相联系的计算；
2. 不同病人在不同区域损伤后受损的语言能力的性质。

我们测试了模型的能力，让它去捕获和解释以下每种类型的高知名度的样例：

1. 沿腹侧、嘴侧 (rostral) 通路的信息的声音/语言至语义的转换，通过分析 变化的沿复测通路不同位置编码的相似结构 (similarity-structure) ；
2. 通过评估不同区域损伤造成的语义性出声/命名错误的比率，我们测试了最高语义错误率 是否发生在前上颞回 (anterior STG) 损伤之后，像一个近期的关于 voxel-symptom lesion mapping 的研究所阐述的那样。

接着，通过探索和理解该区域信息编码的性质，模型提供了关于为什么损伤发生在这里但不是其它地方的见解，在此处生成了一个数量最大的语义错误。

#### Understanding the Significance of the Dual Pathways

（理解双通路模型的重要性）

尽管有清晰的、不断涌现的关于人脑双语言通路的证据，神经计算模型让我们能测试不同可能的结构的运作（有关失语症的命名和重复的并行计算比较，请参见 Nozari 等 [2010]）。通过实现一个单通路结构并将其与双通路模型比较，我们有能力去探索为什么真实大脑使用双交互式通路实现语言能力会更加有利。

## RESULTS

图1显示了双通路模型的神经解剖学约束下的结构（更多详细信息见“实验程序”部分，以及附录中的图S1）。这包括了一条背侧通路（初级听觉皮层 ↔ 下侧缘上回 ↔ 岛叶-运动皮质，由弓状束支持）以及一条腹侧通路（初级听觉皮层 ↔ 中上颞回 (mid-STG) ↔ 前上颞回 (anterior-STG) ↔ 岛盖部-三角部 (opercularis-triangularis) ↔ 岛叶-运动皮质，由中纵向束和极外囊支持）。通过连接至前上颞回，我们也纳入了腹前颞区域 (ventral anterior temporal region, vATL) 。由功能性神经影像学和神经心理学研究表明，此区域对于言语和非言语理解都起到关键作用。模型被训练用于出声/命名、重复和理解一套1710个多音节日语单词（包括随时间变化的输入和输出，以及语言的其他具有计算挑战性的特征；具体见“实验程序”部分）。图2显示了网络的以词频为自变量的这些任务表现函数的发展轨迹。像小孩一样，该模型表现了针对每个任务的不同掌握功能，包括在理解之前的重复 (repetition preceding comprehension) 和在出声/命名之前的理解 (comprehension preceding speaking/naming)。在经过训练之后的“adult”状态，该模型有能力重复训练集中的所有词语，其它未用于训练的真实词语（例如，没包括在训练集中的真实日语单词）以及一系列非词语（如，合乎规则的日语语音非单词序列，与未用于训练的真实单词相比，不可避免地具有较低的音律和bi-mora频率），并与人类的表现相比较（见附录的图S2）。总的来说，此次实现的背腹神经计算模型被证明是一个与成人和儿童的语言表现兼容的全功能模型。

![](https://ars.els-cdn.com/content/image/1-s2.0-S0896627311008348-gr1.jpg)  
图1 Lichtheim 2 — the Implemented Neuroanatomically-Constrained Dual-Pathway Language Model  
(*See also Figure S1.*)

![](https://ars.els-cdn.com/content/image/1-s2.0-S0896627311008348-gr2.jpg)  
图2 Accuracy of the Network on Three Language Tasks as a Function of Learning  
(*The y axis error bars show the standard errors across five simulations. Generalization of repetition was tested using both untrained items (real Japanese words) as well as novel tri-mora items (Japanese nonwords) for direct comparison with human participants. See also Figure S2.*)

### Synthesizing Aphasic Patient Data

图3总结了模拟病变对不同区域（代表的层）的效应。使用60个高频词和60个低频词来评估模型的表现（详见附录的 Supplemental Experimental Procedures）。每个区域中模拟了十五个水平的损伤严重程度。多数形式的病变或萎缩包括了对灰质和其下白质的损伤。相应地，模拟的损伤包括了将噪声添加到单位输出中，以模拟灰质病状（从0.01到0.15，等间隔），以及移除进入受损层的链接以模拟白质损坏（从0.5%至7.5%，等间隔）。

![](https://ars.els-cdn.com/content/image/1-s2.0-S0896627311008348-gr3.jpg)

图3 不同病变部位和严重程度对经典（中风）和进行性失语症的影响  
(*The x axis shows the proportion (%) of the incoming links removed and the range of the noise (bracket) over the output of the damaged layer. “Intact” means the performance of the model before lesioning.*)

几个经典（中风）和进行性失语症被综合。图3A至3E总结了病变对大脑外侧裂后部 (posterior perisylvian region) 的影响(病变的中心以尾端-下端 (caudal-inferior) “顺时针”方式转移)。岛叶-运动层的损伤导致了传导性失语症（conduction aphasia, 受损的出声输出，保持的理解能力）再生 (reproduction) 以及一个相似的模式在损伤覆盖岛叶-运动皮层和下侧缘上回时被生成（图3A和3B）。短时记忆/重复的传导性失语症选择性模式发生自孤立的下侧缘上回损伤（图3C），尽管出声/命名和重复的损伤水平更大。把这些考虑在一起，这些模拟可能解释了短时记忆/重复对于传导性失语症再生 (reproduction conductive aphasia) 的明显的罕有性，因为重复-选择性缺陷至出现在下侧缘上回层受鼓励和轻微损伤的情况下。总之，这些模拟反映了传导性失语症和真实病人背侧通路损伤之间的联系。威尔尼克失语症（理解力严重受损，加上出声/命名和重复的中度至重度障碍）与后测颞上回 (pSTG) 中心及周围区域的损伤有关。模型损坏的相应部分（声音-语音输入层 ± 下侧缘上回的附加损伤）确切地导致了这种行为模式（图3D和3E）。与此相反，上前回的损伤可引起布罗卡类型的/跨皮层的运动失语症 (Broca-type/transcortical motor aphasia) ，特点是，在词语加工的情况下，相对良好的理解能力、受损的重复能力以及严重影响的出声/语词能力。模型在相应区域受损后恰好遵从这种模式（岛盖部-三角部 (triangularis-opercularis)层，见图3G）。最后一个目标是语义痴呆，集中表现为完整的重复能力，严重损害的理解和出声/命名能力，特别是对于萎缩背景下的低频词，侧重于前颞叶的？侧和极侧 (inferolateral) 。这个模型再次展现了ATL成分（腹前颞和前上颞回，图3F）受损后的这种特定综合征组合。为了正式比较模型和实际SD患者中词频效应的大小，我们提取了一个词子集，以匹配 Jefferies 等人使用的频率操纵的大小（Cohen’s d for HF-LF difference = 1.61 in our materials, and d = 1.64 in Jefferies et al. [2009]）。🚧

## EXPERIMENTAL PROCEDURES

### Rationale for Methodological Details (Working Assumptions)

#### Level of Granularity

### Summary of Implementation Details

#### Architecture and the Activation Flow

建立了一个神经网络模型，并与 Light Efficient Network Simulator⚠️ 一起训练 (Rohde, 1999) 。 它被实现为一个 simple-recurrent Elman network model⚠️，以减少计算量(Plaut 和 Kello，1999) ，实现这一实现的精确计算结构如图 S1所示。具体来说，一旦一个模式被固定在声音输入层(例如在重复/理解中) ，Activation在每个 time tick 中扩散到(1)，iSMG →岛叶-运动层; (2)，到 mSTG → aSTG → vATL 层; (3)，mSTG → aSTG → 三角-岛盖层 → 岛叶-运动层。通过利用回写连接 (copy-back connections⚠️) 实现双向连接，每一层的激活模式在下一次 time tick 时反馈到前一层(参见图S1获得更多详细信息)。每个单位使用一个Sigmoid激活函数，Activation的范围定在0和1之间。

### ...