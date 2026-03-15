label chapter11:

    # [Scene: Flooded Plaza | Dusk]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, rising synth pad with soft percussion]
    # play sound "sfx_placeholder"  # [Sound: Murmurs of conversation, distant camera shutters, a kettle steaming at a vendor stall]
    "You move through the press of bodies like a tide finding channels. The campaign's noise is still in your bones: chants, signage, a child's voice reciting a list of names from memory. Beneath it all is"
    "the steady thump of something larger waking up—the city noticing. Your notebook is closed in your hand, pages warmed by your palm. You feel that slight tug at the base of your throat that means possibility"
    "rather than fear."
    "Salt and frying oil mix in the air; a brace of wet fabric brushes your ankle. Someone's megaphone coughs and then keeps talking. You let your eyes take in faces—neighbors you can name, reporters jotting shorthand,"
    "a few municipal staff who look both irritated and interested. The attention you helped create glints like a new surface to walk on: unfamiliar, but firm enough to support the next step."
    "Samir finds you at the edge of the crowd, his utility vest damp at the hem from the plaza's spray. He has a tablet tucked under his arm and that cautious, practical smile he uses when bad bureaucracy becomes good paper."
    show samir_hale at left:
        zoom 0.7

    samir_hale "Mira—there's momentum. I just finished talking to the city liaison. They want to meet. Not a token meeting; they want to hear a plan that won't make them look bad."
    show mira_solace at right:
        zoom 0.7

    mira_solace "And Liora? What are they saying from Aegis' side?"
    "Samir shifts, scanning the crowd as if the answer might be written somewhere in the rhythm of feet. He doesn't meet your eyes right away."

    samir_hale "She's—there's already talk of a press statement. But the liaison hinted she might prefer negotiated optics over another spectacle. That could be leverage if we hold to it. Or it could be a trap for a headline."
    "You let the word 'leverage' sit. It could be the hinge that swings something open, but hinges rust if you aren't careful who oils them."

    mira_solace "So we have three directions: build something that lasts for the community, force binding concessions from Aegis, or push this outwards so other harbors see us. All of them need structure. All of them need people who will stay if applause dies."

    samir_hale "Exactly. There's room to make something durable—if you want it. But durable means committees and meetings and legal frameworks. It means boring paperwork as much as late-night urgency."
    "You think of Noah's paint-smeared hands and his stubborn, stubborn calm. You think of Etta's stories about houses that survived because neighbors fixed roofs together. You think of Arin's camera that makes faces into evidence."

    menu:
        "Ask Samir to call Etta and bring elders into the room":
            "Samir's jaw softens. He taps the tablet and the little heat-map of contacts blooms. 'She'll steady the room,' he says. 'If Etta agrees, haggling over language gets easier.'"
        "Ask Arin to pull up tonight's footage and check the narrative thread":
            "Arin looks up from where he's editing; his grin is quick and conspiratorial. 'Give me five minutes. I'll stitch the chant to the interviews—we can make a sequence that beats their press release.'"

    # --- merge ---
    "Narrative continues"
    # [Scene: Causeway | Early Night]
    hide samir_hale
    hide mira_solace

    scene bg ch11_e67f19_2 at full_bg
    # play music "music_placeholder"  # [Music: Acoustic guitar motif woven with fingers of synth]
    # play sound "sfx_placeholder"  # [Sound: Low hum of distant engines, a gull that hasn't learned to fear the city]
    "You walk the narrow planks of the causeway toward Etta's circle. Her scarves are the same patchwork of seaside memory you remember—salt-stiffened and woven with small shells. Around her, people lower their voices to a careful intensity; the kind that listens as if every word is a seed."
    show etta_maren at left:
        zoom 0.7

    etta_maren "The city's listening, child. That noise you made—it's a net. Fish will be caught. But what kind? Will it feed the whole neighborhood, or only the ships?"
    "You feel the question land in the part of you that catalogues consequences. You want to answer with a protocol, with steps and measurements. Instead you find the simpler language that Etta honors."
    show mira_solace at right:
        zoom 0.7

    mira_solace "We want something that keeps homes, keeps shops. That gives people time to adapt rather than being pushed away."

    etta_maren "Good. Promises with time are less hungry. But promises also have teeth. You need people who will bite on them when suits try to smooth edges. Who stands ready to bite?"
    "Arin Voss, who has been moving in that easy orbit of yours all evening, steps forward with a small roll of footage and a battery that smells faintly of solder. He projects a quick loop on"
    "a portable screen—faces, flooded stoops, a child with a rag doll singing about the pier. The circle leans in."
    show arin_voss at center:
        zoom 0.7

    arin_voss "This is what we hold. Not slogans. Not slogans alone. Real stories. They show the cost if we do nothing, and they show the cost if we do the wrong thing."
    "Etta reaches and touches your wrist briefly, not sentimental—practical, like checking a pulse."

    etta_maren "You have the people's songs and the people's names. Make sure the songs have places to land."
    "You imagine structures—laws, mutual aid funds, technical manuals that aren't written to confuse. The rising chord inside you tightens into determination."

    menu:
        "Accept Etta's woven talisman to carry as a symbol":
            "Etta loops a tiny shell into the cuff of your scarf, her fingers efficient. 'Keep it near the heart,' she says. It's a small, solemn promise."
        "Politely decline, preferring to carry the people's names in your notebook":
            "You tap the closed notebook. 'Names hold better than talismans,' you say, and Etta smiles—it's not disapproval, just recognition of the way your mind wants to hold the world."

    # --- merge ---
    "Narrative continues"
    # [Scene: Neon-Lit Streets | Late Night]
    hide etta_maren
    hide mira_solace
    hide arin_voss

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Upbeat, hopeful motif with brass swells and gentle electronic rhythm]
    # play sound "sfx_placeholder"  # [Sound: The distant clatter of a construction site, passing scooters, a reporter's mic catching breath]
    "By the time you step into the neon-lit stretch near the Aegis field office, the air vibrates with the afterglow of media attention. Cameras angle, lights flare soft halos, and a small crowd has gathered to"
    "watch what will be said next. You can taste the citrus of a lighting crew's detergent and the metallic tang of stress in the voices that pass."
    "Liora Kade arrives with the measured poise of someone who spends her life making decisions look inevitable. Her coat is wet at the hem from the harbor spray but immaculate otherwise. When she sees you she inclines her head in that way that is almost an apology before negotiation."
    show liora_kade at left:
        zoom 0.7

    liora_kade "Mira. You did what you needed to do tonight. Effective. Public pressure is…useful. It creates space."
    show mira_solace at right:
        zoom 0.7

    mira_solace "It created a lot of space. What do you want us to do with it?"

    liora_kade "We can put formal assurances on paper. Binding commitments. Independent oversight. Funds allocated to home retrofits and relocation where necessary. Or—if you prefer—a broader regional program with partners who can scale these models. You have attention. We can convert it into enforceable results."
    "Arin Voss bristles, stepping between you and the outline of corporate generosity. He leans in, eyes bright, a quick edge to his voice that begs caution."
    show arin_voss at center:
        zoom 0.7

    arin_voss "Or you can use that 'formal assurance' to paper over displacement while towers go up behind a floodwall. We saw the PR deck. We know how smooth words get."
    "Liora Kade's expression flickers—small, practiced shifts that keep intent hidden. For a moment she is almost unreadable, then she opens her hands as if showing they carry no dagger."

    liora_kade "I understand the skepticism. I don't ask you to trust my company blindly. I ask for a negotiation with teeth. Independent auditors. Community seats at the table. Consequences for violation."
    "Samir arrives now, breathless, having come straight from a late municipal briefing. He places a hand on your shoulder in a quick, steadying gesture."
    hide liora_kade
    show samir_hale at left:
        zoom 0.7

    samir_hale "They asked about oversight language—about third-party verification. That could be a hard line. Etta would want seats for elders. Arin would want transparency. If you want concessions that bind, this is exactly the moment you can anchor them."
    "Your mind ricochets across considerations: legal enforceability, community control, the risk of compromise, the reach of regional scaling. Each option enlarges the map of possible futures. The city could get a durable body to negotiate—a civic"
    "coalition that outlives headlines. You could leverage this attention into legally binding promises from the company that has the engineering muscle. Or you could push outward, letting media partnerships turn the harbor story into a model"
    "for many other cities."
    "Liora Kade's voice is softer now, as if she senses you're holding the hinge."
    hide mira_solace
    show liora_kade at right:
        zoom 0.7

    liora_kade "Whatever you choose, choose with the intent to make it lasting. Token gestures won't survive the next storm. We can make things hold."

    arin_voss "We make them hold together. Not just 'hold' for those who can afford it."
    "You listen to the three currents pulling—organization, leverage, amplification—and feel, beneath the tilt of pressure, the hopeful hum of possibility. The campaign has done what it needed to do: it opened options. Now those options are yours to shape."
    "You lift your hand, the sound of the crowd like a memory at your back. The decision waits, but for the first time in a long while the waiting feels like a promise instead of a threat."
    # play music "music_placeholder"  # [Music: Swell into an optimistic chord]
    hide arin_voss
    hide samir_hale
    hide liora_kade

    scene bg ch11_e67f19_4 at full_bg

    menu:
        "Institutionalize a civic coalition":
            jump chapter12
        "Negotiate binding concessions with Aegis":
            jump chapter16
        "Scale regionally with media partnerships":
            jump chapter18
    return
