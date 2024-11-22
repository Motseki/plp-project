// import React from 'react'
// import NavBar from './components/NavBar'
// import Jumbotron from './components/Jumbotron'
// import BlogHeading from './components/BlogHeading'
// import BlogContainer from './components/BlogContainer'
// import Footer from './components/Footer'
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom'
import MainLayout from './layouts/MainLayout'
import HomePage from './pages/HomePage'
import AddBlogPage from './pages/AddBlogPage'
import PageNotFound from './pages/PageNotFound'
import DetailPage from './pages/DetailPage'
import EditBlogPage from './pages/EditBlogPage'
import axios from 'axios'
import { toast } from 'react-toastify'
import JoinUsPage from './pages/JoinUsPage'
import Founders from './pages/Founders'
import Investors from './pages/Investors'
import FundingConnect from './pages/FundingConnect'
import Groups from './pages/Groups'
import StartupJobs from './pages/StartupJobs'
import KnowledgeHub from './pages/KnowledgeHub'
import Events from './pages/Events'

const App = () => {

  const createBlog = (data) => {
    axios.post("http://127.0.0.1:8000/blogs/", data)
    .then(res => {
       console.log(res.data)
       toast.success("Blog added successfully!")
  })
    .catch(err => console.log(err.message))
  }

  const updateBlog = (data, slug) => {
    axios.put(`http://127.0.0.1:8000/blogs/${slug}/`, data)
    .then(res => {
      toast.success("Blog UPDATED successfully!")
    })
    .catch(err => console.log(err.message))
  }

  const router = createBrowserRouter(createRoutesFromElements(
    <Route path="/" element={<MainLayout />}>
      <Route index element={<HomePage />} /> 
      <Route path="/founders" element={<Founders />} />
      <Route path="/investors" element={<Investors />} />
      <Route path="/funding-connect" element={<FundingConnect />} />
      <Route path="/groups" element={<Groups />} />
      <Route path="/startup-jobs" element={<StartupJobs />} />
      <Route path="/knowledge-hub" element={<KnowledgeHub />} />
      <Route path="/events" element={<Events />} />
      <Route path="/join-us" element={<JoinUsPage createBlog={createBlog} />} />
      <Route path="/add-blog" element={<AddBlogPage createBlog={createBlog} />} />
      <Route path="/blogs/:slug" element={<DetailPage />} />
      <Route path="blogs/edit/:slug" element={<EditBlogPage updateBlog={updateBlog} />} /> 
      <Route path="*" element={<PageNotFound />} /> 
    </Route>
  ))

  return (
    <RouterProvider router={router} />
  )
}

export default App