label chapter8:

    # [Scene: Old Mill Rooftop | Night — Storm Approaching]

    scene bg ch6_f05820_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, pounding percussion; a distant cymbal crashes in time with thunder]
    # play sound "sfx_placeholder"  # [Sound: Rain increasing from a hiss to a battering, boards creaking, one long keening gust]
    "You breathe with the rooftop: a shallow, quick inhale that tastes of salt and electric ozone. Below, Solhaven is a net of dark shapes — roofs, the washed-out line of the promenade, the ink of the"
    "sea swallowing the horizon. You can feel the decision you made earlier like a bruise under your ribs — practical, chosen, necessary — and tonight it presses against everything."
    "A figure moves beside you. Elias is there, coat plastered to his shoulders, hair at his temple matted by rain. He holds his tablet like a talisman, though the glass is useless in this downpour. In"
    "the pale, stuttering light he looks smaller. Not because he is less, but because whatever machinery he's learned to trust now looks fragile next to what the water is doing."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "Sensors are pegging out. Amina is requesting we stay put—coordinate from here until the lab's secure. The models didn't show this... not this intensity."
    "You want to say that models never showed losing them either. You want to say that the marsh saved them before, that the Commons was not supposed to be a target, that roofs are not good"
    "anchors for grief. Instead you notice the way his voice trembles on the last syllable, the way he is not yet asking for permission to hold you but seems to want it."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Tell me what we're doing. Tell me where people are."

    elias_navarro "Tidewatch has triage tents set up near the old boathouse. Amina's team is getting crews to levee points, but the temporary pumps—' (he swallows) '—the pumps are failing. The promenade's temporary cofferdam's overtopped at Marker Three. If it breaches further…"
    "Your hands remember every shovel you ever lent to a neighbor, the weight of wet sandbags, the small, stubborn rituals that kept water from eating the places you loved. The rooftop's wind hammers against the hanging"
    "planters; one swings and snaps a strand of lights loose. A single bulb goes dark."
    # [Scene: Saltwren Commons | Night — Storm In Full Force]
    hide elias_navarro
    hide mara_lin

    scene bg ch6_f05820_2 at full_bg
    # play music "music_placeholder"  # [Music: Chaotic strings, dissonant; a high, repeating motif of alarm]
    # play sound "sfx_placeholder"  # [Sound: The roar of water, an animal-like snap as a support beam gives way, distant shouts muffled by the wind]
    "You run. Feet find the rope ladder and then the slippery stairs; rain claws at your face. The Commons is a blur of brown water and wet canvas. Your boots sink into something soft and wrong"
    "— mud, compost, a place you had planted names and futures. A wooden archway that had been a place for children to crawl through is now sideways, its bolts stripped by the current."
    "Tommy is there, shoulders hunched against the wind, shouting into the dark. His beanie is flattened; his hands are a map of quick movements, flinging ropes, tying lines to anything that will hold. He looks at"
    "you and for a second the old solidness is back — the boy who fixed your bicycle chain. But then his face breaks, a fissure of fear and urgent need."
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "Mara! The boardwalk at Crane's Bend—it's gone. People are trapped in the low flats behind the greenhouse. We can't get to them without boats."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Who is out there? Names. Houses."

    tomas_tommy_reyes "Mrs. Kline and her boy—third porch down. Old man Jory in unit five. Rae's group is pinned behind the northern berm—too deep to wade."
    "A memory tries to surface: a winter when the marsh rose and swallowed the smallest things, until names floated like driftwood. You clamp it down because there is no room for soft grief yet. There is"
    "only work. You shoulder a coil of rope that smells of algae and old sea, and start toward the waterline."

    menu:
        "Cut a path through the boardwalk to reach Mrs. Kline":
            "You take a crowbar and two friends; splinters fly like gray snow. For a breath, you are nothing but muscle and intent, and the world contracts into the simple physics of rescue. You reach the porch as water nips at your knees and pull Mrs. Kline into a blanket; her teeth chatter, eyes bright and uncomprehending."
        "Coordinate boats to reach the low flats":
            "You run calls into Tommy's radio, barking coordinates, balancing hope and the probability of failure. The first boat arrives half-submerged; you climb in guts-first, hands raw on frayed rope, and the oars strike the dark like frantic punctuation. You pull people aboard until the boat rides low, then push for the temporary pier."

    # --- merge ---
    "The choices dissolve into the same chaotic hum of rescue. Whether you pry or you paddle, whether you carry someone up a boardwalk or pull them into a boat, the motion is the same: translation from"
    "wet danger to something slightly less dangerous. Lives saved; nothing heroic, only necessary and exhausted bravery."
    # [Scene: Promenade | Night — The Cofferdam Fails]
    hide tomas_tommy_reyes
    hide mara_lin

    scene bg ch6_f05820_3 at full_bg
    # play music "music_placeholder"  # [Music: Timpani, metallic crashes; a heartbeat rhythm that speeds into panic]
    # play sound "sfx_placeholder"  # [Sound: The groan of steel, a metallic scream as rebar bends, a fresh, horrible tearing]
    "Celeste Park appears at the edge of the chaos like an image in a broken mirror: precise, soaked through, hands to her mouth as she watches equipment wash away. There is no staged composure tonight. Even she looks small, her usually immaculate coat plastered to her frame."
    show celeste_park at left:
        zoom 0.7

    celeste_park "We built what the funds allowed. We—"
    "You cut across the sodden concrete toward her before the thought finishes. You don't know whether you are looking for accusation or for someone to anchor your outrage."
    show mara_lin at right:
        zoom 0.7

    mara_lin "You built a promenade without real buffers. You called it stability."

    "Celeste Park [voice thin] (meeting your eyes)" "We did what we could under permits. The cofferdam was a temporary measure—"

    mara_lin "Temporary? Temporary costs people their homes."
    "She flinches, the steel in her shaking for a moment. Behind her, a section of the promenade gives way and slides in a clean, vertical swallow into the sea. A chain of equipment goes with it; a worker on the far end is thrown. Shouts. Someone's radio bursts into static."
    "Celeste sags. For the first time you see the exhaustion behind the precision — not cruelty, but a kind of culpable, professional fatigue. Her jaw tightens."

    celeste_park "We have emergency protocols. We are... mobilizing alternative shelters. Elias, the pumps—can they be rerouted to the southern channel?"
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "We can reroute some lines, but the main feed is compromised. Amina's assessing which neighborhoods have intact elevation. We need to prioritize—"
    "Your hands want to grab him for the single, comforting truth you both used to share: numbers matter; people matter; you can make them meet. But the storm scrambles those certainties. When you look at Elias"
    "now there is a new, sharp distance — not from lack of care, but because he is holding institutional lines you both once questioned."

    mara_lin "Prioritize Mrs. Kline's block. Prioritize the Commons. Prioritize lives, Elias."

    elias_navarro "We are prioritizing lives. I'm asking where I can deploy limited pumps and crews to save the most people."

    mara_lin "The Commons matters. The wetlands matter. People built their lives around those things."

    elias_navarro "I know that. I—' (he breaks off, the words breaking under pressure of something else) 'I never meant—"
    "Everything in you is a mouthful of old grief and hot accusation. The storm makes the words sharp and dangerous. You remember your sibling's name in a clean, remembered winter and the way the sea took them and left a grammar of loss you cannot unlearn."
    # [Scene: Tidewatch Lab | Night — Emergency Coordination]
    hide celeste_park
    hide mara_lin
    hide elias_navarro

    scene bg ch6_f05820_4 at full_bg
    # play music "music_placeholder"  # [Music: A single high note that will not resolve; electronic bleeps paired with frantic human voices]
    # play sound "sfx_placeholder"  # [Sound: Radios chattering, footsteps slapping in puddles, someone crying quietly into their sleeve]
    "Inside Tidewatch, Dr. Amina Bhatt moves with a calm that has been honed through long nights of data and disasters. She organizes with hands like a conductor, voice clipped but steady enough to be an anchor. She does not pretend to have miracles."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "We can maintain pumps at the north intake for now—if we hold the feed and shore material in the next twenty minutes. But the southern sluice is open. We'll have to route teams to prop a temporary breakwater."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "I'll marshal the university's portable turbines. We can cobble together a bypass."
    show mara_lin at center:
        zoom 0.7

    mara_lin "And you told the council this would be a balanced plan. You told me—"
    "Elias Navarro [working his tablet by touch]: (cuts in) 'I told you we'd use both strategies. We still can, Mara, but not tonight. Tonight we are triage.'"
    "The word is a scalpel. It says: choices, cuts, some loses are inevitable. You feel yourself go hard around the edges."

    mara_lin "Triage is choosing who to pull up and who to let go."

    elias_navarro "No. Triage is saving the most lives with what we can move."

    mara_lin "It feels like letting things fail so other things stand."
    "He looks at you and for a second his expression is not engineering or policy but bone-deep apology."

    elias_navarro "I am sorry. I thought—"
    "You watch a map on his tablet, little blue pins disappearing as neighborhoods flood in real time. You're a scientist of the earth now; you know thresholds like prayers. You watch them shatter."

    menu:
        "Stay and direct rescue efforts for the Commons":
            "You strap on a harness and bind yourself to a group handling the boardwalk beam. Every time you heave, someone breathes. You are wet and blasted and burning with an odd, furious focus. You keep naming people as you pull them into daylight—humanity becomes inventory, and you cannot stop."
        "Go with Elias to reroute pumps at the Tidewatch intake":
            "You follow him into the belly of the lab where wires hang like vines. He moves with a competence that is near grace; you help him haul a turbine into place, your fingers numb and slick. You feel the thin comfort of shared labor like a bandage over something raw."

    # --- merge ---
    "Neither path erases the other. Wherever you are, the town is splitting along lines you once thought could be bridged by earnest meetings and joint spreadsheets."
    # [Scene: Low-Lying Neighborhoods | Night — Houses Floating, Voices in the Dark]
    hide dr_amina_bhatt
    hide elias_navarro
    hide mara_lin

    scene bg ch6_f05820_5 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano notes; every one a dropped shard]
    # play sound "sfx_placeholder"  # [Sound: Sobbing layered with shouted directions, a distant siren that never gets closer fast enough]
    "The next hours are a kind of sacred brutality. You run through them as if under water — movements slowed, awareness sharpened. You patch a sandbag with trembling hands, lift an elderly woman's wet coat over"
    "a shivering shoulder, listen to the sound of a child asking where their father is and do not have an answer that isn't an ache."
    "At some point, the rescue work clamps around the town's spine and keeps it going. Emergency engineering—Elias' turbines, Amina's makeshift hydrology, Tommy's boats—keeps a constellation of people from drowning. Lives are saved. Not all of them. Not even the ones you had the best claim on."
    "You learn—too clearly—the line between infrastructure and memory. The promenade was not merely concrete; it was a promise that some elements of daily life could be made permanent. The Commons was not merely gardens; it was"
    "a ledger of birthdays and compost, of neighbors teaching neighbors how to coax life from salt."
    "When the storm relents, it leaves a strange, scorched clarity. You stand amid ruins. Raised beds are torn open like small coffins. A sapling whose leaves you traced with a child's hand is lodged against a"
    "fence, salt-caked and silent. The promenade has caved in sections, a jagged toothline into the sea. Low-lying houses are water-ruined, their family photos a smear behind wet glass."
    # [Scene: Old Mill Rooftop | Dawn — Aftermath]

    scene bg ch6_f05820_6 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, but weighted; a low, mourning chord on strings]
    # play sound "sfx_placeholder"  # [Sound: Dripping, distant generator hums, a single crow calling]
    "Dawn is not mercy. It is an inventory. People measure loss like a carpenter measuring timber. The radio traffic is less frantic and more raw. People are calling accounts. People are not calling for strategies; they are naming what has been taken."
    "You stand where the night started, looking down like a mapmaker of ruin. Elias arrives with mud streaking the elbows of his jacket, a bruise under his eye. He looks exhausted in a way the rescue masks cannot hide: raw, litigated emotion worn thin."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "We prevented the worst in the densest blocks. The turbines bought time. Amina's sensors warned us where to shore up. We—"
    show mara_lin at right:
        zoom 0.7

    mara_lin "You saved some. You also let the promenade be engineered the way it was."

    elias_navarro "We didn't build it to fall. I didn't—"

    mara_lin "You were inside the same institutions that signed off on the temporary fixes."
    "He searches your face like someone looking for the coordinate that explains a discrepancy. For all his science, there is a human moment here where no data will reconcile the ache."

    elias_navarro "Mara—"
    "You hold up a hand because to listen will be to let him start the apology that feels like a slab across your chest. You have been carrying apologies all through your adult life—apologies that stood"
    "in for remedies, for promises not kept—and tonight they are small stones sinking in the tide."

    mara_lin "Do you think you can live with that? With choices that weigh lives like data points?"

    elias_navarro "I thought we were choosing together. I thought mediation would give us room to avoid this."

    mara_lin "Mediation gave you leverage you had to defend. It did not stop the water."
    "He flinches as though struck. There is grief in his eyes, yes, but also something like guilt's brittle neighbor: rationalization. He explains, because that's what he knows how to do, because explanation has kept him afloat"
    "through many storms. You feel, with a cold clarity, that his very competence is tonight also a wall."

    elias_navarro "If we'd escalated—if we'd blocked construction outright, some of the funding wouldn't have come. We would have had different weaknesses. I thought—"

    mara_lin "You thought trade-offs could be distributed without cost to us."

    elias_navarro "I thought compromise could limit harm."

    mara_lin "Compromise didn't keep a child from having to hold a blanket around shivering shoulders. Compromise didn't stop the smell of salt and rot mixing in the air."
    "There is a silence like a sinkhole between you. The town thrums beneath, people organizing tarps, calling shelters, offering what they can. You feel the community pull together in its damaged state, but the thread between you and Elias is frayed beyond casual repair."
    "Tommy appears at the rooftop lip, face worked by the night's labor, eyes rimmed in red. He looks at the two of you, then down at the street. He does not speak the thing you both hear."
    show tomas_tommy_reyes at center:
        zoom 0.7

    tomas_tommy_reyes "Mara—people are moving to the school gym. They're asking about relocation funds, about who'll fix the greenhouse. Rae's got a petition already, and—' (he stops, looks at Elias) '—and they want names."
    "Elias meets Tommy's gaze and then yours. He looks older, like someone who has been exposed in the open and left to weather."

    elias_navarro "I'll stay. I'll testify. I'll help rebuild what's salvageable. I'll—"

    mara_lin "Help rebuild where? Where people are climbing out of their living rooms because their floors floated away? Or help rebuild the promenade so investors can advertise calm?"
    "His mouth opens; the words are soft and earnest and imperfect."

    elias_navarro "Both. We have to be pragmatic and humane. We have to—"

    mara_lin "We have to do what the town needs, Elias. And the town doesn't always need the same things as institutions."
    "He reaches toward you, a gesture that used to be a proposition of partnership. Tonight it feels like an appeal for absolution."

    elias_navarro "Can you—can you forgive me for the part I played? For the times I believed the filters would hold?"
    "You study his hand, weathered like everything else tonight, and see the way he wants to fix this with work. He believes in remedy. You believe in preventing the need for remedy. Two visions cleave the same shore."

    mara_lin "Forgiveness isn't a single act. It's a ledger. I'm not sure what belongs in it anymore."
    "He nods, hollowly. He understands the ledger metaphor perhaps too well. For once there is no eloquent engineering fix to stitch a heart."
    # [Scene: Saltwren Commons | Later — The Community Gathers]
    hide elias_navarro
    hide mara_lin
    hide tomas_tommy_reyes

    scene bg ch6_f05820_7 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, aching harmonies; low, supportive strings]
    # play sound "sfx_placeholder"  # [Sound: Quiet murmurs, a child calling a parent's name and receiving an answer, hammers tapping as people begin to build temporary platforms]
    "You walk the Commons perimeter as people organize the work to come. A group is measuring the top of an old raised bed, deciding which will be sacrificed and which can be saved. A small girl"
    "presses a wet palm to a mud-smeared plant like prayer. You kneel and touch the earth, feeling its cold, grainy honesty."
    "Tommy sits nearby, cleaning a knife. He looks at you with an old gentleness that does not demand anything but presence."
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "You did what you had to. So did Elias. And Celeste—well, she didn't mean for this, though she did sign off on things. People are hurting."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Does that make it better?"

    tomas_tommy_reyes "No. But it makes it ours."
    "You want to argue that 'ours' includes policy and plans and the right to refuse development that costs more than it pays, but tonight the town's 'ours' is also a communal patching of wounds."
    "You rise and find Elias at the edge of the work, a silhouette against the slate morning. He meets your gaze. There is a tiredness to him that suggests boundaries have been crossed. There is also a kind of tenderness that doesn't go away because of catastrophe."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "Mara—what do you want to do now?"
    "The question is small and enormous. It is the ground of the next days. It is also a question about two people who once believed common cause could mean the same thing."
    "You look at the mottled shore, at the commons you saved and the promenade you did not, at faces patched with tarps and decided courage. You think of your sibling and the compact you made with the world to never leave those at risk alone."

    mara_lin "I want people to be safe. I want the wetlands to be respected. I want the town to have a future that remembers what was lost."
    "Elias takes that in, his expression folding into something like acceptance and something like grief."

    elias_navarro "I want that too."
    "You both say it, but the 'too' sits on a ledge. It means different things, differently weighted. There is no neat reconciliation tonight, only a shared, ragged vow to attempt something together or apart."
    "You turn away to help at the greenhouse. He calls your name once, faintly, and you hear in it the possibility of many futures: some together, some not; some sacrificial, some pragmatic; all bruised."
    "You cannot predict whether this will be enough to bind two fractured people. You only know the town needs work, and a town's work requires steadiness more than fire. Your heart is a splintered thing."
    "You walk into the Commons—the place that still smells of compost and tea and the traces of a people who will not let the sea write their fate for them. You will stay and rebuild brick"
    "by stubborn brick, even as the ledger of blame thickens and coalesces into stories that will long outlive this night."
    hide tomas_tommy_reyes
    hide mara_lin
    hide elias_navarro

    scene bg ch6_f05820_8 at full_bg
    # play music "music_placeholder"  # [Music: One low, sustained chord that resolves only by fading into silence]
    # play sound "sfx_placeholder"  # [Sound: Distant waves, the murmur of people beginning to fix what can be fixed]
    "You look out to the sea one last time before the hour. The water is calm now, indifferent. It has taken, but it has not finished. You have survived this particular crash. Others will come."
    "You breathe in the cold air and let the grief press against your ribs. It is heavy, and it will stay, and you will not be the same."

    scene bg ch6_f05820_9 at full_bg
    "THE END"
    # [GAME END]
    return
