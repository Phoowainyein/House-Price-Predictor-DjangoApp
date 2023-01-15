import PropTypes from 'prop-types'

const FormRegister = ({ type, name, value, handleChange, labelText }) => {
  return (
    <div className="form-row">
      <label htmlFor={name} className="form-label">
        {labelText || name}
      </label>
      <input
        type={type}
        value={value}
        name={name}
        onChange={handleChange}
        className="form-input"
      />
    </div>
  )
}

export default FormRegister

FormRegister.propTypes = {
  type: PropTypes.any,
  name: PropTypes.string,
  value: PropTypes.string,
  handleChange: PropTypes.func,
  labelText: PropTypes.string
}
