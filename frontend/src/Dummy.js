import { useState } from "react"


function Dummy() {
    const [status, setStatus] = useState("200")

    return (
        <div>
            Hello {status}
        </div>
    )
}

export default Dummy