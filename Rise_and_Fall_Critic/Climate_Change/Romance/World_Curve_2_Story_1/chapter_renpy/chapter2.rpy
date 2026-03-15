label chapter2:

    # [Scene: Tideworks Lab | Morning — hours before the council hearing]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of pumps, the sharp click of instruments, gulls distant and metallic wind against corrugated metal.]
    # play music "music_placeholder"  # [Music: Sparse, descending piano motif]
    "You push the lab door open and the smell hits you first — brine and machine oil, the faint, sweet rot of algae. The air is humid enough to carry the salt into the back of"
    "your throat. Theo looks up from a tangle of sensors; his grin is quick but doesn't quite reach his eyes."
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "You're early. Or I'm late. Depends how you want to count it."
    "You take off your scarf and shake out the damp. Your fingers leave a ring of salt on the workbench where you set your journal down. The pendant under your shirt feels like a small, steady stone against your sternum."
    show elias_navin at right:
        zoom 0.7

    elias_navin "We got a longer window on the last tide. The modules held at thirty percent more dissipation than before, but the anchoring failed in the backwash. It's... complicated."
    "You step closer. The modules are smaller than you imagined, more fragile in the hand, like the thing you want them to be — not weapons, but tissue for the sea to knit into armor."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "Complicated won't stand in the council chamber. People want numbers and a straight story. They don't want nuance when their roofs leak."

    elias_navin "And I don't want to hand them a false certainty. That—' (he taps the side of the basin) '—will be used as a data point. We have to be honest about margins and failure modes."
    "You feel the old argument warm in your chest: the pragmatic need to do the right thing versus the strategic temptation to simplify for power. Rosa's words from the last evening weave at the edge of your mind—make them count as people."
    "Theo interjects, pruning a sensor cable with a pocket knife. His fingers are quick; his voice a nervous cadence that tries to distract from the fact that the lab has been cobbling miracles for months."

    theo_mendes "We can patch anchors for the demo. New composite runners, a cruciform brace. It'll add weight but—"

    elias_navin "And then you claim a different test. We either present the controlled results, or we build a claim on retrofits that weren't in the dataset."
    "Your jaw tightens. You can feel the ache behind your ribs, the old guilt that says if you don't push, people will be left holding wet roofs and bitter mouths. But you also know the cost of overreach — someone dies because you promised the sea a lie."

    menu:
        "Inspect the anchoring on the reef modules":
            "You kneel beside the tray, hands near the filigree of bio-composite. The texture is rough and resigned; you can picture the anchors snagging on rubble instead of clean sand. It makes your stomach drop, but you also notice a hairline seam where a better bond could be tried. Theo leans over, eyes bright with a plan that is not entirely baked."
        "Ask Elias for a simple summary we can say in the hearing":
            "You look at Elias with the weight of the room already on your shoulders. He inhales slowly, then pins you with a look of tired calculation: 'We can say three things: observed dissipation percentage, failure mode in heavy backwash, and an immediate pilot we can fund with local labor.' It's concise — true, but it says nothing about the human stories you wanted to foreground."

    menu:
        "Call Jun's office and demand to add our data to the public feed":
            "Your finger hovers on the contact icon. If you call, you risk confronting him and forcing a bureaucratic scrape that could either embarrass him into inclusion or close a door you need open. Theo watches you like someone waiting to see if the tide will break left or right."
        "Keep the test small and controlled within Tideworks, then release findings on our own timeline":
            "You imagine the press release: a messy but honest story, community faces, sensor graphs. It will ruffle feathers and might be drowned out by City Hall optics. Elias leans in, weighing the scientific integrity against the political reality; he's quietly favoring truth over show."

    jump chapter3
    return
