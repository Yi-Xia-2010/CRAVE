label chapter14:

    # [Scene: Highland Cliffs Overlook | Late Afternoon — After the Surge]

    scene bg ch14_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Low cello, slow and descending]
    # play sound "sfx_placeholder"  # [Sound: The town bell tolling unevenly; distant shoutings; the hollow clank of a loose rigging line in the harbor]
    "You sit with your knees pulled up against the cliff's lip, the damp of the grass seeping through denim. The compass at your throat is cold. Below, Tidehaven looks smaller than it did in the models—shrunken"
    "by water, flecked with moving white. A tidal creek that used to be a thin, silver vein has swollen into a new inlet, and along its banks a row of older homes stands like a row"
    "of paper lanterns caught in wind."
    "The bell in the town square swings on a wind you can feel in your teeth; every toll is a report card you didn't want to read. Salty air, the iron tang of uprooted soil, the faint rotten sweetness of something that once lived—these smells press into you like accusation."
    "Jonah Reyes sits a shoulder away. His coat is salt-dark at the cuffs. He doesn't look at you at first; instead his hands work a flat stone with thumb and fingertip, the small ritual of someone trying to make sense through motion."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They moved fast down there. Boats, trucks, people—everyone who could. Bento organized kitchen shuttles. Kai's running a list. I—' [Stops, breath caught] '—I can't tell if it's luck or if we were lucky enough to get people out."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Rescue teams got to the worst of it. There were calls—some went out early.' Your voice is smaller than you expected. You hold the compass and remember how your thumbs found it in councils and quiet rooms alike. 'Not everyone made it. Not everything could be saved."

    jonah_reyes "I heard about the Larkin place. Old quilts, Jonah—' [Swallows] 'You know what they were talking about on the porch. The Polaroids. Bento said they pulled a box of letters out of the mud and the edges were already papery. He couldn't—"

    mira_kestrel "The images arrive like tidal debris in your head—photos, child's wooden boat, a brass compass you once saw on a mantle. You did not promise the sea mercy; you promised the town a deliberative process. The pause felt like care. Now it feels like an unpaid debt."

    mira_kestrel "I thought time would let us do it right."

    mira_kestrel "I thought more listening would mean fewer mistakes."

    jonah_reyes "More listening didn't stop the tide, Mira.' He finally looks at you—amber eyes rimmed red. 'I get why you wanted it. I stood with you when you asked for more proof. But I can feel people thinking we waited too long."

    mira_kestrel "I know.' You close your eyes and count the bell's tolls. Each one is a ledger entry: what was weighed, what was deferred. 'I know."

    menu:
        "Stand and peer down the cliff towards the creek":
            "You rise and lean forward until your boots scrape the damp earth. From this angle you can see the rescue teams like scattered specks—a group forming a human chain, someone passing a box up the slope. Up close there are faces you recognize and faces you don't; shame mixes with relief in your chest."
        "Stay seated and speak to Jonah":
            "You stay where you are. Jonah turns his hands over in his lap and finds yours with a quiet attempt at anchoring. You talk, small things—how cold the wind is, how Bento cursed under his breath while packing soup—for a moment, ordinary details slow the spin of what just happened."

    # --- merge ---
    "You choose neither to bargain for absolution nor to demand it from Jonah. The cliff answers with wind, the bell answers with time, and down below the town keeps moving—haltingly, messily, alive."
    # [Scene: Tidehaven — Tidal Creek & Flooded Row | Dusk]
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch14_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low murmur of generators; the slap of water against warped siding; someone quietly sobbing under a tarp]
    # play music "music_placeholder"  # [Music: Solo violin—thin, trembling]
    "When you walk the flooded lane later, you move like someone examining the aftermath of a mirror shattered into family fragments. Neighbors exchange small, stunned courtesies; Kai runs with a clipboard, his hair flattened and streaked with mud. You avoid speaking names at first because names are anchors to grief."
    show kai_tan at left:
        zoom 0.7

    kai_tan "We set up a drying station at the Greenhouse. People are bringing things—books, photographs. Bento's organizing the boat teams. We could use more hands. We could use—' He looks at you hard, searching for the cadence of responsibility. 'We needed more urgency."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "I pushed to pause. To listen. To gather better data.' The words feel frail in the cold air, as if they might drift away. 'I thought that would make us stronger when it mattered."

    kai_tan "Stronger how? Better informed? Better at blaming ourselves later?' He doesn't look at you like an ally. He looks at you like someone whose caution cost a family their things. 'We were sitting on studies while their attics filled."

    mira_kestrel "I thought oversight would keep us honest. I thought the phased approach would protect people by giving them choices, giving the community voice in what was prioritized."

    kai_tan "Choices that cost them memories."
    "From the flooded bank a woman calls out a name and someone else answers with a steady list of what they're saving. A rescued dog barks. Your throat tightens—an animal's sound becomes a bell of its own."
    # [Scene: Tidehaven Town Hall — Emergency Meeting | Night]
    hide kai_tan
    hide mira_kestrel

    scene bg ch14_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs folding into a heated cadence; a chair scraped too loudly against the floor]
    # play music "music_placeholder"  # [Music: A low, insistent drum under current strings]
    "The meeting convenes because anger gathers like stormwater—fast, heavy, and relentless. Asha Verma stands at the head of the room, coat still flecked with rain, her tablet closed in one hand. Her face is granite; anger carves lines that were not there the last time you argued in public."
    show asha_verma at left:
        zoom 0.7

    asha_verma "The delay cost us windows. Funding cycles closed, equipment schedules shifted, contractors took other bids. This town needed a structure in place yesterday. We moved slower than the science required."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We moved slower because we tried to make room for those the plan would ask to move. Because we asked questions about equity and ownership. Because enacting retreat without voice is another form of loss."

    asha_verma "A loss you calculated in meetings?' Her eyes scan the room—there's exhaustion and accusation in them. 'Do you understand the people who counted on a wall being there? Do you understand what happens when we trade speed for conversation?"

    mira_kestrel "I understand more of the costs now than I did before.' You breathe and let the confession land. 'I understand the cost of inaction with a full throat."

    asha_verma "This wasn't just process, Mira. This was time. Decisions in the face of a moving ocean are not theoretical exercises. They're triage."
    "Her look is not purely blame—it is also grief. Describe it as complex: you see a woman who has been a soldier in other storms and who now has to hold the tally of what was"
    "gained and what was lost. It is not a simple condemnation; it is a ledger she cannot unwrite."

    "Kai Tan (from the back)" "Accountability isn't just about pointing fingers,' he says, voice ragged. 'It's about who gets heard before the water comes. We tried to be inclusive, but we didn't move like a town on fire. We moved like a town with a meeting."
    "An older council member clears his throat, and Evelyn Sato—who has less stamina in her eyes tonight—folds her hands slow as if rehearsing calm. The chamber smells of wet wool and coffee gone bitter from long hours."

    mira_kestrel "I believed we could do both—care and speed.' The words are small, a confession that doubles as a map of the mistake. 'I wanted to protect what people loved and not just the property they own. I thought we could engineer in justice."

    asha_verma "Justice doesn't stop water.' Her voice cracks on the last word, and you realize she carries her own list of people she couldn't save. 'We had to choose what to prioritize. We chose caution. The ocean chose otherwise."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We chose—you chose—not to lock the gates first."
    "You: Each phrase is a pebble landing on a shoreline you once thought solid. The room's heat makes your ears ring. You feel small and exposed, like a map with the edges already curling."
    # [Scene: Highland Cliffs Overlook | Night — After the Meeting]
    hide asha_verma
    hide mira_kestrel
    hide jonah_reyes

    scene bg ch14_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano notes, slowed; the overall tempo descending]
    # play sound "sfx_placeholder"  # [Sound: The bell finishes a lone, exhausted toll]
    "You and Jonah Reyes return to the cliffs because grief wants a place to be watched. From here you can see rescue lights like constellations rearranged in sorrow. People move below with the terrible focus of those who must do practical things while wounded."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "I don't know how to fix the past, Mira. I know how to build a berm. I know how to plant cordgrass. I know how to pull a drowned kit out of a house. I'm useless at the rest."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "None of us are enough for everything.' you say. 'I am learning that the hard way."
    "Jonah Reyes turns his face toward you, and for a moment the lines between your shared past and present blur. There is tenderness there, but it's scarce. You both have been hollowed in places the sea knows best."

    jonah_reyes "People are angry. They'll frame it as your call, as mine, as Asha's. They'll say someone waited when they shouldn't have. They'll want someone to stand in front of them and say 'I will fix this.'"

    mira_kestrel "I wish I could say those words with certainty."

    jonah_reyes "Maybe certainty was never on the table. Maybe all we have is the next shovel, the next list, the next hour."
    "You: Your mind reaches for a way to make meaning—small forward steps you can take even inside blame. There will be meetings, lawsuits maybe, donations and scorn. There will be photographs that will never be the"
    "same. But there will also be neighbors with kettles and hands that knit salt-crusted lines into rope for makeshift repairs."
    "Asha Verma's name comes up between you like a stone turned over. You do not know if what you see in her is anger or a mirror. Describe her expression as complex—hard edges softened by loss."
    "She will stand before the town in coming days and deliver the kind of words administrative positions require—firm decisions, apologies withheld or given carefully. You know her; you know the woman who has had to choose"
    "quickly before. The gulf between you is not only policy. It is a private geography of losses that neither of you will be allowed to heal in public."
    "In the quiet between tolls you find your palm on Jonah Reyes's knee. He does not pull away."

    mira_kestrel "I keep thinking about the way the town used to mend itself. We argued then too, but we patched with what we had. Now we trade in studies and contracts and stave off one kind of loss by courting another. I don't know if the public will forgive that."

    jonah_reyes "Maybe forgiveness isn't the point tonight.' He looks out at the town. 'Maybe it's about showing up when it's ugly."
    "Mira Kestrel: You swallow the shape of the confession that follows—less a defense than a forecast. 'I will keep showing up.'"

    jonah_reyes "Good."
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch14_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Long descending chord; then silence]
    "You look at the bell and at the town and at the ragged people already rebuilding in the streetlights. The moral erosion you feel is not theatrical; it's practical and relentless. People will write the story"
    "of this pause and this storm; they will decide where blame belongs. The truth is messy, layered like the strata you study—the sediment of good intentions and the bedrock of inevitable harm."
    "You fold your hands over the compass. It is heavier than it was in the lab. You think of your father's boat: the smallness of a vessel against a fetch of open water. You think of"
    "the decisions you made to negotiate fairness and how fairness can be cruel when weighed against immediate danger."
    "In the cold, Jonah Reyes leans his head against yours. It is not an ending so much as a marker: two people holding a shared ache,and a town moving forward under the weight of weather, politics, and memory."

    scene bg ch14_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, mournful piano line that slowly resolves downward]
    "You do not find absolution tonight. You find work to be done, apologies that may be necessary, and the heavy knowledge that the pause you brokered bought time for conversations—and, tragically, not time enough to prevent"
    "loss. The council chambers will be louder tomorrow. The developers will circle like gulls. The town's trust will need tending in a way that no single vote can administer."
    "You let the compass settle in your hand and accept the small, honest truth: you did not fail alone, and you were not alone in trying. That does not make the tally easier to hold."
    # [Scene: Highland Cliffs Overlook | Night — Final Frame]

    scene bg ch14_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Fading single note; then quiet]
    # play sound "sfx_placeholder"  # [Sound: The distant, regular breathing of the town; footsteps receding on the boardwalk]
    "You breathe the night into yourself. The salt, the cold, the memory—these become the ledger you will carry. There will be hearings. There will be written inquiries and charitable drives and angry posters. There will be nights like this where you and Jonah hold a shared, fissured silence."
    "You tighten your fingers around the compass until the brass is warm."

    scene bg ch14_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
