label chapter3:

    # [Scene: Municipal Plaza | Fall, Late Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, urgent strings with a mounting percussion]
    # play sound "sfx_placeholder"  # [Sound: Murmured crowd, the slap of pamphlets on palms, distant gulls over the harbor]
    "You step from the municipal steps into the press of bodies. Rain from earlier has left the flags heavy and dark; the air tastes of salt and wet fabric. People cluster in tight islands—neighbors you grew"
    "up with, a line of corporate reps in slick shell jackets, teenagers with signs doubled over their knees—and the space between them already feels like a fracture."
    "You feel the camera at your hip, its leather strap cold against your palm, but your fingers keep it there more from habit than intent. This morning's meeting has spilled into the open; the vote that"
    "Councilor Rosa announced is symbolic but dangerous—a spark when the tinder has already been stacked. You can hear the raw edges of it as easily as you can hear the wind: promises, accusations, a hunger for"
    "immediate answers."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Etta's voice, rough with rain and years]
    show etta_hargrove at left:
        zoom 0.7

    etta_hargrove "We have been saying this for years—mend the marsh, plant the marsh, let the roots slow the water. If you pull people away from the shore, you pull stories away with them. We are not a problem to be solved; we are a place to be saved."
    "She pauses and the crowd fills the silence with a rough, uneven applause. You smell peat and citrus from Etta's greenhouse apron; the scent settles into the seams of the plaza like a plea."
    "You want to step forward—want to give the woman who taught you how to read a tide line an anchor in the current—but before you move, someone else speaks."
    hide etta_hargrove

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft, steady voice; a murmur of interest from the crowd]
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "This thing won't replace the marsh. It won't pretend the sea isn't changing. But it can buy us time—power sensors for pumps, dampen wave energy off the worst coves. Small, modular, open-source. We can build these here, with the workforce we trust."
    "There are nods. Someone in the crowd—Jun, you think—calls out a cautious, 'Can they be fixed if they break?' Mateo answers with a smile that doesn't quite reach his eyes."

    mateo_alvarez "They're designed for hands like ours. If an arm breaks, we fix it. If a panel tears—Jun, you'll be out there with duct tape and coffee before dawn."
    "The laugh that follows is brittle; the buoy glints under a brief shaft of watery light. You feel a tug between admiration and the weight of compromise. Mateo's plan threads the needle—enough tech to offer protection,"
    "enough local control to stay honest—but threads can burn when people breathe on them wrong."

    menu:
        "Step up to support Etta":
            "You take two steps forward and set your hand on Etta's shoulder. The touch is small, steady. Etta breathes in, lifts her chin, and for a moment her eyes find you and the crowd quiets. You hear, above everything, the creak of old wood."
        "Hold back—listen to Mateo first":
            "You keep your feet planted, letting Mateo finish. His hands trace the buoy's shape and the crowd leans in toward the promise of hardware. You feel the air between you and Etta tighten, like a line pulled taut."

    # --- merge ---
    "Story continues"
    "Etta's face is a map—wrinkles like riverbeds—but her voice hardens into something like steel when she answers the murmurs that flutter toward Mateo's table."
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "Modular buoys won't save the eelgrass. Pumps won't rebind the peat. Time bought with machines is often time bought with strings attached. I've seen the contracts—I've seen promises that come with fences."
    "Jun steps forward, knuckles white around a wet rope, and faces a corporate rep handing out glossy pamphlets with a smile that doesn't reach his eyes."
    show jun_park at center:
        zoom 0.7

    jun_park "You say 'community-built'—and then the city sells our shore to the highest bidder. How do we know this won't be another sell-off?"

    "Corporate Rep" "Our proposal includes community oversight. We want to partner—invest in infrastructure so we don't lose anyone."
    "The word partner tastes slick and generic. You can hear the crowd divide like an incoming tide hitting a jetty: cautious, hopeful, furious."
    "Mara pushes through with her recorder out, rain beading on its plastic. She finds you and drops into the space at your side, eyes bright and hungry."
    hide mateo_alvarez
    show mara_chen at left:
        zoom 0.7

    mara_chen "Ari—people are watching. If you speak, they'll listen. If you don't, they'll decide you didn't care enough to try. Which is worse—their anger or their disappointment?"
    "You open your mouth and close it. The answer you want is tangled in other people's breathing. Saying anything will rearrange loyalties like furniture in a storm."
    hide etta_hargrove
    hide jun_park
    hide mara_chen

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A clean, specific timbre that cuts through the wind]
    "Elio Sato: 'We can raise the lowest berms, deploy surge barriers that:"
    "- Reduce immediate flooding risk,"
    "- Secure municipal assets,"
    "- Attract investment that keeps Tidebridge afloat financially."
    "Managed interventions are not the end of heritage—they can be a means to preserve it.'"
    "His eyes sweep the crowd and land—unmistakably—on you. There is a recognition there that feels old and clinical at once, like someone cataloguing a well-known specimen."
    show elio_sato at left:
        zoom 0.7

    elio_sato "Ari, I know you understand the data. We can talk logistics later, but today matters for preventing loss."
    "You hear the words as a scalpel. 'Preventing loss'—it is practical, crisp, and cold enough to cut. For a breath you imagine the shoreline stabilized, infrastructure humming, fewer nights of emergency evacuations. Then you imagine the long, slow hollowing when people are moved to make way for walls and gates."
    "Councilor Rosa steps to the central mic. Her shawl is damp and heavy, and people quiet because the office she represents is the one with the keys to the next meeting."
    show councilor_rosa_menendez at right:
        zoom 0.7

    councilor_rosa_menendez "This advisory vote is not binding. It's a direction for the consultations that will follow. But it's symbolic—so I ask neighbors to stand and signal which path they prefer today: community-led restoration, hybrid measures, or entering formal negotiations with outside firms."
    "The plaza's hum tightens into a held breath. The crowd rearranges into queues; hands go up, banners wave. The symbolic vote is a theater of pressure—and the theater demands a protagonist."
    "You feel it then: the weight of the town's eyes. Mothers with salt-streaked scarves look at you, men you fished with as a teenager cross their arms, Etta's jaw tightens into a line you've seen when"
    "she measures a seed tray for infestation. Mateo's fingers find the buoy's seam as if to steady himself; his face is a mix of hope and a fear he won't let tilt into pleading. Elio's gaze"
    "is steady, trained."
    "Your chest is a drum. Your palms are damp inside your gloves. You think of all the nights you stood in marsh grass testing soil, of the time the storm took your neighbor's shed and left"
    "them shaking on the porch. You think of promises you made in committee rooms and the camera in your tote that has traced the slow gnaw of salt into everything you love."
    "Jun finds you in the crush and presses a damp palm into your forearm."
    show jun_park at center:
        zoom 0.7

    jun_park "Ari—what are you going to do? If you stand up there and say nothing, people will fold like wet paper."

    "Etta's voice cuts in, raw and small" "You helped plant the first coir logs here—this was your idea once. Where does your loyalty lie?"
    "Mateo Alvarez looks up, then at you, and his expression is unreadable in a way that twists something tight in your chest. You can't tell if it's an appeal, disappointment, or a shield."
    hide elio_sato
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "No matter what you choose, I want us to listen first. There are ways to keep people together without letting outside money write the rules."
    "Elio Sato steps closer, lowering his voice so only you can hear. His tone is softer than his words."
    hide councilor_rosa_menendez
    show elio_sato at right:
        zoom 0.7

    elio_sato "Ari, you know the cost of hesitation. I lost people to indecision once. I won't let that happen here if you—if we—move with resolve."
    "There is heat now in the plaza, the kind that sings under skin. Arguments flare: a councilor's aide stressing budgetary timelines; a resident demanding guarantees about property rights; someone at the back sobbing quietly, the kind of sound that makes your insides ache."

    menu:
        "Hand your camera to Mara so she can capture the crowd":
            "You lift the camera and press it into Mara's hands. She nods, a fierce gratitude in her eyes, and angles it toward the rows of people. The optics—your camera—become a witness. The act is small, concrete, and it pins you in place."
        "Clutch the camera and keep your options open":
            "You leave the camera at your hip, fingers curled around the strap. The weight grounds you but also keeps you in the role of observer, not an orator. People glance at you as if waiting for a sign."

    # --- merge ---
    "Story continues"
    "Voices pile atop each other; the tent flaps slap as the wind turns. You can feel the arousal of the crowd: not merely excitement but a pressure like surf dragging on a pebbled shore—relentless, pulling."
    "Mara's recorder clicks. Etta's next words are a lance."
    hide jun_park
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "We do this together or we see our town offered in pieces. I refuse to be the generation that sells itself out."
    "A chorus answers—'We refuse'—and the sound is fierce and unmoored. Across the square, a dozen hands shoot up for the hybrid plan; a few, fewer now, lift for negotiation. The symbolic vote, you realize, will be a narrow margin if you don't steer it."
    "Councilor Rosa looks to you, and her face is both kind and impossible."
    hide mateo_alvarez
    show councilor_rosa_menendez at left:
        zoom 0.7

    councilor_rosa_menendez "Ari, you've been an anchor for the restoration collective and a voice on these issues long before this week. People respect your judgement. Will you stand and declare your support for one of the options, so we can tally a meaningful advisory vote?"
    "The plaza narrows to the space between your ribs and the sky. You taste metal—fear, maybe—and every argument you fought in committee, every phone call that ended in silence, unspools in your mind. You feel the"
    "old guilt—the one that saturates your decisions: the idea that if you don't choose correctly, people you love will pay the price."
    "Behind you, someone shouts about children whose rooms flooded last season. In front of you, Mateo's fingers flex around a seam on the buoy as if squeezing for courage. Elio's jaw sets like a breakwater."
    "Your pulse climbs, each beat louder than the last. The music in your head bangs at the same tempo: high, urgent, no shelter. This is the point where ambitions and compromises collide; it will fracture friendships or forge new alliances. Your decision can't be neutral. The plaza demands a declamation."
    "You feel the town's eyes rest on your sea-glass gaze. The moment is a blade: it will cut something open."
    # play music "music_placeholder"  # [Music: Strings peak, a sharp drum rolls—climax]
    hide elio_sato
    hide etta_hargrove
    hide councilor_rosa_menendez

    scene bg ch3_98c6f2_5 at full_bg
    "You inhale, and everything tightens—Etta's steady hand, Mateo's unreadable look, Elio's measured insistence, Jun's damp grip. The air is full of expectation, fear, and the knowledge that whatever you say will ripple outward."
    "You are about to speak. You are about to choose."

    menu:
        "Back the restoration collective with Etta.":
            jump chapter4
        "Endorse Mateo's hybrid buoy-and-marsh plan publicly.":
            jump chapter7
        "Agree to enter formal negotiations with Elio's firm for centralized protection.":
            jump chapter10
    return
