import React, { useState } from 'react';
import Button from '@material-ui/core/Button'
import { Chip, TextField } from '@material-ui/core'

function Page() {
    let chips = ["k8s", "ci/cd", "devops"]

    const [tags, setTags] = useState(new Set());

    const onClick = (item) => {
        setTags(tags.add(item.target.innerText))
        console.log(tags)
    }

    const chipEls = chips.map(item => 
        <Chip label={item} clickable={true} onClick={onClick} />
    )

    const tagsEl = Array.from(tags).join()


    return (
        <div>
            <form>
            <TextField value="sdsad" />

            { chipEls}

            </form>
        </div>
    )
}

export default Page
