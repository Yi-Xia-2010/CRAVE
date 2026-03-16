label chapter10:

    # [Scene: Tidewatch Coastal Lab | Late Night]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low whirr of pumps; an old box fan clicks as its blades slow; distant, rhythmic slap of tide against pilings.]
    # play music "music_placeholder"  # [Music: Sparse, tense piano underscoring]
    "You step inside and the warm, damp air wraps around you like an old coat. The lab smells of solder and wet paper and the faint mineral tang of seawater that has been breathed into everything that lives here. Claire looks up from the screen before you close the door."
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "You're late, or the storm's on schedule and you aren't."
    "You drop your jacket on a chair. Your boots leave a smear on the concrete—salt-darkened, quick to dry in the lamp's glow. Your notebook is heavy in your pocket, pages swollen with thumb-grease and coffee. The compass at your throat feels like a weight and a promise both."
    show mara_solano at right:
        zoom 0.7

    mara_solano "Traffic. And a cooling-off period,' 'Which you did not give me."
    "Dr. Claire Hsu pushes a stray curl of silver-streaked hair behind her ear and taps a key. The screen flares: lines of model code, colored overlays of predicted surge, and a matrix of boundary conditions."

    dr_claire_hsu "Good. Because I think you'll want to see this before it goes farther."
    "She slides a printed sheet across to you—figures, simplified notes in her cramped handwriting. The title header blares the project's brand name in corporate fonts. Your name is nowhere; the model is proprietary, encrypted in layers and licensed to Voss Development."

    dr_claire_hsu "We ran a parallel implementation against publicly available bathymetry and our survey points. For the first pass, it's... plausible.' [voice tightens] 'But the assumptions—Mara, look at the substrate compression term."
    "You feel your palms go a little damp. Claire's fingers hover over the code as if it could be soothed. Her field vest has dark blotches of wet sampling residue; her smell is a cross of tea and antiseptic. The lamp hums. Outside, rain hammers a little harder."
    "Mara Solano: 'Explain it to me like I haven't stared at sediment compaction since grad school.”"
    "Dr. Claire Hsu lets out a dry sound that might be a laugh, might be a sigh."

    dr_claire_hsu "They linearized the compression response. They treat substrate settling like it's uniform—an elastic adjustment with a fixed modulus. That smooths out localized settling and assumes the landfill under the barrier compresses evenly. It erases nonlinearity: liquefaction pathways, scour concentration, substrate failure where loads concentrate. In reality, those heterogeneities can redirect surge laterally into neighborhoods that the model reports as 'protected.'"
    "You lean in until the glow of the screen paints your face pale. The word 'protected' sits on the model like lacquer."

    mara_solano "So the model underestimates redirected surge because it assumes the ground behaves like a single, honest sheet."

    dr_claire_hsu "Exactly. And if the barrier is built to those specs, the map goes from theoretical resilience to engineered hazard for the margins."
    hide dr_claire_hsu
    hide mara_solano

    scene bg ch10_453e40_2 at full_bg
    "Your chest tightens. Your father's hands come back—hands that tightened lines on nets, that braced against wind you could still smell sometimes when a storm pressed down. You imagine the streets near the market, the children"
    "playing on patched steps, roofs curling like old paper. The model is a promise in corporate fonts. Your throat tastes like the salt on your lips."
    "A chime from Claire's tablet draws both your eyes: a new message."
    # play sound "sfx_placeholder"  # [Sound: Tablet chime — short, urgent]

    scene bg ch10_453e40_3 at full_bg
    "Claire's face goes immediately neutral, businesslike. The softness you know is there, but tonight it is folded under a surgical calm."
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "They routed it through counsel. IP access, Claire Hsu and Mara Solano—do not disseminate proprietary material. You didn't—' [she stops] '—but they know someone is poking. They will scrub access logs."
    "Your heartbeat hammers a rhythm that matches the pumps. The legal language is sterile and precise; in it, threat hides like a knife in silk."
    show mara_solano at right:
        zoom 0.7

    mara_solano "So they noticed an anomaly in their telemetry? Or someone tipped them?"

    dr_claire_hsu "Both, maybe. Their telemetry flagged repeated access from an external node last week. And their communications team has been scanning open-source repos. We triggered a ping."
    "You run your thumb across the edge of the printed sheet until the paper fibers lift slightly. Your mind lists immediate consequences: locked-out data, subpoenas, court injunctions, gag orders. And beneath the legal apparatus, the very human thing: Elena's PR machine—friendly quotes on coastal stewardship—ready to paint dissenters as alarmists."
    "A knock at the lab's outer door—soft, deliberate. Jonah's silhouette fills the rain-streaked glass before the door opens an inch."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "They said you'd be up,' 'they also said there's a letter on the street for Claire. I brought sandwiches."
    "His smile is the small warm light you have been measuring your days against. He sets a damp paper bag on the table, but his eyes are steady—not bright. There's worry folded into the corners, like"
    "the way he tugs at the silver streak in his hair when he's thinking too much."

    mara_solano "Sandwiches are a strategy?"

    jonah_reyes "For late nights. Also: documentation and witness lists.' [he fishes a small stack of notepaper from his jacket] 'If you're going public, we need chain of custody, timestamped tests, witness statements. Rosa and Mateo can vouch for survey dates. I can get the market coop to archive the petition copies—won't let them say this is some anonymous blogpost."

    dr_claire_hsu "We will need more than testimony. We need reproducible probes—open code, error bars, a clear explanation of the compression simplification and its practical consequences. If we can show runoff pathways materially differ when substrate heterogeneity is modeled, that's scientifically damning."

    mara_solano "And legally messy."

    jonah_reyes "Messy but necessary.' [meets your gaze] 'You know I'll stand with you in it. But we've got to be honest about what comes next. Elena's firm won't just sue. They will—' [he searches for the word] '—spin. They'll make it personal. They'll try to make you the danger, not the design."
    "You hear solidarity in him but also a weariness that sinks through you. This is not the same as a march with banners and hands; this is a fight with equations and subpoenas and reputations. The town understands banners. Lawyers understand fine print."

    menu:
        "Double-check the codebase tonight":
            "You tuck your notebook under your arm, fingers eager, and tell Claire you'll run a second implementation overnight—no sleep, more tests. The lamp will keep you honest."
        "Get some rest; start fresh tomorrow":
            "You let out a long breath and say you'll shut the lab down for a few hours. Jonah will coordinate witness lists while you sleep. There is a tremor of relief in that option."

    # --- merge ---
    "Claire watches you choose with an expression that's almost maternal—stern, guarded, and quietly proud."

    dr_claire_hsu "If we run a second build, do it in an isolated node. Document everything. If they accuse us of tampering, the logs will tell the truth. And Mara—' [her voice drops] '—if we publish, be prepared for reprisals. Not only legal: smear campaigns, targeted surveillance, threats. Elena's team knows how to make noise."
    "You think of Elena's composed face at council meetings—her platinum bob like a blade of glass, her measured phrases that come wrapped in spreadsheets. She said once, in a town hall lit cold with LEDs, that"
    "hard choices had to be made to save many. The memory of it tastes metallic now."

    mara_solano "We have to tell people. The town can't be a lab variable for a corporate dashboard."
    "Jonah Reyes reaches out, covering your hand for a second. The touch is small and steady; it argues with your more practical mind in the only way it can—by feeling true."

    jonah_reyes "Then we make the explanation clear. We keep it local first: market, community councils, the lab. Then bigger. But we lock down the chain-of-custody. No loose copies."

    dr_claire_hsu "I'll contact Claire (legal)—' [she laughs softly at the name confusion] '—my university's counsel. They'll give us a safe harbor for the data if we follow procedure. But university counsel also hates headlines. They're cautious but useful."
    # play sound "sfx_placeholder"  # [Sound: A low vibration—your smartwatch buzzing against the lab table. You can see the cracked face, the improvised strap caught in the lamplight.]
    hide dr_claire_hsu
    hide mara_solano
    hide jonah_reyes

    scene bg ch10_453e40_4 at full_bg
    "The lab seems to shrink around that phrase. 'Immediate cessation requested' reads like an instruction to stop breathing."
    show mara_solano at left:
        zoom 0.7

    mara_solano "If we stop, nothing changes.' (the syllables are rough) 'If we release this, people will get angry, and maybe they'll be safer. Which version of harm do you choose—slow and structural or sudden and public?"
    show dr_claire_hsu at right:
        zoom 0.7

    dr_claire_hsu "Both can hurt the same people; both can save some. We need to choose transparency over false assurance. Ethically, I can't sit silent if the model misleads on redirection risk."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "And I won't let them make you the villain for telling the truth. We'll get witness lists, documentation, and community voices. But you should know—my mother lost her stall to a storm three years ago. I won't let us lose more than our patience here."
    "You stare at the code until the brackets and semicolons blur. Inside the blur, the anomaly stays distinct: a boxed comment where some junior engineer may have written 'ASSUME COMPRESSIBILITY CONST' and someone higher up let"
    "it stand because it made the model converge. A small, human shortcut with large consequences."
    # [Scene: Your Home | Near Midnight]
    hide mara_solano
    hide dr_claire_hsu
    hide jonah_reyes

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Spoon against ceramic as Aunt Pilar kneads; soft conversational hum of radio in the other room.]
    "You step inside and the smell of rising yeast and citrus peel pushes against the cold echo of the lab. Aunt Pilar works dough with a practiced surety—her hands flattened and folded, rhythm steady. The kitchen light glows amber and forgiving."
    show aunt_pilar at left:
        zoom 0.7

    aunt_pilar "You look like you've been marching storms,' (she says without looking up) 'Or wrestling ghosts."
    "You sit at the table, the notebook heavy like an animal waiting to be fed. You consider laying out the prints for her to see, but her face is a map of years lived in sun and salt. You don't want to drag her into engineers' equations."
    show mara_solano at right:
        zoom 0.7

    mara_solano "We found a simplification in the model. It could redirect surge if they build as designed."
    "Aunt Pilar pauses, pinching dough, flour dusting her knuckles like frost."

    aunt_pilar "So the shiny wall could push the water to other doors."

    mara_solano "Yes."
    "She studies you for a beat, the creases at her eyes deepening as if to hold enough counsel for a lifetime."

    aunt_pilar "When your padre died, we cried and then we barricaded doors. There were always choices then. You must keep your head clear, niña. If you go to war with a tower, make sure the war you fight is the one you can win. Not because victory is everything, but because the cost of losing to foolishness is too dear."
    "Her voice is low, the leather of her wisdom rubbed smooth. You taste the dough in the air—yeast, salt, citrus—and for a minute you're a child again, kneading under her gaze, safe."

    mara_solano "And if the cost is my life?"
    "Aunt Pilar looks at you with a steady, fierce tenderness."

    aunt_pilar "Then make sure it was worth it. But don't let fear wrap you so tight you forget who you are."
    "Her hands continue their motion, measured and ancient. You press your fingertips to the paper of your notebook until it indents. Outside, the rain begins to soften."
    "You think of Jonah's lists, of Claire's code, of Elena's legal notice, and of Aunt Pilar's soft admonition. Each thread pulls you in a direction as real as tides."

    mara_solano "If we publish, Claire says we can make it reproducible. If we don't—"
    "Your voice fails. The options don't sit on a pedestal of neat morals; they're porous, messy, human-shaped. You know what exposing the flaw could do—and you know what the backlash might feel like: lawsuits, smear campaigns, threats, the kind that hide in the small indignities before they bloom into danger."
    "An alert light on the lab tablet seems to breathe one last time in your memory—Cease & Desist—cold, legal, final. But your hands remember how to parse sediment cores and read a shoreline. The lab's lamp"
    "is still on in the corner of your mind, and beyond that, there are people who will need explanation, leadership, facts."
    "You can feel the tide of possibility gathering: come clean, risk everything; or remain quiet, preserve small safety, and watch the town be modeled into a false security. Both will leave scars."
    hide aunt_pilar
    hide mara_solano

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: A single low cello note, unresolved]
    "You stand, the dough's scent clinging to your sleeves. Your fingers find Claire's printed sheet in your bag like an anchor."
    show mara_solano at left:
        zoom 0.7

    mara_solano "We prepare everything. We follow procedure. We protect the chain-of-custody. We tell the town first."

    "Aunt Pilar nods almost imperceptibly. Jonah's voice, calm and resolute, seems to echo from the lab" "We archive, we witness, we stand with you."
    "For a moment the plan is a string of practical steps—clear, rational. But between them yawns the possibility of personal loss. You imagine headlines, the cold brightness of Elena's lobby flashing reassurance, a television pundit reducing"
    "sediment dynamics to sleeve-rolled comparisons. You imagine, too, a map where some neighborhoods survive because of a hard truth laid bare."
    "The lamp in the kitchen hums. Outside, rain eases into a soft patter. Somewhere in town a pump's motor slows, then picks up again."
    "You sit at the table and begin to write: test protocols, sample logs, timestamped notes, witness contacts. Your handwriting is messy but determined. Each line is a small weapon; each line is a promise."
    # [PAGE-TURN MOMENT: You place the completed stack of annotated code, printouts, and witness lists into an envelope addressed to the community archives and to the lab's institutional counsel. The Cease & Desist is folded into the packet, a cold reminder of the friction ahead. Your heart thrums with fear and purpose—and as you lift the envelope, you realize the town will not wait for a courthouse to decide whether it must flood or stand. You step into the rain with the packet under your jacket, the air tasting of salt and potential. The night holds its breath. The choice is set in motion, but the consequences have not yet arrived.]
    hide mara_solano

    scene bg ch10_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
