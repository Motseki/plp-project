import { useState } from "react"
import { useNavigate } from "react-router-dom"

const JoinUsPage = ({createBlog}) => {

  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  const navigate = useNavigate()

  const newBlog = {
    title:title,
    content:content
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(newBlog)
    createBlog(newBlog)
    navigate("/")
  }

  return (
	<div className="flex justify-center items-center h-auto mt-10 border-purple-900">
  <form className="w-full max-w-lg bg-white p-8 rounded-lg shadow-lg" onSubmit={handleSubmit}>
    <p className="text-2xl mb-4 text-center font-semibold">Join Our Community</p>
    <div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">Title</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
	<div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">First name</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
	<div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">Last name</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
	<div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">Password</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
	<div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">Email</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
	<div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">Confirm email</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
	<div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">Current city</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
	<div className="mb-8">
      <label htmlFor="input" className="block text-gray-700 text-sm font-bold mb-2">Current country</label>
      <input 
        id="input"
        onChange={(e) => setTitle(e.target.value)}
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        placeholder="Enter your input"
        required 
      />
    </div>
    {/* <div className="mb-8">
      <label htmlFor="textarea" className="block text-gray-700 text-sm font-bold mb-2">Content</label>
      <textarea 
      onChange={(e) => setContent(e.target.value)}
        id="textarea"  
        className="border-2 border-purple-900 rounded w-full py-2 px-3 text-gray-950 leading-tight focus:outline-none focus:shadow-outline" 
        rows="6" 
        placeholder="Enter your message" 
        required
      ></textarea>
    </div> */}
    <div className="flex items-center justify-center">
      <button 
        type="submit" 
        className="bg-purple-500 hover:bg-purple-700 w-full text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Next
      </button>
    </div>
  </form>
</div>

  )
}

export default JoinUsPage